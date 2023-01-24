"""
Author: Raj Verma
Date: 24/01/2023
Desc: Snake Water Gun game with zero runtime error and no unexpected behaviour 
"""
import random


def winner(player, computer):
  '''Returns 0 for draw 1 for win -1 for lose'''
  winning_matrix = [
    [0, -1, 1],
    [1, 0, -1],
    [-1, 1, 0]
  ]
  return winning_matrix[computer][player]

score = []
swg = ['snake', 'water', 'gun']
states = ['Draw :! \n', 'You Win :) \n', 'You Lose :( \n']

while True:
  # for i in range(3-len(score)):
  while len(score) < 3:
    # handeles valueerror (if user press enter instead of any number)
    user = input("select one snake, water or gun [0/1/2]: ")
    comp = random.choice([0, 1, 2])

    # handels if user provide wrong input or no input
    if not user in ['0', '1', '2']: continue
    
    user = int(user)
    print(f"you selected {swg[user]} and computer selected {swg[comp]}")
    print(states[winner(user, comp)])
    score.append(winner(user, comp))
    print(len(score))
  
  if sum(score) > 0:
    print("You won the best of three :) Hope you enjoyed\n")
  elif sum(score) < 0:
    print("You lose the best of three :( Better luck next time\n")
  else:
    print("There is a draw between you and computer :!\nseems like you got the computer's vision\nor computer can read your mind \n")
  score = []
  prompt = input("press any key to continue or [0] to exit: ")
  if prompt == '0':break
  
