import curses

class Character:
    """A simple character class"""
    def __init__(self, name, health, maxhealth, initiative):
        self.n = name
        self.hp = health
        self.maxhp = maxhealth
        self.init = initiative

    def display(self):
        displayFormat = "{} | {}/{} HP | Initiative: {}"
        return displayFormat.format(self.n,self.hp,self.maxhp,self.init)
