class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return(f"{self.name} || {self.description}")

    def getName(self):
        return (f"{self.name}")

    def getDesc(self):
        return (f"{self.description}")