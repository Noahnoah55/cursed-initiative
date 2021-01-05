import curses
import curses.textpad
import curses.ascii
import character

POPUP_WIDTH = 40
POPUP_HEIGHT = 3
POPUP_X = 5
POPUP_Y = 5

# Synonyms for control keys, used in the numberFilter function
SYNONYMS = (curses.KEY_BACKSPACE, curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT)

def getInput(message = "Enter A String", func = lambda x : x):
    output = ""
    popup = curses.newwin(POPUP_HEIGHT,POPUP_WIDTH,POPUP_Y,POPUP_X)
    popup.box()
    popup.addstr(message)
    popup.refresh()
    curses.curs_set(True)
    textwin = popup.subwin(1, POPUP_WIDTH-2, POPUP_Y+1, POPUP_X+1)
    textbox = curses.textpad.Textbox(textwin)
    output = textbox.edit(func)
    curses.curs_set(False)
    popup.clear()
    popup.refresh()
    return output

def getString(message = "Enter A String"):
    return getInput(message).strip()

def numberFilter(char):
    if curses.ascii.isdigit(char) or curses.ascii.iscntrl(char) or char in SYNONYMS:
        return char
    else:
        return None

def getNumber(message = "Enter A Number"):
    return int(getInput(message, numberFilter))

def getConfirmation(message = "Are you sure?"):
    output = None
    popup = curses.newwin(POPUP_HEIGHT,POPUP_WIDTH,POPUP_Y,POPUP_X)
    popup.box()
    popup.addstr(message)
    popup.addstr(1,1,"(y)es or (n)o")
    while True:
        tempchar = popup.getkey()
        if tempchar == "y" or tempchar == "Y":
            output = True
            break
        elif tempchar == "n" or tempchar == "N":
            output = False
            break
    popup.refresh()
    popup.clear()
    popup.refresh()
    return output
    

def getCharacter():
    charName = getString(message = "Enter your character's name")
    charHP = getNumber(message = "Enter your character's HP")
    charMaxHP = getNumber(message = "Enter your character's Maximum HP")
    charInitiative = getNumber(message = "Enter your character's initiative")
    return character.Character(charName, charHP, charMaxHP, charInitiative)

def showInfo(title, message):
    lines = message.count('\n')
    lineList = message.split('\n')
    popup = curses.newwin(2+lines, POPUP_WIDTH, POPUP_Y, POPUP_X)
    popup.box()
    popup.addstr(title)
    for l in range(lines):
        popup.addstr(l+1,1,lineList[l])
    popup.getkey()
    popup.refresh()
    popup.clear()
    popup.refresh()
