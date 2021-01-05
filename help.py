from query import showInfo

HELP_MESSAGE = """Press Any Key to Close This Window
? - help
q - quit

MOVEMENT:
j - down
k - up

CHARACTER MANAGEMENT:
a - add character
d - delete character
e - edit character
"""

def showHelp():
    showInfo("Help",HELP_MESSAGE)
