# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, pos, health, inventory, hand):
        self.name = name
        self.pos = pos
        self.health = health
        self.inventory = inventory
        self.hand = hand

    def getHealth(self):
        return (f"{self.health}")

    def hurtPlayer(self, amount):
        self.health -= amount

    def getRoom(self):
        return (f"Position: {self.pos}")

    def moveRoom(self, pos):
        self.pos = pos