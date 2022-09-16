running = True # Variable that controls the entire game running
validYN = False # Determines if the user entered a valid Y/N answer

# Introduction
print('Welcome to the Flarsheim Guesser!')
print()

# The loop that keeps the game running until the user says otherwise
while (running == True):
    print('Please think of a number between and including 1 and 100.')
    print()
    
    # Determines if the remainder the user entered is a valid number and repeats
    # the question until the answer is valid
    div3Invalid = True
    while (div3Invalid == True):
        # Asks the user the remainder
        div3 = int(input('What is the remainder when your number is divided by 3 ? '))
        if (div3 < 0):
            print('The value entered must be 0 or greater')
        elif (div3 >= 3):
            print('The value entered must be less than 3')
        else:
            div3Invalid = False
    print()

    # Determines if the remainder the user entered is a valid number and repeats
    # the question until the answer is valid
    div5invalid = True
    while (div5invalid == True):
        # Asks the user the remainder
        div5 = int(input('What is the remainder when your number is divided by 5 ? '))
        if (div5 < 0):
            print('The value entered must be 0 or greater')
        elif (div5 >= 5):
            print('The value entered must be less than 5')
        else:
            div5invalid = False
    print()

    # Determines if the remainder the user entered is a valid number and repeats
    # the question until the answer is valid
    div7invalid = True
    while (div7invalid == True):
        # Asks the user the remainder
        div7 = int(input('What is the remainder when your number is divided by 7 ? '))
        if (div7 < 0):
            print('The value entered must be 0 or greater')
        elif (div7 >= 7):
                print('The value entered must be less than 7')
        else:
            div7invalid = False
    print()

    # Cycles through number from 1 to 100 to determine the user's number
    for i in range(1, 100):
        if(i % 3 == div3 and i % 5 == div5 and i % 7 == div7):
            print(f'Your number was {i}\nHow amazing is that?')
            print()

            # Asks the user if they want to play again
            while(validYN == False):
                continueYN = input('Do you want to play again? Y to continue, N to quit ==> ')
                if (continueYN == 'Y' or continueYN == 'y'):
                    print()
                    break
                elif (continueYN == 'N' or continueYN == 'n'):
                    # Thanks the user for playing
                    print('Thank you for playing!')
                    running = False # ends loop 
                    break
