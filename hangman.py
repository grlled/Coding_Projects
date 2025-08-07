import random
from words import thewords

hangman = ["(``)", 
             "|", 
             "+", 
             "---",
             "---",
             "|",
             "/",
             "\\"]

incorrectattempt = 0
gamerunning = True
winner = None
usedletters = []
# make word come at bottom
theword = random.choice(thewords)
thedisplay = ["_"] * len(theword)

def playagain():
    global incorrectattempt, theword, usedletters, thedisplay, gamerunning
    play = input("\nDo you want to play again? (yes/no): ").lower()
    if play == "yes":
        incorrectattempt = 0
        theword = random.choice(thewords)
        usedletters.clear()
        thedisplay[:] = ["_"] * len(theword)
        gamerunning = True 
        return True
    else:
        gamerunning = False
        return False

# get user's letter input
def userinput(thedisplay, theword):
    global incorrectattempt
    inp = input("Pick a letter A-Z\n").lower()
    usedletters.append(inp)
    if inp in theword:
        for index, letter in enumerate(theword): 
            if letter == inp:
                thedisplay[index] = inp
    else:
        incorrectattempt = incorrectattempt + 1
            
        
    
# make hangman and hangy thing appear
print(f"Welcome to hangman!")
def hangplatform(hangman):
    hangman[0] = "(``)" if incorrectattempt > 0 else " "
    hangman[1] = "|" if incorrectattempt > 1 else " "
    hangman[2] = "+" if incorrectattempt > 2 else " "
    hangman[3] = "---" if incorrectattempt > 3 else " "
    hangman[4] = "---" if incorrectattempt > 4 else " "
    hangman[5] = "|" if incorrectattempt > 5 else " "
    hangman[6] = "/" if incorrectattempt > 6 else " "
    hangman[7] = "\\" if incorrectattempt > 7 else " "
    print(f"")
    print(f"      ______________                                ")
    print(f"      |/           |                                ")
    print(f"      |           {hangman[0]}                      ")
    print(f"      |            {hangman[1]}                      ")
    print(f"      |         {hangman[3]}{hangman[2]}{hangman[4]}")
    print(f"      |            {hangman[5]}                     ")
    print(f"      |           {hangman[6]} {hangman[7]}         ")
    print(f"      |    ")
    print(f"   --------  ")
    print(f"")
    print(f"            {" ".join(thedisplay)}            ")
    print(f"")
    print(f"Used letters: {" ".join(usedletters)} ")


    
# determine win or nah
def checkunderscore(thedisplay):
    global winner
    
    if "_" not in thedisplay:
        return True
    
def checkwinandlost():
    global gamerunning
    if checkunderscore(thedisplay):
        gamerunning = False
        hangplatform(hangman)
        print("\nYou Won !!!")
        return True
    elif incorrectattempt == 8:
        gamerunning = False
        hangplatform(hangman)
        print("\nYou Lost..")
        return True

# ask play again

        
#play game
while True:
    while gamerunning:
        hangplatform(hangman)
        print("")
        userinput(thedisplay, theword)
        checkwinandlost()

    if not playagain():
        break
