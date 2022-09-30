########################################################################
##
## CS 101 Lab
## 005L
## Halena Aquino-Dunkin
## hjaym5@umkc.edu
##
########################################################################


# import statements
import string

# functions
def get_school(libr_card):
    # Determines if the user enters a valid school, returns Invalid if they didn't 
    if libr_card[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif libr_card[5] == '2':
        return 'School of Law'
    elif libr_card[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'

def get_grade(libr_card):
    # Determines if the user enters a valid grade level, returns Invalid if they didn't
    if libr_card[6] == '1':
        return 'Freshmen'
    elif libr_card[6] == '2':
        return 'Sophmore'
    elif libr_card[6] == '3':
        return 'Junior'
    elif libr_card[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'

def character_value(character):
    # Determines if the character is a letter or a number
    # If it's a letter, it finds the proper value, if it's a number, sets the value to the number
    if character.isalpha() == True:
        return string.ascii_uppercase.index(character)
    elif character.isdigit() == True:
        return int(character)

def get_check_digit(libr_card):
    num = 0
    # Cycles through all of the characters on the card and finds the digit value
    for i in range(0, len(libr_card)-1):
        num = (i + 1) * (character_value(libr_card[i])) + num

    num = num % 10
    return num

def verify_check_digit(libr_card):
    # Makes sure that all of the information entered is valid
    # Tells the user the error and it's location if some of the information is invalid
    if len(libr_card) != 10:
        return False, 'The length of the number given must be 10'
    for i in range(0, 5):
        if libr_card[i].isalpha() == False:
            return False, 'The first 5 characters must be A-Z, the invalid character is at ' + str(i) + ' is ' + str(libr_card[i])
    for i in range(7, 10):
        if libr_card[i].isdigit() == False:
            return False, 'The last 3 characters must be 0-9, the invalid character is at ' + str(i) + ' is ' + str(libr_card[i])
    if libr_card[5] != '1' and libr_card[5] != '2' and libr_card[5] != '3':
        return False, 'The sixth character must be 1 2 or 3'
    elif libr_card[6] != '1' and libr_card[6] != '2' and libr_card[6] != '3' and libr_card[6] != '4':
        return False, 'The seventh character must be 1 2 3 or 4'
    elif int(libr_card[9]) != get_check_digit(libr_card):
        return False, 'Check digit ' + str(libr_card[9]) + ' does not match calculated value ' + str(get_check_digit(libr_card))
    else:
        return True, ''

# main program
    print("Main Program")
if __name__ == "__main__":
    
    running = True
    while running == True:
        # Prints out the results for all of the functions (I used this to make sure the functions were working properly
        user_string = input('Enter library card number: ')

        # Determines is the user entered a valid school.
        # If they didn't, prompt them to try again and restarts the program from the beginning
        if get_school(user_string) == 'Invalid School':
            print('That is not a valid school. Please try again.')
            print()
            continue
        else:
            print(f'School: {get_school(user_string)}')

        # Determines is the user entered a valid grade.
        # If they didn't, prompt them to try again and restarts the program from the beginning
        if get_grade(user_string) == 'Invalid Grade':
            print('That is not a valid grade. Please try again.')
            print()
            continue
        else:
            print(f'Grade: {get_grade(user_string)}')
        
        print(f'Digit: {get_check_digit(user_string)}')
        
        valid, reason = verify_check_digit(user_string)

        # Determines is the digit the user entered matches the calculated digit.
        # If they didn't, prompt them to try again and restarts the program from the beginning
        if valid == False:
            print(f'Error: {reason}. Please try again.')
            print()
            continue
    
        print('Information correct!')
        print()
        break
    

