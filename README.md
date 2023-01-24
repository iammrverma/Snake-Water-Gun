# Snake-Water-Gun
Command line Snake Water Gun game with zero runtime Error

# Description
This is a simple Python script that simulates the Snake Water Gun game. The game is a simple, text-based game that allows the user to play against the computer. The user is prompted to select one of three options: 'snake', 'water', or 'gun', represented by the numbers 0, 1, and 2 respectively. The computer then randomly selects one of the three options. The winner of the round is determined by a predefined winning matrix, with the user winning if their choice beats the computer's, losing if it loses to the computer's, and drawing if the choices are the same. The game keeps track of the score throughout the rounds, and once 3 rounds have been played, the game will print out the result of the game, whether the user won, lost, or drew.
The game will continue to play until the user decides to exit by inputting '0' when prompted.

# Eficiency 
The efficiency of code refers to how well the code performs in terms of its use of resources, such as time and memory. In this case, the code is relatively efficient. It uses a simple while loop to play the game in rounds until the user chooses to exit. It also uses a simple function to determine the winner of each round based on a pre-defined winning matrix, which eliminates the need for complex logic. Additionally, it uses the built-in random.choice() function to randomly select the computer's choice, which is a more efficient method than implementing a random number generator.
It also checks if user has entered the correct input or not.
