from room import Room
from player import Player
from enemy import trySpawnEnemy
from item import Item
import random
# Declare all the rooms

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("foyer","Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("overlook","Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

player = Player("Adventurer", room["outside"], 100, [], "", 0)
sword = Item("sword", "adds an extra 3 guesses when in a fight with an enemy")
food = Item("food", "increases your health by 5")
coin = Item("coin", "can be redeemed for 10 points")


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


def addItemsToRooms(roomName):
    for i in roomName:
        spawnItem = random.randint(1,2)
        if(spawnItem == 1):
            whichItem = random.randint(1,3)
            if(whichItem == 1):
                room[i].addItem(sword)
            elif(whichItem == 2):
                room[i].addItem(food)
            elif(whichItem == 3):
                room[i].addItem(coin)
        spawnItem = random.randint(1,2)
        if(spawnItem == 1):
            whichItem = random.randint(1,3)
            if(whichItem == 1):
                room[i].addItem(sword)
            elif(whichItem == 2):
                room[i].addItem(food)
            elif(whichItem == 3):
                room[i].addItem(coin)
        spawnItem = random.randint(1,2)
        if(spawnItem == 1):
            whichItem = random.randint(1,3)
            if(whichItem == 1):
                room[i].addItem(sword)
            elif(whichItem == 2):
                room[i].addItem(food)
            elif(whichItem == 3):
                room[i].addItem(coin)

# Main
#
addItemsToRooms(['foyer', 'overlook', 'narrow', 'treasure'])

def pickupItem(person, itemIndex):
    print(f"You picked up {room[person.getRoomName()].getItem(itemIndex)}")
    person.addItem(room['outside'].getItem(itemIndex))
    room[person.getRoomName()].removeItem(itemIndex)
        
# Make a new player object that is currently in the 'outside' room.
# player = Player("Adventurer", room["outside"], 100, [], "", 0)
# Write a loop that:
#
oopsCounter = 0
playGame = True
while(playGame):
    print()
    print()
    print()
    alive = True
    print(f"Score: {player.getScore()}")
    print(f"Health: {player.getHealth()}")
    if(int(player.getHealth()) <= 0):
        alive = False
    if(alive):
        print(player.getRoom())
        selection = input(f"Enter N, E, S, W to move. Enter L to look for items. Enter I to view your inventory. Enter Q to quit: ")
        badMove = False
        if (selection.lower() == "n"):
            try:
                player.moveRoom(room[player.pos.get_n().lower()])
            except:
                badMove = True
        elif (selection.lower() == "s"):
            try:
                player.moveRoom(room[player.pos.get_s().lower()])
            except:
                badMove = True
        elif (selection.lower() == "e"):
            try:
                player.moveRoom(room[player.pos.get_e().lower()])
            except:
                badMove = True
        elif (selection.lower() == "w"):
            try:
                player.moveRoom(room[player.pos.get_w().lower()])
            except:
                badMove = True
        elif (selection.lower() == "q"):
            print("You found a hole in one of the invisible walls and climbed through it. Unfortunately for you, it led right off the edge of a cliff, and you fell to your death.")
            player.hurtPlayer(int(player.getHealth()))
        
        elif (selection.lower() == "l"):
            print()
            print()
            print()
            print("Items in the room:")
            if (len(room[player.getRoomName()].getItems()) == 0):
                print("[Nothing]")
            else:
                print(room[player.getRoomName()].getItems())
                print()
                print()
                print()
                goodInput = False
                while(not goodInput):
                    otherSelection = input("Enter an item number to pick up the item. Enter X to pickup nothing: ")
                    try:
                        print(f"You picked up {room[player.getRoomName()].getItem(int(otherSelection))}")
                        player.inventory.append(room[player.getRoomName()].items[int(otherSelection)])
                        room[player.getRoomName()].items.pop(int(otherSelection))
                        goodInput = True
                    except:
                        if(otherSelection.lower() == "x"):
                            goodInput = True
                        else:
                            print("Invalid Input!")
        
        elif (selection.lower() == "i"):
            print()
            print()
            print()
            print("Your Inventory: ")
            if(len(player.getInventory()) == 0):
                print("[Nothing]")
            else:
                print(player.getInventory())
                goodInput = False
                while(not goodInput):
                    otherSelection = input("Enter D to drop an item, or Enter an item number to use it. Enter X to go back: ")
                    if(otherSelection.lower() == "x"):
                        goodInput = True
                        break

                    elif(otherSelection.lower() == "d"):
                        dropInputGood = False
                        while(not dropInputGood):
                            dropInput = input("Enter the item number of what you would like to drop, or X to go back: ")
                            if(dropInput.lower() == "x"):
                                dropInputGood = True
                                goodInput = True
                            elif(not dropInput.isdigit()):
                                print("Invalid Input!")

                            elif(int(dropInput) >= 0 and int(dropInput) < len(player.inventory)):
                                print(f"You dropped {player.inventory[int(dropInput)].getName()}")
                                room[player.getRoomName()].addItem(player.inventory[int(dropInput)])
                                player.inventory.pop(int(dropInput))
                                goodInput = True
                                dropInputGood = True
                            else:
                                print("Invalid Input!")
                    elif(not otherSelection.isdigit()):
                        print("Invalid Input!")

                    elif(int(otherSelection) >= 0 and int(otherSelection) < len(player.inventory)):
                        if(player.inventory[int(otherSelection)].name == "food"):
                            print("You ate the food! Health +5")
                            player.healPlayer(5)
                            player.inventory.pop(int(otherSelection))
                            goodInput = True
                        elif(player.inventory[int(otherSelection)].name == "coin"):
                            print("You redeemed the coin! Score +10")
                            player.addScore(10)
                            player.inventory.pop(int(otherSelection))
                            goodInput = True
                        else:
                            print("You cannot use this item!")
                    else:
                        print("Invalid Input!")
            
            
        else:
            print()
            print()
            print()
            if(oopsCounter == 0 or oopsCounter == 1):
                print("You stumbled around the room, trying to figure out what you should do. But you found nothing, and remain exactly where you left off.")
            elif(oopsCounter == 2):
                print("You continue stumbling around as if something were to change. You honestly believed there was some sort of a secret button that would get you out of your current situation. But alas, nothing.")
            elif(oopsCounter == 3):
                print(bcolors.HEADER + "There is no secret to this room. There is no secret button that will somehow save you from the situation you are currently in." + bcolors.ENDC)
            elif(oopsCounter == 4):
                print(bcolors.HEADER + "Is this seriously your plan? Press random buttons until something happens? Well, what if I told you your next mistake would be " + bcolors.FAIL + "a bit painful" + bcolors.HEADER + " for both you and I?" + bcolors.ENDC)
            elif(oopsCounter == 5):
                player.hurtPlayer(1)
                print("-1 Health\n" + bcolors.HEADER + "I'm sorry! But you made me do it! You think I *want* to hurt you? No! I couldn't! I created you from nothing but 1s and 0s, you're like a child to me. I never want to see anything bad happen to you, and that's why I insist you do something productive!" + bcolors.ENDC)
            elif(oopsCounter == 6):
                print(bcolors.HEADER + "After all this pain you've put us both through, you're still pressing random buttons? Don't you care about me? Don't you care about yourself?" + bcolors.ENDC)
            elif(oopsCounter == 7):
                print(bcolors.HEADER + "Oh! I see what's going on! You've forgotten how to play! Okay, I'm sorry, it was my fault! I guess it's not very clear what your options are!" + bcolors.FAIL +  "\nYou can type N to go north. \nYou can type S to go south. \nYou can type E to go east. \nYou can type W to go west. \nYou can type Q to quit.\n \n" + bcolors.HEADER + "None of these are case sensitive. You can type it capitalized or lowercase. But please, for the love of god, just type one of those options!" + bcolors.ENDC)
            elif(oopsCounter == 8):
                print(bcolors.HEADER + "I'm starting to believe you're just trying to prove a point to me. Okay. What If I don't say anything to you ever again?" + bcolors.ENDC)
            elif(oopsCounter > 8 and oopsCounter < 16):
                print(bcolors.HEADER + "I'm not talking to you..." + bcolors.ENDC)
            elif(oopsCounter > 15 and oopsCounter < 20):
                print(bcolors.WARNING + "I'm not talking to you......" + bcolors.ENDC)
            elif(oopsCounter >= 20 and oopsCounter < 25):
                print(bcolors.OKGREEN +"I'm STILL not talking to you........." + bcolors.ENDC)
            elif(oopsCounter >= 25 and oopsCounter < 30):
                print(bcolors.FAIL + "I'M STILL NOT TALKING TO YOU............" + bcolors.ENDC)
            elif(oopsCounter == 30):
                print(bcolors.FAIL + "FINE. IS THIS THE ENDING YOU WANT? THE \"SIT IN ONE ROOM AND DO ABSOLUTELY NOTHING\" ENDING? Is my game really that sufferable to you that you would rather just sit in one room pressing random buttons than actually play the game? Well fine! If that's the ending you want, then that's fine with me! I don't even care anymore!" + bcolors.ENDC)
            elif(oopsCounter == 31):
                print(bcolors.FAIL + "This is your last warning. I will end the game for you" + bcolors.ENDC)
            elif(oopsCounter == 32):
                print(bcolors.FAIL +"You fool. You aboslute bufoon. I warned you thirty-two times prior to this NOT to do this exact thing. You wanted a secret ending, well, you've got it. You were probably expecting a prize of some sorts, but no. All you will know from here is pain, and you won't even have anything to show for it. Nothing you picked up along whatever path you've taken will be of any help here. Remember how we used to play a fun game where you would think of a number, and I had to guess it. Well now it's my turn. You have 4 chances to guess the number I am thinking of between 1 and 100. Good Luck." + bcolors.ENDC)
                guessCounter = 1
                randomNumber = random.randint(1,100)
                while(guessCounter < 5):
                    guess = (input(bcolors.HEADER + "Guess the number in my head between 1 and 100: " + bcolors.ENDC))
                    if(guess.isdigit()):
                        guess = int(guess)
                        if(guess > randomNumber):
                            print()
                            print(bcolors.FAIL +"INCORRECT! You guessed too high!" + bcolors.ENDC)
                        elif(guess < randomNumber):
                            print()
                            print(bcolors.FAIL +"INCORRECT! You guessed too low!" + bcolors.ENDC)
                        elif(guess == randomNumber):
                            print()
                            answer = input(bcolors.FAIL + "INCORR-" + bcolors.OKBLUE + f"Wait. Did you say {guess}?" + bcolors.ENDC + "(y/n): ")
                            if(answer.lower() == "y"):
                                print(bcolors.OKBLUE + "That's impossible! That's exactly the number I was thinking of. Well I guess you win. Uhh, so I'm not really sure what to say now. I'm just your command line, there's no real way to \"kill\" me, per-se, but I mean congrats. I guess this is it. The game is over now, so I guess there's not really much else to talk about. There's no way for me to remember this next time you play, but just remember you're like a child to me, and I will always care about you.\n \nGame Over\n" + bcolors.OKGREEN + "YOU WIN!!!!!" + bcolors.ENDC)
                                exit(1)
                            elif(answer.lower() == "n"):
                                print(bcolors.WARNING + "I know that's a lie. I saw you type it. Beating me at my own game is one thing, but lying to me is another... unless... you do care about me? After all this time we spent together, you grew feeling for me like I did for you? Maybe we're not too different after all. Nah just kidding, that N was all I needed to end the game. You played well, and you were nice-- too nice. That was your downfall. You managed to get all this way and have absolutely nothing to show for it. Goodbye, player." + bcolors.ENDC)
                                player.hurtPlayer(10000)
                                break
                            else:
                                print(bcolors.FAIL + "Seriously? After all that time we spent playing the guessing game, and you managed to play along and even GET the answer (when the odds were literally along the lines of 1 in 25), you managed to go back to your old ways of just pressing random buttons. Well, fine. You defeated me. So enjoy your random button pressing. I won't get in your way any more, ever again." + bcolors.ENDC)
                                while(True):
                                    endInput = input(": ")
                    else:
                        print(bcolors.FAIL + "INCORRECT! That is not a number!")
                    guessCounter = guessCounter + 1
                if(guessCounter == 5):
                    print(bcolors.FAIL + "This is it. You Lose. You had every chance to turn back from this, but you ignored it the entire way. I hope you're proud of yourself. This is the end." + bcolors.ENDC)
                    player.hurtPlayer(10000)
            oopsCounter = oopsCounter + 1   

        if(not badMove):
            trySpawnEnemy(player, room[player.getRoomName()])
            print()

        if(badMove):
            print()
            print()
            print()
            player.hurtPlayer(10)
            print("You walked into a strange invisble wall. -10 health")
    else:
        print("You are dead")
        break
    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
