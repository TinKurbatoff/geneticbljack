import random, copy, dealer, curses, time, subprocess, os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main(stdscr):
    """checking for keypress"""
    stdscr.nodelay(True)  # do not wait for input when calling getch
    return stdscr.getch()

def whait_for_keys_press(prompt, key1, key2, key3, key4):
    """ checking for 2 options of key pressed with prompt """
    print(prompt)
    while True:
      Key_pressed = curses.wrapper(main)
      #if Key_pressed != (-1): print(Key_pressed) # displays number of key
      if Key_pressed == key1:
        break
      if Key_pressed == key2:
        break
      if Key_pressed == key3:
        break  
      if Key_pressed == key4:
        break  
      time.sleep(0.1)
    return Key_pressed 

# this section checks if the player would like to play with betting enabled or not.  If they choose yes,
# then 'betting' = True, and a set of 'if betting = True:' statements throughout the program turn on
player_wallet = 22.5  
print("Would you like to change bets?")
betting_on = input("Type Yes if so:")
print("")
if betting_on == 'Yes':
  betting = True
else:
  betting = False

# game setup
keep_playing = True
while keep_playing:
  subprocess.call("clear", shell=True) # clear screen
  # this block here copies a new deck into the playing_deck variable, and resets the other playing variables
  playing_deck = copy.copy(dealer.the_deck)
  player_hand = []
  player_score = 0
  player_2nd_hand = []
  player_2nd_score = 0

  dealer_hand = []
  dealer_score = 0
  in_game = True
  # this block draws the player's starting hand, and tells them what they have
  player_hand.append(dealer.draw_card(playing_deck)) #player get card
  dealer_hand.append(dealer.draw_card(playing_deck)) #dealer get card
  player_hand.append(dealer.draw_card(playing_deck)) #player get card
  dealer_hand.append(dealer.draw_card(playing_deck)) #dealer get card
  dealer_score = dealer.compute_score(dealer_hand) # dealer score calculation
  player_score = dealer.compute_score(player_hand) # player score calculation

  # here the player places their bet
  player_bet = 5 # standard bet $5
  if player_wallet < player_bet:
    player_wins = False
    in_game = False  
    print("Out of money!")
    break
  player_wallet = player_wallet - player_bet

  #print("Dealer's card (all): "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
  print("Player wallet: " + str(player_wallet) + " | Bet: "+str(player_bet))
  print()
  print("Dealer's card upright: ## "+ str(dealer.cards_in_hand_one(dealer_hand,1)))     
  print()
  print("Your hand: " + dealer.cards_in_hand(player_hand))
  print("your score: " + str(player_score))
  print("")
  if betting == True:
      player_bet = 5   
      while player_bet == 0:
        try:
          player_bet = int(input("How many credits would you like to wager?"))
          if player_bet > player_wallet:
            print("You don't have that many credits to wager, try again!")
            player_bet = 0
        except:
          print("That's not a number, try again!")
          player_bet = 0
  print("")
  # >>> If dealer have initial black jack (no insurance!)
  if dealer_score == 21:
    in_game = False
    print(bcolors.WARNING + "Dealer got the black jack!" + bcolors.ENDC)
    if player_score == 21: 
      print("Tie! The bet refunded.")
      player_wallet = player_wallet + player_bet
    else:
      print("you lost your bet")  



  # =============   This is the start of the proper game loop  ===========================
  player_wins = None
  hit_played = False
  while in_game:
    # >>> If player have initial black jack (no insurance!)
    if player_score == 21:
      print(bcolors.WARNING + "Plyer got the black jack!" + bcolors.ENDC)
      print("Dealer's hand: "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
      print("You get your bet 3:2")
      player_wallet = player_wallet + player_bet + player_bet*(3/2) # Blackjack 3:2 premium  
      break
    # Ask for key / if no enough funds - Double down = hit.
    keep_going = whait_for_keys_press("Would you like to draw a card? (Hit/Stay/Double/sPlit)",104,115,100,112)
    #print(keep_going, player_bet, player_wallet) # for debug porposes
    if keep_going == 100:
      if (player_bet > player_wallet): 
        keep_going = 104 # replace to hit if no enough funds for double betting
        print("No enough funds to Double. You hit.")
    if keep_going == 104: keep_going = "hit"
    if keep_going == 115: keep_going = "stay"
    if keep_going == 100: keep_going = "double_down"
    if keep_going == 112: keep_going = "split"

    # ===== SPLIT ====== if the player chooses to Split cards...
    if keep_going == "split":
     if not hit_played: 
      print("Split")
      player_hand.append(dealer.draw_card(playing_deck))
      player_score = dealer.compute_score(player_hand)
      if player_score == 21:
        print("Current hand: " + dealer.cards_in_hand(player_hand))
        print(bcolors.WARNING + "Plyer got the black jack!" + bcolors.ENDC)
        print("Dealer's hand: "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
        print("You get your bet 3:2")
        player_wins = False
        player_wallet = player_wallet + player_bet + player_bet*(3/2) # Blackjack 3:2 premium  
        break
      if player_score > 21:
        print("Current hand: " + dealer.cards_in_hand(player_hand))
        print("Current score: " + str(player_score))
        print('')
        print(bcolors.FAIL + "Oh no!  You went bust!" + bcolors.ENDC )
        player_wins = False
        in_game = False
      elif len(player_hand) > 4:
        print(bcolors.WARNING + "Wow!  You got a 'Five Card Charlie'!  You Win!" + bcolors.ENDC)
        player_wins = True
        in_game = False
      else:
        print("Current hand: " + dealer.cards_in_hand(player_hand))
        print("Current score: " + str(player_score) + "\n")
   
    # ===== DOUBLE DOWN ====== if the player chooses to Double down...
    if keep_going == "double_down": 
      if not hit_played:
        keep_going = "stay" # to pass the next turn to dealer
        player_wallet = player_wallet - player_bet # extra bet
        player_bet = player_bet + player_bet
        player_hand.append(dealer.draw_card(playing_deck))
        player_score = dealer.compute_score(player_hand)      
        if player_score > 21:
          print("Current hand: " + dealer.cards_in_hand(player_hand))
          print("Current score: " + str(player_score))
          print('')
          print(bcolors.FAIL + "Oh no!  You went bust!" + bcolors.ENDC )
          player_wins = False
          in_game = False   
          break   
        print("Double down! Player wallet: " + str(player_wallet) + " | Bet: "+str(player_bet))
        print("Current hand: " + dealer.cards_in_hand(player_hand) + " | => " + str(player_score))
        if player_score == 21:
          print(bcolors.WARNING + "Plyer got the black jack!" + bcolors.ENDC)
          print("Dealer's hand: "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
          print("You get your bet 3:2")
          player_wins = False
          player_wallet = player_wallet + player_bet + player_bet*(3/2) # Blackjack 3:2 premium  
          break
    # ===== HIT ====== if the player chooses to hit...
    if keep_going == "hit":
      hit_played = True
      player_hand.append(dealer.draw_card(playing_deck))
      player_score = dealer.compute_score(player_hand)
      if player_score == 21:
        print("Current hand: " + dealer.cards_in_hand(player_hand))
        print(bcolors.WARNING + "Plyer got the black jack!" + bcolors.ENDC)
        print("Dealer's hand: "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
        print("You get your bet 3:2")
        player_wins = False
        player_wallet = player_wallet + player_bet + player_bet*(3/2) # Blackjack 3:2 premium  
        break
      if player_score > 21:
        print("Current hand: " + dealer.cards_in_hand(player_hand))
        print("Current score: " + str(player_score))
        print('')
        print(bcolors.FAIL + "Oh no!  You went bust!" + bcolors.ENDC )
        player_wins = False
        in_game = False
      elif len(player_hand) > 4:
        print(bcolors.WARNING + "Wow!  You got a 'Five Card Charlie'!  You Win!" + bcolors.ENDC)
        player_wins = True
        in_game = False
      else:
        print("Current hand: " + dealer.cards_in_hand(player_hand))
        print("Current score: " + str(player_score) + "\n")
    

    # ==== STAY ==== if the player chooses to stay, the dealer then draws and plays
    elif keep_going == "stay":

      while dealer_score <= 16:
        dealer_hand.append(dealer.draw_card(playing_deck))
        dealer_score = dealer.compute_score(dealer_hand)
      print("The dealer's hand is: " + dealer.cards_in_hand(dealer_hand))
      print("The dealer's score is: " + str(dealer_score))
      print('')
      if dealer_score > 21:
        print(bcolors.OKBLUE +"The dealer went bust!  You win!" + bcolors.ENDC)
        player_wins = True
        in_game = False
      elif len(dealer_hand) > 4:
        print("The dealder got a 'Five Card Charlie'.  You lose!")
        player_wins = False
        in_game = False
      elif dealer_score == player_score:
        print(bcolors.OKGREEN + "Tie! Bet refunded." + bcolors.ENDC)
        player_wallet = player_wallet + player_bet
        player_wins = False
        in_game = False
      elif dealer_score == 21:
        print(bcolors.WARNING + "Dealer got Blackjack! You lose!" + bcolors.ENDC)
        player_wins = False
        in_game = False        
      elif dealer_score > player_score:
        print(bcolors.FAIL + "The dealer beat you!  You lose!" + bcolors.ENDC)
        player_wins = False
        in_game = False
      else:
        print(bcolors.OKBLUE + "You beat the dealer!  You win!" +  bcolors.ENDC)
        player_wins = True
        in_game = False
  
  # here the player's bet gets resolved
  if player_wins == True: player_wallet = player_wallet + player_bet + player_bet # pays with premium 2:1
  if player_wallet < 1:
      print(bcolors.FAIL + "You've run out of credits!\nGame Over!" + bcolors.ENDC)
      break
  
  # this checks if the player wants to play again
  print("Player wallet: " + str(player_wallet)) # Current account
  check_continue = whait_for_keys_press("Press enter to continue, q — to quit...", 10, 113,999,999) # Hit "Enter"/"q"
  if check_continue == 10:
    if player_wallet >= 5: 
      print('\n````` NEW GAME `````\n')
    else:  
      print("Out of funds. Thanks for playing!")
      keep_playing = False       
  if check_continue == 113: 
    print("Thanks for playing!")
    keep_playing = False 

 
    

