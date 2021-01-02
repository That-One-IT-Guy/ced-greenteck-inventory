import time
import json
from colorama import init, Fore, Back, Style
init(convert=True)
print("Welcome user! Please wait...")
print("Server is not set up on this version, skipping")
print(Fore.GREEN + 'Contact a admin if not green')
print(Fore.WHITE)
while True:
    database = "inv.json"
    data = json.loads(open(database).read())
    print("What can I find for you?" + Fore.BLACK + Back.WHITE)
    item = input()
    print(Fore.WHITE + Back.BLACK + "")
    item = item.lower()
    if item == "admin":
        while True:
            admin = input("(R)ead, (W)rite, (U)pdate or (Q)uit admin?")
            if admin == "W" or admin == "w":
                print("Writing mode!")
                nname = input("Product code on printout: ")
                nname = nname.lower()
                nabv = input("Item description on printout: ")
                nabv = nabv.lower()
                nloc = input("Where can it be found: ")
                itemdat = {nname: nloc,
                nabv: nloc
                }
                with open('inv.json') as json_file:
                    data = json.load(json_file)
                    data.update(itemdat)
                with open('inv.json', 'w') as json_file:
                    json.dump(data, json_file)
            elif admin == "R" or admin == "r":
                with open('inv.json') as json_file:
                    data = json.load(json_file)
                    print(data)
            elif admin == "U" or admin == "u":
                print("Update mode unavalible.")
            else:
                break
    elif item == "help":
        print("Help information:")
        print("This program is to help find objects, object names are not case sensitive")
        print("Products can be found with its product code or description on the printout.")
        print()
        print("The top of your page should look a little like this:")
        print()
        print("-------------------------------------------------------------------------------")
        print("| ### ########                             Page(#) of ###           ##########|")
        print("| ### ########                           ####################    ------------ |")
        print("| ###############                        ########  | ##/##/##    |####      | |")
        print("| Tel: ### ###-####                      |   ###########    |    |### ### ##| |")
        print("| Fax: ### ###-####                      |                  |    ------------ |")
        print("|                                        --------------------    |########  | |")
        print("| Sold to:#####                                                  |          | |")
        print("|         ##########                                             ------------ |")
        print("|         ######         Ship to:  #########                     |### |#### | |")
        print("|         ######                   ############                  |    |     | |")
        print("|                                  ##########                    ------------ |")
        print("|                                  ###########                                |")
        print("|                      ***INV WILL BE SENT & MAILED ***                       |")
        print("| ----------------------------------------------------------     ------------ |")
        print("| |ACCOUNT NO.      | JOB NAME AND ADDRESS | ##### | ####  |     |###|####|#| |")
        print("| |  ##########     | #########            |  #####|  #### |     |###| ## | | |")
        print("| ------------------+---------------------------------------     ------------ |")
        print("| |##########       | ##########   |######|##|## |## |#### |     |#  | ## |#| |")
        print("| |### ##           |    ####      |######|  |   |   |     |     | # | #  | | |")
        print("| ----------------------------------------------------------     ------------ |")
        print("| |QUANTINTITY |                 |                |        |     |          | |")
        print("| |ORDERD      |" + Fore.RED +"PRODUCT CODE     " + Fore.WHITE + "|" + Fore.RED + "DESCRIPTION     " + Fore.WHITE + "|# # # ##|     |##  # ####| |")
        print("| ----------------------------------------------------------     ------------ |")
        print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
        print()
        print("Check the program admin for adding items or errors")
    else:
        with open('inv.json') as json_file:
            data = json.load(json_file)
            try:
                loc = (data[item])
                print("That should be at " + Fore.GREEN + loc + Fore.WHITE + " .")
            except:
                print(Back.RED + Fore.BLACK + "Uhhh this is emabarising I cant find that!" + Back.BLACK + Fore.WHITE)
