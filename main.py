import random
import art
from replit import clear

############### Blackjack Project #####################

def game():
  print(art.logo)

  player_name = input("What is your name? \n")
  print(" ")

  # player_money = 100

    
  player_card_list = []
  player_final_score = 0
  dealer_card_list = []
  dealer_final_score = 0

  card_score = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
  }


  def deal_card():
    """Randomly picks a card"""
    
    card_picker = {
    1: "Ace",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "Jack",
    12: "Queen",
    13: "King"
  }
    
    card_location = random.randint(1,13)
    
    picked_card = card_picker[card_location]
    
    return picked_card
  
  
  def card_dealer(card_pick):
    """Records card score"""
    deal_score = card_score[card_pick]
    return deal_score
    
  #----------Generate a Suit----------
  def suit_picker():
    """Randomly generates a suit for a card"""
    suit_picker = {
      0: "Hearts",
      1: "Diamonds",
      2: "Spades",
      3: "Clubs"
    }
  
    suit_location = random.randint(0,3)
    picked_suit = suit_picker[suit_location]
    return picked_suit
    
  
  def announce_card(name, card_num):
    """Announces full card identity"""
    #eventually find ascii art for user experience update
    card_suit = suit_picker()
    print(f"{name} drew: {card_num} of {card_suit}")
  
  
  #----------Draw Cards----------
  def select_card():
    selected_card = deal_card()
    return selected_card
  
  def score(card):
    score_result = card_dealer(card)
    return score_result
  
  def dealer_draw():
    """Draws a card for the dealer"""
    dealer_card = select_card()
    dealer_score = score(dealer_card)
    dealer_card_list.append(dealer_score)
    return dealer_score
  
   
  
  def player_draw():
    """Draws a card for the player"""
    player_card = select_card()
    player_score = score(player_card)
    player_card_list.append(player_score)
    return player_score
  
    
  
  def find_final_score(list, final_score):
    """Calculates score"""
    exist_ace = list.count(11)
    exist_ten = list.count(10)
    if exist_ace == 1 and exist_ten == 1 and len(list) == 2:
      return 0
    else:
      test_final = 0
      for score in list:
        test_final += score
  
      if test_final > 21:
        for score in list:
          if score == 11:
            score = 1
          final_score += score
        return final_score
      else:
        for score in list:
          final_score += score
        return final_score

  

    
  
  
  
  def play_round():
    # DEALER
    

    if len(dealer_card_list) < 1:
      dealer_card = dealer_draw()
      announce_card("Dealer", dealer_card) 
      print(f"Cards on table: {dealer_card_list}")
      d_score = find_final_score(dealer_card_list, dealer_final_score)
      print(f"Current score: {d_score}")
    else: 
      dealer_card = dealer_draw()
      d_score = find_final_score(dealer_card_list, dealer_final_score)
      

    
    

    
    print(" ")

    # PLAYER
    player_card = player_draw()
    announce_card(player_name, player_card)
    print(f"Cards on table: {player_card_list}")
    p_score = find_final_score(player_card_list, player_final_score)
    print(f"Current score: {p_score}")
  
  
  
  
  


  
  play_round()
  d_score = find_final_score(dealer_card_list, dealer_final_score)
  p_score = find_final_score(player_card_list, player_final_score)
  
  stop_dealing = False
  while stop_dealing == False:
    d_score = find_final_score(dealer_card_list, dealer_final_score)
    p_score = find_final_score(player_card_list, player_final_score)
    if p_score == 0 or p_score == 21:
      print("Blackjack!!!")
      print("YOU WIN!!!")
      stop_dealing = True
    elif p_score < 21:
      print(" ")
      draw_again = input("Do you want to draw again? yes or no \n").lower()
      print(" ")
      if draw_again == "yes":
        print("======================")
        print(">>>>>>NEXT ROUND<<<<<<")
        print(" ")
        play_round()
        print(" ")
      else:
        if d_score > 21:
          print(" ")
          print("Dealer busts")
          print(" ")
          print("YOU WIN!!!")
          print(" ")
          stop_dealing = True
        else: 
          if p_score > d_score:
            print(" ")
            print("YOU WIN!!!")
            print(" ")
            stop_dealing = True
          elif p_score == d_score:
            print(" ")
            print("YOU TIE...")
            print(" ")
          else:
            if d_score < 21:
              print(" ")
              print("YOU LOSE!!")
              print(" ")
 
            elif d_score > 21:
              print(" ")
              print("You both bust..")
              print(" ")
              print("It's a LOSER TIE!!!")
              print(" ")
              
        print(f"Your score: {p_score}")
        print(f"Dealer score: {d_score}")
        stop_dealing = True
    else:
      print("BUST!!!!")
      print(" ")
      print(f"Sorry,{player_name}! You Lose!")
      stop_dealing = True
  print(" ")
  play_again = input("Do you want to play again? yes or no \n").lower()
  print(" ")
  if play_again == "yes":
    clear()
    game()
      
    
    


game()








