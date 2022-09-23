########################################################################
##
## CS 101 Lab
## 005L
## Halena Aquino-Dunkin
## hjaym5@umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random


def play_again() -> bool:
    valid_input = False
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while valid_input == False:
        continueYN = input('Would you like to play again? Y/N: ')
        if continueYN == 'y' or continueYN == 'Y' or continueYN.lower() == 'yes' :
            valid_input = True
            end_game = False
            return False
        elif continueYN == 'n' or continueYN == 'N' or continueYN.lower() == 'no':
            valid_input = True
            end_game = True
            return True
        else:
            print('Must enter Y/YES/N/No to continue.')
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    chip_amount = int(input('How many chips would you like to wager?: '))
    while chip_amount <= 0 or chip_amount > bank:
        if chip_amount <= 0:
            print('Too low!')
        if chip_amount > bank:
            print('Not enough chips')
        chip_amount = int(input('How many chips would you like to wager?: '))
    return chip_amount            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    num1 = random.randint(1, 11)
    num2 = random.randint(1, 11)
    num3 = random.randint(1, 11)
    return num1, num2, num3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb and reelb == reelc and reela == reelc):
        return 3
    elif (reela == reelb and reela != reelc) or (reelb == reelc and reelb != reela) or (reela == reelc and reela != reelb):
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    play_chips = int(input('How many chips would you like to play with?: '))
    while (play_chips < 0 or play_chips > 100):
        print('Too low a value, you can only choose 1 - 100 chips')
        play_chips = int(input('How many chips would you like to play with?: '))

    return play_chips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if (matches == 3):
        return wager * 10
    elif (matches == 2):
        return wager * 3
    else:
        return wager * -1


if __name__ == "__main__":

    playing = True
    banklist = []
    while playing:

        bank = get_bank()
        original_amount = bank
        spin_count = 0
        banklist.append(original_amount)

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            banklist.append(bank)
            print("Current bank", bank)
            print()

            spin_count += 1
           
        print("You lost all", original_amount, "in", spin_count, "spins")
        print("The most chips you had was", max(banklist))
        end_game = play_again()
        if (end_game == True):
            playing = False
        else:
            playing = True
            
        print()
