import random

rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''
paper = '''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            '''
scissors = '''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            '''
gameImage = [rock, paper, scissors]
print("Welcome to Rock - Paper - Scissors Game")
print("1. Rock\n2.Paper\n3.Scissors")
print("!-----------------------------------------!")
compChoice = random.randint(0, 2)
userChoice = int(input("Enter your choice\n: "))
if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You Choose: ")
    print(gameImage[userChoice])
    print("Computer Choose: ")
    print(gameImage[compChoice])
    if userChoice == 0 and compChoice == 2:
        print("Result: You win!")
    elif compChoice == 0 and userChoice == 2:
        print("Result: You lose")
    elif compChoice > userChoice:
        print("Result: You lose")
    elif userChoice > compChoice:
        print("Result: You win!")
    elif userChoice == compChoice:
        print("Result: It's a draw")
