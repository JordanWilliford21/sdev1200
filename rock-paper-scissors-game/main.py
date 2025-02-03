#
# Name
# Date
# Rock, Paper, Scissors Game Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
#This will allow the computer to choose 1 - 3 randomly but not show the user what it chose
def computerChoice():
    import random
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        return 'rock'
    elif randomNumber==2:
        return'paper'
    else:
        return'scissors'

#Now this wil check if the choice was valid
def validChoice(choice):
    return choice=='rock' and choice!='paper' and choice != 'scissors'

#Check for invalid choice
def invalidChoice(choice):
    while choice !='rock' and choice !='paper' and choice != 'scissors':
        print('That is not a valid choice!')
        choice=input('Enter rock paper or scissors:')
        return choice

# This will check and see who won
def winner(player,computer):
    if player =='rock' and computer =='scissors':
        print("rock smashes scissors")
        return True
    elif player == 'scissors' and computer =='paper':
        print("scissors cuts paper")
        return True
    elif player =='paper' and computer == 'rock':
        print ("paper wraps rock")
        return True
    
    else:
        return False
compChoice=computerChoice()
playerChoice = input('Choose from rock, paper or scissors:')
#now we check if the player choice was valid
if not validChoice(playerChoice):
    playerChoice = invalidChoice(playerChoice)

while playerChoice == compChoice:
    print('Computers choice:',compChoice)
    print('Its a tie! Choose again!')
    compChoice = computerChoice()
    playerChoice= input ('Enter rock paper or scissors')
    if not validChoice(playerChoice):
        playerChoice = invalidChoice(playerChoice)
#This will display the winning results
print('Computers Choice:', compChoice)

if winner(playerChoice, compChoice):

   print('Congratulations! You win!')

else:

   print('You lose! Computer wins!')