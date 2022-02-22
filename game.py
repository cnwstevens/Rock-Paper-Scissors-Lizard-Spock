import random
import time

#Introduce game and give instructions
def intro_instruct():
  print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
  print("""
    How to Play:
    Rock crushes Scissors.
    Scissors cuts Paper.
    Paper covers Rock.
    Rock crushes Lizard.
    Lizard poisons Spock.
    Spock smashes Scissors.
    Scissors cuts Lizard.
    Lizard eats Paper.
    Paper disproves Spock.
    Spock vaporizes Rock.
    """)

def game():
  #instead of writing names, use numbers as variables and create a dictionary of options
  #0 = rock
  #1 = paper
  #2 = scissors
  #3 = lizard
  #4 = Spock
  game_dict = {0:'rock', 1:'paper', 2:'scissors', 3:'lizard', 4:'spock'}

  #create a win/lost matrix for the game
  #-1 = tie, other numbers are the number/name correspondence from the dictionary

  win_lose = [[-1, 1, 0, 0, 4], [1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]

  #take user input (words) and convert to number for computer to work with
  choice = input("Enter your move:")

  if (choice.lower() == 'rock'):
    player_move = 0
  elif (choice.lower() == 'paper'):
    player_move = 1
  elif (choice.lower() == 'scissors'):
    player_move = 2
  elif (choice.lower() == 'lizard'):
    player_move = 3
  elif (choice.lower() == 'spock'):
    player_move = 4
  else:
    print("Invalid response. Please try again.")
    return
    

  computer_choice = random.randint(0,4)
  #print computer choice as words, not number
  print("Computer chooses " + game_dict[computer_choice])


  winner = win_lose[player_move][computer_choice]

  if winner == player_move:
    print("You win!")
    time.sleep(2)
  elif winner == computer_choice:
    print("Sorry, you lose!")
    time.sleep(2)
  else:
    print("Tie!")
    time.sleep(2)

if __name__ == '__main__':
  while True:
    intro_instruct()
    time.sleep(2)
    game()
 