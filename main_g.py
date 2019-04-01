#import random, copy, dealer, curses, time, subprocess, os, sys, json, born_next_gen, time
import random, copy, dealer, curses, os, subprocess, sys, json, born_next_gen, time
import multiprocessing


# The idea of the blackjack code is got from https://trinket.io/python3/9c2e46209e
# The optimal strategy was described (as well as a genetic approach) at 
#     https://towardsdatascience.com/winning-blackjack-using-machine-learning-681d924f197c

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Global variables
Average = 0; # average earning by the generation
av_max = 0; # max arned by the generation
av_min = 0; # minimum earned by the generation
played_times = 0; # how much hands play per specie 
playing_deck_flagged = [True]*52

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


# === table with well-known optimal strategy, not used for work, for debugging only.
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

def playing_generation(generation_size):
# ========== PLAYING FOR EVERY SPECIE IN GENERATION ===========
  global Average 
  global av_max
  global av_min
  global played_times 
  global playing_deck_flagged 
  for av in range(generation_size):  # Generation: playing for every specie in generation
    player_wallet = 0
    wallet_max=0 # maximum funds earned with this specie
    wallet_min=0 # minimum funds earned with specie
    played_cards = 0 # counts of every card played with dealer
    Games_count=0 # games played with current specie
    # ============== GENETIC ALGORYTM ===================
    # read table ("specie") with strategy of playing
    #with open("./species/specie@.json", "r") as f: # test with the optimal strategy
    with open("./species/specie"+str(av)+".json", "r") as f:  # loading rules table of the specie #av 
      #print(av)
      strategy = json.load(f)
    f.closed  

    #====================================================

    played_times = int(sys.argv[1])  # ----------> number of hands per specie
    if played_times == 0: played_times = 500 # if no number - play 500 hands by default
    #print("Plays " + str(played_times) + " hands.")
    play_decision = [104,115,100] # 104 - hit, 115 - stay, 100 - double  
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
    # ============= Playing defined hands with this particular specie ==================
    while keep_playing: 
      # this block here copies a new deck into the playing_deck variable, and resets the other playing variables
      playing_deck_flagged = [True] * 52 # reset deck with default      
      player_hand = []
      player_score = 0
      player_2nd_hand = []
      player_2nd_score = 0

      dealer_hand = []
      dealer_score = 0
      in_game = True
      
      # == singleprocessor
      player_hand.append(dealer.draw_card(playing_deck,playing_deck_flagged)) # player get 1st card
      dealer_hand.append(dealer.draw_card(playing_deck,playing_deck_flagged)) # dealer get 1st card
      player_hand.append(dealer.draw_card(playing_deck,playing_deck_flagged)) # player get 2st card
      dealer_hand.append(dealer.draw_card(playing_deck,playing_deck_flagged)) # dealer get 2st card      
      

      # == multiprocessor pooling
      #pool = multiprocessing.Pool(processes=2) # creating pool of multiprocesses
      # this block draws the player's starting hand, and tells them what they have
      #poolresult=pool.map(player_hand.append(dealer.draw_card(playing_deck)),\
      #dealer_hand.append(dealer.draw_card(playing_deck))) #player get 1st card, dealer get 1st card
      #poolresult=pool.map(player_hand.append(dealer.draw_card(playing_deck)),\
      #dealer_hand.append(dealer.draw_card(playing_deck))) #player get 2st card, dealer get 2st card
       
      dealer_score = dealer.compute_score(dealer_hand) # dealer score calculation
      player_score = dealer.compute_score(player_hand) # player score calculation
      Games_count = Games_count + 1
      
      # here the player places their bet
      player_bet = 5 # standard bet $5
      #if player_wallet < player_bet:
      #  player_wins = False
      #  in_game = False  
      #  print("Out of money!")
      #  break
      if player_wallet > wallet_max: wallet_max = player_wallet # remeber max and 
      if player_wallet < wallet_min: wallet_min = player_wallet #   min of account
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
      if dealer_score == 21: #dealer's blackjack
        in_game = False      # skip the following game cycle
      #  print(bcolors.WARNING + "Dealer got the black jack!" + bcolors.ENDC)
        if player_score == 21: # player also has blackjack - bet paid back
      #    print("Tie! The bet refunded.")
          player_wallet = player_wallet + player_bet
      #  else:
      #   print("you lost your bet")  

      # =============   Dealing with current hand  ===========================
      player_wins = None
      hit_played = False
      dd_choosen = False
      #print("Next game #"+str(Games_count))
      played_times = played_times - 1     
      while in_game:
        if played_times == 0 : break # No more games to play        
        # >>> If player have initial black jack (no insurance!)
        if player_score == 21:
          player_wallet = player_wallet + player_bet * (3/2) # Blackjack 3:2 premium  
      #      print(bcolors.WARNING + "Plyer got the black jack!" + bcolors.ENDC)
      #      print("Dealer's hand: "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
      #      print("You get your bet 3:2")
          break
        # Ask for key / if no enough funds - Double down = hit.
        #keep_going = whait_for_keys_press("Would you like to draw a card? (Hit/Stay/Double/sPlit)",104,115,100,112)
        

        # =================== CHOSE NEXT ACTION FROM TABLE  ====================
        #print("pl: ",dealer.cards_in_hand(player_hand))
        #print("dl: ",dealer.cards_in_hand(dealer_hand))
        column_index = dealer_hand[1][1] - 2 #dealer.cards_in_hand_one(dealer_hand,1)
        #>>>> Row in optimal table depends on player cards on hand
        if dealer.ace_check_hand(player_hand) and len(player_hand) == 2:
          row_index = 37 - player_score # the 37 — it is the shift in the strategy table for aces at dealer's hand
          #print(" -> ace! ",dealer.cards_in_hand(player_hand)) 
          #row_index = 20 - player_score 
          #print(player_hand," ",row_index ," ",column_index)
        else: 
          row_index = 20 - player_score # the 20 — it is the shift in the strategy table for normal hands

        #print("rw:",row_index,"cl:",column_index) # checking what was selected from playing table
        # optimal strategy
        #os.write(1, b"\r") 
        #os.write(1, b".")
        #if (Games_count % int(int(sys.argv[1])/500)) == 0: os.write(1, b".")  ### ===== JUST PRINTING DOTS ON SCREEN!!!
          #os.write(1, bytes(str(played_times / 1000) + "\r","UTF-8"))
        #  played_times = played_times
        
        # =============== PLAYING BY STRATEGY TABLE ==================
        try:
          keep_going = strategy[row_index][column_index]  # ====>  strategy from specie table
          played_cards = played_cards + 1 
          #keep_going = play_decision[random.randint(0,2)] # ===>  random strategy
        except IndexError:
          print(player_hand," ",dealer_hand)
          print(row_index," ",column_index) 
        except:
          print(sys.exc_info()[2],"!!!")        
        #print(keep_going)  # debug data on screen
        #os.write(1, bytes("\r"+str(row_index)+" "+str(column_index)+" kg:"+str(keep_going)+ " "\
        #+ str(played_cards)+" "+str(player_score)+" dd:"+str(dd_choosen)+" h:"+str(hit_played),"UTF-8"))

        #print(keep_going, player_bet, player_wallet) # for debug porposes
        #if keep_going == 100:
        #  if (player_bet > player_wallet): 
        #    keep_going = 104 # replace to hit if no enough funds for double betting
        #    print("No enough funds to Double. You hit.")
        #if keep_going != 100: print(" kg:",keep_going)
        # time_stamp=time.time()
        if keep_going == 104: keep_going = "hit"
        if keep_going == 115: keep_going = "stay"
        if keep_going == 100 and hit_played: keep_going = "hit" # no double down after hit   
        if keep_going == 100: keep_going = "double_down"
        if keep_going == 112: keep_going = "split"
        # print(time.time()-time_stamp)

        #time_stamp=time.time()
        # ===== DOUBLE DOWN ====== if the player chooses to Double down...
        if keep_going == "double_down" and not hit_played: # no double down after hit
            dd_choosen = True
            dd_played = dd_played + 1
            keep_going = "stay" # to pass the next turn to dealer
            player_wallet = player_wallet - player_bet # extra bet
            player_bet = player_bet + player_bet
            player_hand.append(dealer.draw_card(playing_deck,playing_deck_flagged))
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
          player_hand.append(dealer.draw_card(playing_deck,playing_deck_flagged))
          player_score = dealer.compute_score(player_hand)
          if player_score == 21:
    #        print("Current hand: " + dealer.cards_in_hand(player_hand))
    #        print(bcolors.WARNING + "Plyer got the black jack!" + bcolors.ENDC)
    #        print("Dealer's hand: "+ dealer.cards_in_hand(dealer_hand))  # what is dealer's hand
    #        print("You get your bet 3:2")
            player_wins = False # no need to pay a general bonus, blackjack
            player_wallet = player_wallet + player_bet*(3/2) # Blackjack 3:2 premium  
            break
          if player_score > 21:
    #        print("Current hand: " + dealer.cards_in_hand(player_hand))
    #        print("Current score: " + str(player_score))
    #        print('')
    #        print(bcolors.FAIL + "Oh no!  You went bust!" + bcolors.ENDC )
            player_wins = False  # no need to pay a general bonus, player is busted! 
            in_game = False
          if len(player_hand) > 4:
    #       print(bcolors.WARNING + "Wow!  You got a 'Five Card Charlie'!  You Win!" + bcolors.ENDC)
            player_wins = True  # to pay a general bonus  2:1
            in_game = False
    #    else:
    #       print("Current hand: " + dealer.cards_in_hand(player_hand))
    #       print("Current score: " + str(player_score) + "\n")
        

        # ==== STAY ==== if the player chooses to stay, the dealer then draws and plays
        if keep_going == "stay":
          stay_played = stay_played +1
          while dealer_score < 16:
            dealer_hand.append(dealer.draw_card(playing_deck,playing_deck_flagged))
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
            player_wins = False  # no need to pay a general bonus, dealer won
            in_game = False
          elif dealer_score == player_score:
      #       print(bcolors.OKGREEN + "Tie! Bet refunded." + bcolors.ENDC)
            player_wallet = player_wallet + player_bet
            player_wins = False  # no need to pay a general bonus, paid already
            in_game = False
          elif dealer_score == 21:
      #       print(bcolors.WARNING + "Dealer got Blackjack! You lose!" + bcolors.ENDC)
            player_wins = False  # no need to pay a general bonus, dealer won
            in_game = False        
          elif dealer_score > player_score:
    #        print(bcolors.FAIL + "The dealer beat you!  You lose!" + bcolors.ENDC)
            player_wins = False  # no need to pay a general bonus, dealer won
            in_game = False
          else:
    #        print(bcolors.OKBLUE + "You beat the dealer!  You win!" +  bcolors.ENDC)
            player_wins = True
            in_game = False
        #print("res: ",time.time()-time_stamp)
      # here the player's bet gets resolved
      if player_wins == True: 
        player_wallet = player_wallet + player_bet + player_bet # pays with premium 2:1
      if played_times == 0:
        species[av]=player_wallet  # record result of this particular specie
        Average = Average + player_wallet # summ up all results for averaging in the end
        av_max= av_max + wallet_max # summ up all results for averaging in the end
        av_min= av_min + wallet_min # summ up all results for averaging in the end
        #print(bcolors.FAIL + "\nAll games played!\nGame Over!" + bcolors.ENDC)
        #print("Thanks for playing!")
        #print("Player wallet: " + str(player_wallet)) # Current account
        #print("Max wallet account: "+str(wallet_max))
        #print("Min wallet account: "+str(wallet_min))    
        #print("dd:", dd_played, ", Hits:", hits_played, ", Stays:", stay_played, ", Total:",dd_played+hits_played+stay_played)
        break





