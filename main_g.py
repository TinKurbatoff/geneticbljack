import random, copy, dealer, curses, time, subprocess, os, sys, json, born_next_gen


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

strategy = \
[[115,115,115,115,115,115,115,115,115,115],\
 [115,115,115,115,115,115,115,115,115,115],\
 [115,115,115,115,115,115,115,115,115,115],\
 [115,115,115,115,115,115,115,115,115,115],\
 [115,115,115,115,115,104,104,104,104,104],\
 [115,115,115,115,115,104,104,104,104,104],\
 [115,115,115,115,115,104,104,104,104,104],\
 [115,115,115,115,115,104,104,104,104,104],\
 [104,104,115,115,115,104,104,104,104,104],\
 [100,100,100,100,100,100,100,100,100,100],\
 [100,100,100,100,100,100,100,100,104,104],\
 [104,100,100,100,100,104,104,104,104,104],\
 [104,104,104,104,104,104,104,104,104,104],\
 [104,104,104,104,104,104,104,104,104,104],\
 [104,104,104,104,104,104,104,104,104,104],\
 [104,104,104,104,104,104,104,104,104,104],\
 [104,104,104,104,104,104,104,104,104,104],\

 [115,115,115,115,115,115,115,115,115,115],\
 [115,115,115,115,100,115,115,115,115,115],\
 [100,100,100,100,100,115,115,104,104,104],\
 [104,100,100,100,100,104,104,104,104,104],\
 [104,104,100,100,100,104,104,104,104,104],\
 [104,104,100,100,100,104,104,104,104,104],\
 [104,104,104,100,100,104,104,104,104,104],\
 [104,104,104,100,100,104,104,104,104,104],\
 [104,104,104,100,100,104,104,104,104,104]]  #line 25

