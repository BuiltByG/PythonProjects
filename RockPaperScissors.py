# Define Computer Play - Select a random number between 0 and 2

import random
computerplay = random.randint(0, 2)
print(computerplay)

# Prompt the user to enter their play:
play = int(input('Enter 0 for Rock, 1 for paper or 2 for scissors: '))

# Define plays:
rock = 0
paper = 1
scissors =  2

def variablename (var):
    if var == 0:
        return 'Rock'
    elif var == 1:
        return 'Paper'
    elif var == 2:
        return 'Scissors'


# Define rules for winning

if play <=2 and play >= 0:
    if play == computerplay: # Draw
        print('The computer is', variablename(computerplay), '. You are ', variablename(play), ' too. It is a draw.')
    elif play > computerplay and play - computerplay > 1: # Player Scissors, Computer Rock
        print('The computer is', variablename(computerplay), '. You are ', variablename(play),  '. The computer wins.')
    elif play > computerplay and play - computerplay == 1: # Player Paper, Computer Rock
        print('The computer is', variablename(computerplay), '. You are ', variablename(play), '. You win!')
    elif play < computerplay and computerplay - play ==  1: # Player Paper or Rock, Computer Scissors or Paper
        print('The computer is', variablename(computerplay), '. You are ', variablename(play), '. The computer wins!')
    elif play < computerplay and computerplay - play > 1: # Player Rock, Computer Scissors
        print('The computer is', variablename(computerplay), '. You are ', variablename(play), '. You win!')


        
else:
    print('Error, invalid  input option.')
