import random

#This instantiation of a 52 card deck is a set of tuples, each containing a card name string at index 0
#and a card value at index 1.  The .png file names at index 2 are from an attempt to create a graphical
#representation of the cards that were in play, which did not pan out.
#the_deck = [("Ace of Hearts", 11, "ace-of-hearts.png"), ("2 of Hearts", 2, "two-of-hearts.png"), \
#("3 of Hearts", 3, "three-of-hearts.png"), ("4 of Hearts", 4, "four-of-hearts.png"), \
#("5 of Hearts", 5, "five-of-hearts.png"), ("6 of Hearts", 6, "six-of-hearts.png"), \
#("7 of Hearts", 7, "seven-of-hearts.png"), ("8 of Hearts", 8, "eight-of-hearts.png"), \
##("9 of Hearts", 9, "nine-of-hearts.png"), ("10 of Hearts", 10, "ten-of-hearts.png"), \
#("Jack of Hearts", 10, "jack-of-hearts.png"), ("Queen of Hearts", 10, "queen-of-hearts.png"), \
#("King of Hearts", 10, "king-of-hearts.png"), ("Ace of Spades", 11, "ace-of-spades.png"), \
#("2 of Spades", 2, "two-of-spades.png"), ("3 of Spades", 3, "three-of-spades.png"), \
#("4 of Spades", 4, "four-of-spades.png"), ("5 of Spades", 5, "five-of-spades.png"), \
#("6 of Spades", 6, "six-of-spades.png"), ("7 of Spades", 7, "seven-of-spades.png"), \
#("8 of Spades", 8, "eight-of-spades.png"), ("9 of Spades", 9, "nine-of-spades.png"), \
#("10 of Spades", 10, "ten-of-spades.png"), ("Jack of Spades", 10, "jack-of-spades.png"), \
#("Queen of Spades", 10, "queen-of-spades.png"), ("King of Spades", 10, "king-of-spades.png"), \
#("Ace of Diamonds", 11, "ace-of-diamonds.png"), ("2 of Diamonds", 2, "two-of-diamonds.png"), \
#("3 of Diamonds", 3, "three-of-diamonds.png"), ("4 of Diamonds", 4, "four-of-diamonds.png"), \
#("5 of Diamonds", 5, "five-of-diamonds.png"), ("6 of Diamonds", 6, "six-of-diamonds.png"), \
#("7 of Diamonds", 7, "seven-of-diamonds.png"), ("8 of Diamonds", 8, "eight-of-diamonds.png"), \
#("9 of Diamonds", 9, "nine-of-diamonds.png"), ("10 of Diamonds", 10, "ten-of-diamonds.png"), \
#("Jack of Diamonds", 10, "jack-of-diamonds.png"), ("Queen of Diamonds", 10, "queen-of-diamonds.png"), \
#("King of Diamonds", 10, "king-of-diamonds.png"), ("Ace of Clubs", 11, "ace-of-clubs.png"), \
#("2 of Clubs", 2, "two-of-clubs.png"), ("3 of Clubs", 3, "three-of-clubs.png"), \
#("4 of Clubs", 4, "four-of-clubs.png"), ("5 of Clubs", 5, "five-of-clubs.png"), \
#("6 of Clubs", 6, "six-of-clubs.png"), ("7 of Clubs", 7, "seven-of-clubs.png"), \
#("8 of Clubs", 8, "eight-of-clubs.png"), ("9 of Clubs", 9, "nine-of-clubs.png"), \
#("10 of Clubs", 10, "ten-of-clubs.png"), ("Jack of Clubs", 10, "jack-of-clubs.png"), \
#("Queen of Clubs", 10, "queen-of-clubs.png"), ("King of Clubs", 10, "king-of-clubs.png")]

