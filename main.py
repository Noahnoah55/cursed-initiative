import curses
from curses import wrapper
from character import Character
from order import Order
import help
import query

" Testing Variables, remove after insert and delete are added "
OrderExample = Order()
OrderExample.add_character(Character("Steve", 10,10,10))
OrderExample.add_character(Character("Rodger", 10,10,20))
OrderExample.add_character(Character("Bob", 10,10,15))

def main(stdscr):
    stdscr.clear()
    curses.curs_set(False)
    OrderExample.renderList(stdscr)
    key = stdscr.getkey()
    while True:
        if key == 'j':
            OrderExample.increment_position()
        elif key == 'k':
            OrderExample.decrement_position()
        elif key == 'a':
            tempChar = query.getCharacter()
            OrderExample.add_character(tempChar)
        elif key == 'd':
            if query.getConfirmation("Really delete?"):
                OrderExample.remove_character()
        elif key == '?':
            help.showHelp()
        elif key == 'q':
            if query.getConfirmation("Really quit?"):
                break
        elif key == 'e':
            if query.getConfirmation("Change Name?"):
                OrderExample.change_name(query.getString(message="Enter a new name"))
            elif query.getConfirmation("Change HP?"):
                OrderExample.change_hp(query.getNumber(message="Enter a new initiative"))
            elif query.getConfirmation("Change Max HP?"):
                OrderExample.change_maxhp(query.getNumber(message="Enter a new initiative"))
            elif query.getConfirmation("Change Initiative?"):
                OrderExample.change_init(query.getNumber(message="Enter a new initiative"))
        stdscr.clear()
        OrderExample.renderList(stdscr)
        stdscr.refresh()
        key = stdscr.getkey()
    stdscr.refresh()

wrapper(main)
