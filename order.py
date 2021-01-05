import curses

class Order:
    def __init__(self):
        self.characters = []
        self.length = len(self.characters)
        self.position = 0

    # Potential for optimization here, but it shouldn't matter much
    def __round_position(self):
        if self.length > 0:
            self.position = self.position % self.length
        else:
            self.position = 0

    def increment_position(self):
        self.position += 1
        self.__round_position()

    def decrement_position(self):
        self.position -= 1
        self.__round_position()

    def remove_character(self):
        self.characters.pop(self.position)
        self.length = len(self.characters)
        self.sort_list()
        self.__round_position()

    def add_character(self,character):
        self.characters.append(character)
        self.length = len(self.characters)
        self.sort_list()

    def sort_list(self):
        self.characters.sort(key=lambda character : character.init,reverse=True)

    def renderList(self,window,y=0,x=0,hlit=True):
        for character in self.characters:
            args = []
            if y == self.position and hlit:
                args.append(curses.A_STANDOUT)
            window.addstr(y,x,character.display(),*args)
            y += 1

    def change_name(self, name):
        self.characters[self.position].n = name

    def change_hp(self, hp):
        self.characters[self.position].hp = hp

    def change_maxhp(self, maxhp):
        self.characters[self.position].maxhp = maxhp

    # TODO: Eventually have the position follow the edited character
    def change_init(self, init):
        self.characters[self.position].init = init
        self.sort_list()