the_deck = [("Ace♥︎", 11, "ace-of-hearts.png"), ("2♥︎", 2, "two-of-hearts.png"), \
("3♥︎", 3, "three-of-hearts.png"), ("4♥︎", 4, "four-of-hearts.png"), \
("5♥︎", 5, "five-of-hearts.png"), ("6♥︎", 6, "six-of-hearts.png"), \
("7♥︎", 7, "seven-of-hearts.png"), ("8♥︎", 8, "eight-of-hearts.png"), \
("9♥︎", 9, "nine-of-hearts.png"), ("10♥︎", 10, "ten-of-hearts.png"), \
("Jack♥︎", 10, "jack-of-hearts.png"), ("Queen♥︎", 10, "queen-of-hearts.png"), \
("King♥︎", 10, "king-of-hearts.png"), ("Ace♠︎", 11, "ace-of-spades.png"), \
("2♠︎", 2, "two-of-spades.png"), ("3♠︎", 3, "three-of-spades.png"), \
("4♠︎", 4, "four-of-spades.png"), ("5♠︎", 5, "five-of-spades.png"), \
("6♠︎", 6, "six-of-spades.png"), ("7♠︎", 7, "seven-of-spades.png"), \
("8♠︎", 8, "eight-of-spades.png"), ("9♠︎", 9, "nine-of-spades.png"), \
("10♠︎", 10, "ten-of-spades.png"), ("Jack♠︎", 10, "jack-of-spades.png"), \
("Queen♠︎", 10, "queen-of-spades.png"), ("King♠︎", 10, "king-of-spades.png"), \
("Ace♦", 11, "ace-of-diamonds.png"), ("2♦", 2, "two-of-diamonds.png"), \
("3♦", 3, "three-of-diamonds.png"), ("4♦", 4, "four-of-diamonds.png"), \
("5♦", 5, "five-of-diamonds.png"), ("6♦", 6, "six-of-diamonds.png"), \
("7♦", 7, "seven-of-diamonds.png"), ("8♦", 8, "eight-of-diamonds.png"), \
("9♦", 9, "nine-of-diamonds.png"), ("10♦", 10, "ten-of-diamonds.png"), \
("Jack♦", 10, "jack-of-diamonds.png"), ("Queen♦", 10, "queen-of-diamonds.png"), \
("King♦", 10, "king-of-diamonds.png"), ("Ace♣︎", 11, "ace-of-clubs.png"), \
("2♣︎", 2, "two-of-clubs.png"), ("3♣︎", 3, "three-of-clubs.png"), \
("4♣︎", 4, "four-of-clubs.png"), ("5♣︎", 5, "five-of-clubs.png"), \
("6♣︎", 6, "six-of-clubs.png"), ("7♣︎", 7, "seven-of-clubs.png"), \
("8♣︎", 8, "eight-of-clubs.png"), ("9♣︎", 9, "nine-of-clubs.png"), \
("10♣︎", 10, "ten-of-clubs.png"), ("Jack♣︎", 10, "jack-of-clubs.png"), \
("Queen♣︎", 10, "queen-of-clubs.png"), ("King♣︎", 10, "king-of-clubs.png")]
#♤♧♡♢J♠︎♣︎♥︎♦︎

# when given a list, this function will choose an item in the list, remove it from the list, and return it.
# it is intended to choose a card out of a list representing a deck, remove it from the deck list,
# and return it to a list representing a player's hand.
def draw_card(x):
  drawn_card = random.choice(x)
  x.remove(drawn_card)
  return drawn_card

# this function takes the intergers from the card tuples and puts them into a list of values.
# it then checks to see if the sum of the values would be over 21.  If they are, it checks if there
# are any 11s in the value list, representing aces.  If so, it replaces one of the 11s with a 1, and
# checks the sum again.  It continues this until the value is less than 21, or there are no more aces
# in the list.  Then, it returns the final total for the values.  This is then the value of a player's hand
# for the purposes of scoring.
def ace_check_hand(x):
  value_set = []
  for i in x:
    value_set.append(i[1])  
  ace_check = False
  if 11 in value_set:
    ace_check = True
  return ace_check


def compute_score(x):
  total = 0
  value_set = []
  for i in x:
    value_set.append(i[1])  
  total = sum(value_set)
  ace_check = True
  while ace_check == True:
    if total > 21 and 11 in value_set:
      value_set.remove(11)
      value_set.append(1)
      total = sum(value_set)
    else:
      ace_check = False
  return total

# this function is not as necessary for playing the game, but helps with readability.  It takes the card
# tuples in a hand list, and extracts the card name strings.  These are then concatenated, and then returned
def cards_in_hand(x):
  hand = []
  for i in x:
    hand.append(i[0])
  handstring = hand[0]
  for i in hand[1:]:
    handstring = handstring + ', ' + i
  return handstring

def cards_in_hand_one(x,idx):
  #for i in x:
  #  hand.append(i[idx])
  #  print("hand: " + str(hand),"i: "+str(i),i[1]) 
  handstring = x[idx][0]
  #for i in hand[idx:]:
  #  handstring = handstring + ', ' + i
  return handstring

  