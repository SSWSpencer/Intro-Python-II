import random
from item import Item

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

food = Item("food", "increases your health by 5")
coin = Item("coin", "can be redeemed for 10 points")

def trySpawnEnemy(player, room):
    tryspawn = random.randint(1,5)
    if(tryspawn == 3):
        print()
        print()
        print()
        print(bcolors.FAIL + "You've encountered an enemy!" + bcolors.ENDC)
        enemy = random.randint(0,10)
        enemyHealth = 0
        enemyType = ""
        guessCounter = 1
        possibleScore = 0
        guessedCorrect = False
        numberGuesses = 5
        if("sword" in player.getInventory()):
            print("You have a sword!")
            numberGuesses = 8
        if(enemy <= 5):
            enemyHealth = 10
            enemyType = "Easy"
            possibleScore = 10
        elif(enemy > 5 and enemy < 9):
            enemyHealth = 15
            enemyType = "Medium"
            possibleScore = 15
        elif(enemy >= 9):
            enemyHealth = 20
            enemyType = "Hard"
            possibleScore = 20
        secretNumber = random.randint(0, enemyHealth)
        while(guessCounter <= numberGuesses and not guessedCorrect):
            print(f"Enemy Type: {enemyType}")
            print(f"You have {numberGuesses} chances to guess the number between 0 and {enemyHealth}")
            guess = input(f"Guess {guessCounter}: ")
            try:
                guess = int(guess)
            except:
                print(f"{guess} is not a number!")
            if(guess == secretNumber):
                player.addScore(possibleScore)
                guessedCorrect = True
                print(f"You defeated the enemy! Score increased by {possibleScore}")
                dropItem = random.randint(1,3)
                if(dropItem == 1):
                    print("The enemy dropped 1 food!")
                    room.addItem(food)
                elif(dropItem == 2):
                    print("The enemy dropped 1 coin")
                    room.addItem(coin)
            else:
                print("Incorrect!")
                guessCounter+= 1
            print()
        if(not guessedCorrect):
            print("You were unable to defeat the enemy! -10 Health")
            player.hurtPlayer(10)