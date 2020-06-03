# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, key, name, desc):
        self.key = key
        self.name = name
        self.desc = desc

    def __str__(self):
        return (f"{self.name} || \"{self.desc}\"")

    def get_name(self):
        return (f"{self.name}")

    def n_to(self, room):
        self.n_to = room
    def s_to(self, room):
        self.s_to = room
    def e_to(self, room):
        self.e_to = room
    def w_to(self, room):
        self.w_to = room

    def get_n(self):
        return (f"{self.n_to.key}")
    def get_s(self):
        return (f"{self.s_to.key}")
    def get_e(self):
        return (f"{self.e_to.key}")
    def get_w(self):
        return (f"{self.w_to.key}")
    