######################################## MAIN CYCLE ##################################################

# this section checks if the player would like to play with betting enabled or not.  If they choose yes,
# then 'betting' = True, and a set of 'if betting = True:' statements throughout the program turn on
try: 
  generations = max(int(sys.argv[3]),1) #  ----------> number of generations 
except:
  print("Use:\n python3 main_g.py [games per specie] [species in every generation] [numebr of generations]")
  exit()
subprocess.call("clear", shell=True) # clears screen
cycles=max(int(sys.argv[2]),1)    #  ---------->  number of species
playing_deck = copy.copy(dealer.the_deck) # create deck with default deck

# ========= MAIN ================
for genx in range(generations): # cycling in generations
  species = [i for i in range(cycles)] # how many species (i.e. playing different cycles per generation)
  print("\033[6;3HGeneration: ",genx, "/", generations, " Species in the generation: ", cycles)
  best_species=[0,1,2] # the array for indexes of the three best species in the generation
  #print("Played ",cycles," species.")
  
  # ============= Testing current generation
  playing_generation(cycles) ####

  # ============= Output of result of current generation
  print("av wallet: ", Average/cycles)  
  print(max(species))
  #print("av max:    ",av_max/cycles)   
  #print("av min:    ",av_min/cycles)   
  #print(species) 
  champ_result = max(species) # define champion in current generation (lowest loss)
  champ = species.index(champ_result) # get champion's index in generation
  species[champ] = min(species) # remove champion from the list to find the second best
  ScndChamp = species.index(max(species)) 
  print("Champion: #", champ, " ", champ_result)
  born_next_gen.mutate(champ, ScndChamp, genx, cycles, genx/generations) # mutate, arguments: (the champion index, generation, generation size)

