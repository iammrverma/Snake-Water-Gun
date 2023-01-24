"""
Author: Raj Verma
Date: 24/01/2023
Desc: Snake Water Gun game with zero runtime error and no unexpected behaviour 
"""
import random
swg = ['snake', 'water', 'gun']
states = ['Draw :! \n', 'You Win :) \n', 'You Lose :( \n']

def winner(player, computer):
  '''Returns 0 for draw 1 for win -1 for lose'''
  winning_matrix = [
    [0, -1, 1],
    [1, 0, -1],
    [-1, 1, 0]
  ]
  return winning_matrix[computer][player]

def handle_input():
    """Handles input validation and returns the choice of user"""
    while True:
        user = input("select one snake, water or gun [0/1/2]: ")
        if user in ['0', '1', '2']:
            return int(user)
        print("Invalid Input, please enter a valid choice.")

def play_game():
    """Plays one round of the game and returns the result (0 for draw, 1 for win, -1 for lose)"""
    user = handle_input()
    comp = random.choice([0, 1, 2])
    print(f"you selected {swg[user]} and computer selected {swg[comp]}")
    result = winner(user, comp)
    print(states[result])
    return result

def display_result(score):
    """Displays the result of the game based on the score"""
    if score > 0:
        print("You won the best of three :) Hope you enjoyed\n")
    elif score < 0:
        print("You lose the best of three :( Better luck next time\n")
    else:
        print("There is a draw between you and computer :!\nseems like you got the computer's vision\nor computer can read your mind \n")

def main():
    """Main function of the game"""
    score = 0

    # Play the game for 3 rounds
    for i in range(3):
        score += play_game()

    # Display the final result
    display_result(score)


if __name__ == '__main__':
    while True:
      main()
      
      prompt = input("Press any key to continue or [0] to exit: ")
      if prompt == '0': break