# this section checks if the player would like to play with betting enabled or not.  If they choose yes,
# then 'betting' = True, and a set of 'if betting = True:' statements throughout the program turn on
generations = max(int(sys.argv[3]),1) #  ----------> number of generations 
cycles=max(int(sys.argv[2]),1)    #  ---------->  number of species
for genx in range(generations):
  print("Generation: ",genx)
  species = [i for i in range(cycles)]
  best_species=[0,1,2]
  average=0
  av_max=0
  av_min=0
  #print("Played ",cycles," species.")
  for av in range(cycles):
    player_wallet = 0
    wallet_max=0
    wallet_min=0
    xx = 0
    yyy=0
    # ============== GENETIC ALGORYTM ===================
    # read table ("specie") with strategy of playing
    #with open("./species/specie@.json", "r") as f: # optimal strategy
    with open("./species/specie"+str(av)+".json", "r") as f:  # loading specie #av
      #print(av)
      strategy = json.load(f)
    f.closed  

    #====================================================

    played_times = int(sys.argv[1])  # ----------> number of hands
    if played_times == 0: played_times = 500
    #print("Plays " + str(played_times) + " hands.")
    play_decision = [104,115,100] # h s d
    #print("Would you like to change bets?")
    #betting_on = input("Type Yes if so:")
    #print("")
    #if betting_on == 'Yes':
    #  betting = True
    #else:
    #  betting = False

    # game setup
    keep_playing = True
    dd_played = 0
    hits_played = 0
    stay_played = 0
    while keep_playing:
      #/////subprocess.call("clear", shell=True) # clear screen
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
      yyy=yyy+1
      # here the player places their bet
      player_bet = 5 # standard bet $5
      #if player_wallet < player_bet:
      #  player_wins = False
      #  in_game = False  
      #  print("Out of money!")
      #  break
      if player_wallet > wallet_max: wallet_max = player_wallet # remeber max and min of account
      if player_wallet < wallet_min: wallet_min = player_wallet #
      player_wallet = player_wallet - player_bet 

      #print("Dealer's card (all): "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
      #print("Player wallet: " + str(player_wallet) + " | Bet: "+str(player_bet))
      #print()
      #print("Dealer's card upright: ## "+ str(dealer.cards_in_hand_one(dealer_hand,1)))     
      #print()
      #print("Your hand: " + dealer.cards_in_hand(player_hand))
      #print("your score: " + str(player_score))
      #print("")
      #if betting == True:
      #    player_bet = 5   
      #    while player_bet == 0:
      #      try:
      #        player_bet = int(input("How many credits would you like to wager?"))
      #        if player_bet > player_wallet:
      #         print("You don't have that many credits to wager, try again!")
      #          player_bet = 0
      #      except:
      #        print("That's not a number, try again!")
      #        player_bet = 0
      #print("")
      # >>> If dealer have initial black jack (no insurance!)
      if dealer_score == 21:
        in_game = False
      #  print(bcolors.WARNING + "Dealer got the black jack!" + bcolors.ENDC)
        if player_score == 21: 
      #    print("Tie! The bet refunded.")
          player_wallet = player_wallet + player_bet
      #  else:
      #   print("you lost your bet")  



      # =============   This is the start of the proper game loop  ===========================
      player_wins = None
      hit_played = False
      dd_choosen = False
      #print("Next game #"+str(yyy))
      played_times = played_times - 1     
      while in_game:
        # >>> If player have initial black jack (no insurance!)
        if player_score == 21:
      #      print(bcolors.WARNING + "Plyer got the black jack!" + bcolors.ENDC)
      #      print("Dealer's hand: "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
      #      print("You get your bet 3:2")
          player_wallet = player_wallet + player_bet*(3/2) # Blackjack 3:2 premium  
          break
        # Ask for key / if no enough funds - Double down = hit.
        #keep_going = whait_for_keys_press("Would you like to draw a card? (Hit/Stay/Double/sPlit)",104,115,100,112)
        

        # =================== CHOSE NEXT ACTION FROM TABLE  ====================
        #print("pl: ",dealer.cards_in_hand(player_hand))
        #print("dl: ",dealer.cards_in_hand(dealer_hand))
        if played_times == 0 : break
        column_index = dealer_hand[1][1] - 2 #dealer.cards_in_hand_one(dealer_hand,1)
        #>>>> Row in optimal table depends on player cards on hand
        if dealer.ace_check_hand(player_hand) and len(player_hand) == 2:
          row_index = 37 - player_score 
          #print(" -> ace! ",dealer.cards_in_hand(player_hand)) 
          #row_index = 20 - player_score 
          #print(player_hand," ",row_index ," ",column_index)
        else: 
          row_index = 20 - player_score 
        #print("rw:",row_index,"cl:",column_index)
        # optimal strategy
        #os.write(1, b"\r")
        #os.write(1, b".")
        #if (yyy % int(int(sys.argv[1])/500)) == 0: os.write(1, b".")  ### ===== PRINTING DOTS!!!
          #os.write(1, bytes(str(played_times / 1000) + "\r","UTF-8"))
        #  played_times = played_times
        # =========== PLAYING BY STRATEGY ==============================
        try:
          keep_going = strategy[row_index][column_index]  # ====> optimal strategy
          xx = xx +1 
          #keep_going = play_decision[random.randint(0,2)] # ===>  random strategy
        except IndexError:
          print(player_hand," ",dealer_hand)
          print(row_index," ",column_index) 
        except:
          print(sys.exc_info()[2],"!!!")        
        #print(keep_going)
        #os.write(1, bytes("\r"+str(row_index)+" "+str(column_index)+" kg:"+str(keep_going)+ " "\
        #+ str(xx)+" "+str(player_score)+" dd:"+str(dd_choosen)+" h:"+str(hit_played),"UTF-8"))

        #print(keep_going, player_bet, player_wallet) # for debug porposes
        #if keep_going == 100:
        #  if (player_bet > player_wallet): 
        #    keep_going = 104 # replace to hit if no enough funds for double betting
        #    print("No enough funds to Double. You hit.")
        #if keep_going != 100: print(" kg:",keep_going)
        if keep_going == 104: keep_going = "hit"
        if keep_going == 115: keep_going = "stay"
        if keep_going == 100 and hit_played: keep_going = "hit" # no double down after hit   
        if keep_going == 100: keep_going = "double_down"
        if keep_going == 112: keep_going = "split"


        # ===== DOUBLE DOWN ====== if the player chooses to Double down...
        if keep_going == "double_down" and not hit_played: # no double down after hit
            dd_choosen = True
            dd_played = dd_played +1
            keep_going = "stay" # to pass the next turn to dealer
            player_wallet = player_wallet - player_bet # extra bet
            player_bet = player_bet + player_bet
            player_hand.append(dealer.draw_card(playing_deck))
            player_score = dealer.compute_score(player_hand)  
    #        print(dealer.cards_in_hand(player_hand)," ",player_score)    
            if player_score > 21:
    #          print("Current hand: " + dealer.cards_in_hand(player_hand))
    #          print("Current score: " + str(player_score))
    #          print('')
    #          print(bcolors.FAIL + "Oh no!  You went bust!" + bcolors.ENDC )
              player_wins = False
              in_game = False     
     #         print("Double down! Player wallet: " + str(player_wallet) + " | Bet: "+str(player_bet))
     #         print("Current hand: " + dealer.cards_in_hand(player_hand) + " | => " + str(player_score))
              break 
            if player_score == 21:
              #print(bcolors.WARNING + "Plyer got the black jack!" + bcolors.ENDC)
              #print("Dealer's hand: "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
              #print("You get your bet 3:2")
              player_wins = False
              player_wallet = player_wallet + player_bet*(3/2) # Blackjack 3:2 premium  
              break
            
        # ===== HIT ====== if the player chooses to hit...
        if keep_going == "hit":
          hits_played = hits_played +1
          hit_played = True
          player_hand.append(dealer.draw_card(playing_deck))
          player_score = dealer.compute_score(player_hand)
          if player_score == 21:
    #        print("Current hand: " + dealer.cards_in_hand(player_hand))
    #        print(bcolors.WARNING + "Plyer got the black jack!" + bcolors.ENDC)
    #        print("Dealer's hand: "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
    #        print("You get your bet 3:2")
            player_wins = False
            player_wallet = player_wallet + player_bet*(3/2) # Blackjack 3:2 premium  
            break
          if player_score > 21:
    #        print("Current hand: " + dealer.cards_in_hand(player_hand))
    #        print("Current score: " + str(player_score))
    #        print('')
    #        print(bcolors.FAIL + "Oh no!  You went bust!" + bcolors.ENDC )
            player_wins = False
            in_game = False
          if len(player_hand) > 4:
    #       print(bcolors.WARNING + "Wow!  You got a 'Five Card Charlie'!  You Win!" + bcolors.ENDC)
            player_wins = True
            in_game = False
    #    else:
    #       print("Current hand: " + dealer.cards_in_hand(player_hand))
    #       print("Current score: " + str(player_score) + "\n")
        

        # ==== STAY ==== if the player chooses to stay, the dealer then draws and plays
        if keep_going == "stay":
          stay_played = stay_played +1
          while dealer_score < 16:
            dealer_hand.append(dealer.draw_card(playing_deck))
            dealer_score = dealer.compute_score(dealer_hand)
      #     print("The dealer's hand is: " + dealer.cards_in_hand(dealer_hand))
      #     print("The dealer's score is: " + str(dealer_score))
      #    print('')
          if dealer_score > 21:
    #        print(bcolors.OKBLUE +"The dealer went bust!  You win!" + bcolors.ENDC)
            player_wins = True
            in_game = False
          elif len(dealer_hand) > 4:
      #       print("The dealder got a 'Five Card Charlie'.  You lose!")
            player_wins = False
            in_game = False
          elif dealer_score == player_score:
      #       print(bcolors.OKGREEN + "Tie! Bet refunded." + bcolors.ENDC)
            player_wallet = player_wallet + player_bet
            player_wins = False
            in_game = False
          elif dealer_score == 21:
      #       print(bcolors.WARNING + "Dealer got Blackjack! You lose!" + bcolors.ENDC)
            player_wins = False
            in_game = False        
          elif dealer_score > player_score:
    #        print(bcolors.FAIL + "The dealer beat you!  You lose!" + bcolors.ENDC)
            player_wins = False
            in_game = False
          else:
    #        print(bcolors.OKBLUE + "You beat the dealer!  You win!" +  bcolors.ENDC)
            player_wins = True
            in_game = False
      
      # here the player's bet gets resolved
      if player_wins == True: 
        player_wallet = player_wallet + player_bet + player_bet # pays with premium 2:1
      if played_times == 0:
        species[av]=player_wallet  # record result of this particular specie
        average = average + player_wallet # summ up all results for averaging in the end
        av_max= av_max + wallet_max # summ up all results for averaging in the end
        av_min= av_min + wallet_min # summ up all results for averaging in the end
        #print(bcolors.FAIL + "\nAll games played!\nGame Over!" + bcolors.ENDC)
        #print("Thanks for playing!")
        #print("Player wallet: " + str(player_wallet)) # Current account
        #print("Max wallet account: "+str(wallet_max))
        #print("Min wallet account: "+str(wallet_min))    
        #print("dd:", dd_played, ", Hits:", hits_played, ", Stays:", stay_played, ", Total:",dd_played+hits_played+stay_played)
        break
  print("av wallet: ", average/cycles)  
  print(max(species))
  #print("av max:    ",av_max/cycles)   
  #print("av min:    ",av_min/cycles)   
  #print(species) 
  champ = max(species) # define champion in current generation (lowest loss)
  champ = species.index(champ) # get champ index in generation
  species[champ] = min(species) # remove champ from list
  ScndChamp = max(species)
  ScndChamp = species.index(ScndChamp) 
  print("Champion: #", champ, " ", max(species))
  born_next_gen.mutate(champ, ScndChamp, genx, cycles) # mutate, arguments: (the champion index, generation, generation size)

