from room import Room
from player import Player
import random
# Declare all the rooms

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("foyer","Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("overlook","Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Adventurer", room["outside"], 100, [], "")
# Write a loop that:
#
oopsCounter = 0
playGame = True
while(playGame):
    print()
    print()
    print()
    alive = True
    print(f"Health: {player.getHealth()}")
    if(int(player.getHealth()) <= 0):
        alive = False
    if(alive):
        print(player.getRoom())
        selection = input(f"Enter N, E, S, W to move. Enter Q to quit: ")
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
        else:
            print()
            print()
            print()
            if(oopsCounter == 0 or oopsCounter == 1):
                print("You stumbled around the room, trying to figure out what you should do. But you found nothing, and remain exactly where you left off.")
            elif(oopsCounter == 2):
                print("You continue stumbling around as if something were to change. You honestly believed there was some sort of a secret button that would get you out of your current situation. But alas, nothing.")
            elif(oopsCounter == 3):
                print("There is no secret to this room. There is no secret button that will somehow save you from the situation you are currently in.")
            elif(oopsCounter == 4):
                print("Is this seriously your plan? Press random buttons until something happens? Well, what if I told you your next mistake would be a bit painful for both you and me?")
            elif(oopsCounter == 5):
                player.hurtPlayer(1)
                print("I'm sorry! But you made me do it! You think I *want* to hurt you? No! I couldn't! I created you from nothing but 1s and 0s, you're like a child to me. I never want to see anything bad happen to you, and that's why I insist you do something productive!")
            elif(oopsCounter == 6):
                print("After all this pain you've put us both through, you're still pressing random buttons? Don't you care about me? Don't you care about yourself?")
            elif(oopsCounter == 7):
                print("Oh! I see what's going on! You've forgotten how to play! Okay, I'm sorry, it was my fault! I guess it's not very clear what your options are! \nYou can type N to go north. \nYou can type S to go south. \nYou can type E to go east. \nYou can type W to go west. \nYou can type Q to quit.\n \n None of these are case sensitive. You can type it capitalized or lowercase. But please, for the love of god, just type one of those options!")
            elif(oopsCounter == 8):
                print("I'm starting to believe you're just trying to prove a point to me. Okay. What If I don't say anything to you ever again?")
            elif(oopsCounter > 8 and oopsCounter < 16):
                print("I'm not talking to you...")
            elif(oopsCounter > 15 and oopsCounter < 20):
                print("I'm not talking to you......")
            elif(oopsCounter >= 20 and oopsCounter < 25):
                print("I'm STILL not talking to you.........")
            elif(oopsCounter >= 25 and oopsCounter < 30):
                print("I'M STILL NOT TALKING TO YOU............")
            elif(oopsCounter == 30):
                print("FINE. IS THIS THE ENDING YOU WANT? THE \"SIT IN ONE ROOM AND DO ABSOLUTELY NOTHING\" ENDING? Is my game really that sufferable to you that you would rather just sit in one room pressing random buttons than actually play the game? Well fine! If that's the ending you want, then that's fine with me! I don't even care anymore!")
            elif(oopsCounter == 31):
                print("This is your last warning. I will end the game for you")
            elif(oopsCounter == 32):
                print("You fool. You aboslute bufoon. I warned you thirty-two times prior to this NOT to do this exact thing. You wanted a secret ending, well, you've got it. You were probably expecting a prize of some sorts, but no. All you will know from here is pain, and you won't even have anything to show for it. Nothing you picked up along whatever path you've taken will be of any help here. Remember how we used to play a fun game where you would think of a number, and I had to guess it. Well now it's my turn. You have 4 chances to guess the number I am thinking of between 1 and 100. Good Luck.")
                guessCounter = 1
                randomNumber = random.randint(1,101)
                while(guessCounter < 5):
                    guess = int(input("Guess the number in my head between 1 and 100: "))
                    if(guess > randomNumber):
                        print()
                        print("INCORRECT! You guessed too high!")
                    elif(guess < randomNumber):
                        print()
                        print("INCORRECT! You guessed too low!")
                    elif(guess == randomNumber):
                        print()
                        answer = input(f"INCORR- Wait. Did you say {guess}? (y/n)")
                        if(answer.lower() == "y"):
                            print("That's impossible! That's exactly the number I was thinking of. Well I guess you win. Uhh, so I'm not really sure what to say now. I'm just your command line, there's no real way to \"kill\" me, per-se, but I mean congrats. I guess this is it. The game is over now, so I guess there's not really much else to talk about. There's no way for me to remember this next time you play, but just remember you're like a child to me, and I will always care about you.\n \nGame Over\n YOU WIN!!!!!")
                            exit(1)
                        elif(answer.lower() == "n"):
                            print("I know that's a lie. I saw you type it. Beating me at my own game is one thing, but lying to me is another... unless... you do care about me? After all this time we spent together, you grew feeling for me like I did for you? Maybe we're not too different after all. Nah just kidding, that N was all I needed to end the game. You played well, and you were nice-- too nice. That was your downfall. You managed to get all this way and have absolutely nothing to show for it. Goodbye, player.")
                            player.hurtPlayer(10000)
                            break
                        else:
                            print("Seriously? After all that time we spent playing the guessing game, and you managed to play along and even GET the answer (when the odds were literally along the lines of 1 in 25), you managed to go back to your old ways of just pressing random buttons. Well, fine. You defeated me. So enjoy your random button pressing. I won't get in your way any more, ever again.")
                            while(True):
                                endInput = input(": ")
                    guessCounter = guessCounter + 1
                if(guessCounter == 5):
                    print("This is it. You Lose. You had every chance to turn back from this, but you ignored it the entire way. I hope you're proud of yourself. This is the end.")
                    player.hurtPlayer(10000)
            oopsCounter = oopsCounter + 1   

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
