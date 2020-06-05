# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, pos, health, inventory, hand, score):
        self.name = name
        self.pos = pos
        self.health = health
        self.inventory = inventory
        self.hand = hand
        self.score = score

    def getHealth(self):
        return (f"{self.health}")

    def hurtPlayer(self, amount):
        self.health -= amount
    
    def healPlayer(self, amount):
        self.health += amount

    def getRoom(self):
        return (f"Position: {self.pos}")

    def getRoomName(self):
        return (f"{self.pos.key}")

    def moveRoom(self, pos):
        self.pos = pos
    
    def getScore(self):
        return(f"{self.score}")
    
    def addScore(self, score):
        self.score += score
    
    def addItem(self, item):
        self.inventory.append(item)

    def getInventory(self):
        output = ""
        counter = 0
        for i in self.inventory:
            output+= (f"Item {counter}: {i.getName()} || {i.getDesc()}\n")
            counter += 1
        return output
