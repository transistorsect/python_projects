# Andrew Birmingham - 6/30/24 - ITSE 1402 - created so you can't fudge the rolls with your friends

import random
import time

print('''
██████╗ ██████╗  ██████╗     ██████╗ ██╗ ██████╗███████╗    ██████╗  ██████╗ ██╗     ██╗     ███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝     ██╔══██╗██║██╔════╝██╔════╝    ██╔══██╗██╔═══██╗██║     ██║     ██╔════╝██╔══██╗
██████╔╝██████╔╝██║  ███╗    ██║  ██║██║██║     █████╗      ██████╔╝██║   ██║██║     ██║     █████╗  ██████╔╝
██╔══██╗██╔═══╝ ██║   ██║    ██║  ██║██║██║     ██╔══╝      ██╔══██╗██║   ██║██║     ██║     ██╔══╝  ██╔══██╗
██║  ██║██║     ╚██████╔╝    ██████╔╝██║╚██████╗███████╗    ██║  ██║╚██████╔╝███████╗███████╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝      ╚═════╝     ╚═════╝ ╚═╝ ╚═════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝''') # https://patorjk.com/software/taag/ used this resource to generate the header

secret_art = r"""
                              _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      )\
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
                             )(  l\ o ('..-.
                       _..--' _'-' '--'.-. |
                __,,-'' _,,-''            \ \
               f'. _,,-'                   \ \
              ()--  |                       \ \
                \.  |                       /  \
                  \ \                      |._  |
                   \ \                     |  ()|
                    \ \                     \  /
                     ) `-.                   | |
                    // .__)                  | |
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  \
                                             |lllj
                                             |||||
You have been slain by a skeleton! Choose again...""" # https://www.asciiart.eu/mythology/skeletons  artist is -nabis

time.sleep(1)
print('\nWell met adventurer. Welcome to the RPG Dice Roller.')
time.sleep(1)

            
def roll_dice(dice_type, rolls): #the function generates a list of values based on the user selection of the dice and amount to be rolled; it will display each value and a sum of the value; special rules under certain scenarios apply
    print(f"\nRolling {rolls} d{dice_type}. Good luck!")
    results = [random.randint(1, dice_type) for _ in range(rolls)]
    
    if dice_type == 100:  #percentile dice are only rolled once
        print(f"--- {results[0]} ---")
    elif dice_type == 20 and rolls == 2:  # common rule in tabletop rpg is if you have advantage you take the highest number; if disadvantage you take the lowest number
        print(f"--- {max(results)} (rolled with advantage) ---")
        print(f"--- {min(results)} (rolled with disadvantage) ---")
    print(results)
    print(f"\nTotal: {sum(results)}")
        
    print()


    
dice_types = [4, 6, 8, 10, 12, 20, 100]
readme_option = len(dice_types) +1
exit_option = len(dice_types) +2
secret = len(dice_types) +3

while True:
    print("\nOptions:\n")
    for i, dice_type in enumerate(dice_types, start=1):
        print(f"{i}. d{dice_type}")
        
    print(f"{readme_option}. Read Me")
    print(f"{exit_option}. Exit")

    try:
        choice = int(input("\nMake a selection: "))
    except ValueError:
        print("\nInvalid selection. Please choose again.")
        continue
                
    if choice == exit_option:
            print("\nFare thee well adventurer!")
            break
        
    elif choice == readme_option:
            print("\nA d100 can only roll one dice at a time. If you roll 2 d20 dice, the rolls will be display advantage/disadvantage. What ever you do, don't enter 10 when making a selection.")
            continue
        
    elif choice == secret:
        print(secret_art)
        time.sleep(2)
        continue

    elif choice > 10:
            print("\nInvalid selection. Choose again.")
            continue

    dice_type = dice_types[choice - 1]

    if dice_type == 100:
            rolls = 1
    else:
        try:
            rolls = int(input("How many dice do you need to roll? "))
        except ValueError:
            print("\nInvalid selection. Try again.")
            continue

    roll_dice(dice_type, rolls)

