#
# Escape Castle Game
# Lynn B. Tyra M. Vendela L. Anine K. Salome A.
#

from graphics import *
from Drawings import *
from Zombie import *

invalidEntry = "Sorry. we didn't get that, please try again"
invalidRoom = "Oops, you already visited this room, please try another one"

introTitle = "Hi there, Welcome to Escape Castle! Before getting started, let me introduce the game to you."

introDesc = "To win the game you need to free the princess from the castle!\n" \
            "It will be a tough fight!\n" \
            "To move in either direction type: south, north, east, west"

menuIntro = "You stand in front of the castle, but the guard is not letting you in because you don't have enough coins.\n" \
            "To be able to free the princess you need four golden coins. You need to go face the horror of the game\n" \
            "and go through all 4 rooms, 1 golden coin for each room."

roomNorthDesc = "\n\n\nYou are now caught in the labyrinth in a pyramid and hear sounds approaching you"
roomNorthQuestion = "Suddenly, you see a mummy and a its mummy snake, do you try to KILL them or do you try to RUN?"
roomNorthRA = "run"
roomNorthWA = "kill"
roomNorthReason = "You can't kill what's already dead!"
roomNorthDrawing = drawMummy

roomSouthDesc = "You are currently in the freezing Winter Wonderland,\n" \
                "or well it used to be a wonderland before the angry snowman brought terrible snowstorms\n" \
                "and scared everyone off the land. You defeat him by making him a kind man."
roomSouthQuestion = "Do you try to TALK to him or do you try to make him less cold by offering some HOT CHOCOLATE? "
roomSouthRA = "talk"
roomSouthWA = "hot chocolate"
roomSouthReason = "Hot Chocolate might warm you up, but it melts snow!"
roomSouthDrawing = drawSnowMan

roomEastDesc = "There is a furious dragon spitting fire towards you.\n" \
               "You decide to hide in a corner behind a stone from the fire to figure out your next move."
roomEastQuestion = "What is your next move, to trow a FIREBOMB or to use your SWORD for combat?\n"
roomEastRA = "sword"
roomEastWA = "firebomb"
roomEastReason = "You can't fight fire with fire!"
roomEastDrawing = drawDragon

roomWestDesc = "You choose to go west. Very dangerous...\n" \
               "In this land far far away there's an armed soldier thirsty for blood and a fight.\n" \
               "You better bring on your best game to win this one! You decided to wait for the angry soldier.\n" \
               "Suddenly, you stand face to face with Armed Soldier, you don't have a choice but to attack."
roomWestQuestion = "This is a guessing game, do you use KNIFE or FISTS? "
roomWestRA = "knife"
roomWestWA = "fists"
roomWestReason = "Ha ha, you really thought you were stronger than a soldier!"
roomWestDrawing = drawSoldier




def clear(win):
    # As found on stackoverflow.com to eliminate repeating undraws
    for item in win.items[:]:
        item.undraw()
    win.update

def drawCoins(win, coins):
    for i in range(coins):
        coin = Image(Point(850 + i * 35, 100), "coin.png")
        coin.draw(win)


def showGameOver(win, reason):
    gameOverText = Text(Point(500, 200), "GAME OVER")
    gameOverText.setSize(30)
    gameOverText.setStyle('bold')


    gameOverDescText = Text(Point(500, 300), "Sorry to see you lose, click to try again!")
    gameOverDescText.setSize(20)

    gameOverReasonText = Text(Point(500, 250), reason)
    gameOverReasonText.setSize(20)
    gameOverReasonText.setStyle('bold')


    gameOverText.draw(win)
    gameOverDescText.draw(win)
    gameOverReasonText.draw(win)

    click = win.getMouse()
    clear(win)

def showPrincess(win):
    restartText = Text(Point(500, 900), "Click to restart")
    restartText.setSize(20)
    # restartText.setStyle('bold')


    drawPrincess(win)
    restartText.draw(win)

    click = win.getMouse()
    clear(win)


def showIntro(win):

    win.setBackground("light blue")

    titleText = Text(Point(500, 200), introTitle)
    titleText.setSize(20)
    titleText.setStyle('bold')

    descText = Text(Point(500, 250), introDesc)
    descText.setSize(15)

    startText = Text(Point(500, 400), "Click to Start!")
    startText.setSize(25)
    startText.setStyle('bold')
    startText.setTextColor('green')


    titleText.draw(win)
    descText.draw(win)
    startText.draw(win)


    click = win.getMouse()
    titleText.undraw()
    descText.undraw()
    startText.undraw()

def showRoom(win, description, question, rightAnswer, wrongAnswer, drawingFunc):

    errorText = Text(Point(500, 475), invalidEntry)
    errorText.setSize(15)
    errorText.setTextColor('red')

    descText = Text(Point(500, 320), description)
    descText.setSize(20)
    questionText = Text(Point(500, 400), question)
    questionText.setSize(20)
    questionText.setStyle('bold')
    answerEntry = Entry(Point(500, 440), 30)
    answerEntry.setSize(25)

    drawingFunc(win)

    descText.draw(win)
    questionText.draw(win)
    answerEntry.draw(win)


    while True:
        key = win.getKey()

        errorText.undraw()

        if key == "Return":
            answer = answerEntry.getText()
            answer = answer.lower()
            answer = answer.strip()

            if answer == rightAnswer:
                return True
            elif answer == wrongAnswer:
                return False
            else:
                errorText.draw(win)




def showMenu(win):

    coins = 0
    result = False
    score = 0
    visitedRooms = []

    while True:

        win.setBackground("light blue")
        introText = Text(Point(500, 330), menuIntro)
        scoreText = Text(Point(887, 30), "Score: " + str(score))
        scoreText.setSize(20)
        scoreText.setStyle('bold')
        scoreText.draw(win)
        answerEntry = Entry(Point(500,400),30)
        answerEntry.setSize(25)
        introText.draw(win)
        answerEntry.draw(win)

        castle = Image(Point(500,150), "castle.png")

        door1 = Image(Point(300,150), "door.png")
        door2 = Image(Point(700,150), "door.png")
        door3 = Image(Point(500,50), "door.png")
        door4 = Image(Point(500,250), "door.png")

        castle.draw(win)
        door1.draw(win)
        door2.draw(win)
        door3.draw(win)
        door4.draw(win)

        errorText = Text(Point(500, 450), invalidEntry)
        errorText.setSize(15)
        errorText.setTextColor('red')


        while True:
            key = win.getKey()

            errorText.undraw()

            if key == "Return":
                answer = answerEntry.getText()
                answer = answer.lower()
                answer = answer.strip()

                if answer in visitedRooms:
                    errorText.setText(invalidRoom)
                    errorText.draw(win)
                    continue

                if answer == "north":
                    visitedRooms.append(answer)
                    clear(win)
                    result = showRoom(win, roomNorthDesc, roomNorthQuestion, roomNorthRA, roomNorthWA, roomNorthDrawing)
                    break


                elif answer == "south":
                    visitedRooms.append(answer)
                    clear(win)
                    result = showRoom(win, roomSouthDesc, roomSouthQuestion, roomSouthRA, roomSouthWA, roomSouthDrawing)
                    break

                elif answer == "east":
                    visitedRooms.append(answer)
                    clear(win)
                    result = showRoom(win, roomEastDesc, roomEastQuestion, roomEastRA, roomEastWA, roomEastDrawing)
                    break

                elif answer == "west":
                    visitedRooms.append(answer)
                    clear(win)
                    result = showRoom(win, roomWestDesc, roomWestQuestion, roomWestRA, roomWestWA, roomWestDrawing)
                    break

                else:
                    errorText.setText(invalidEntry)
                    errorText.draw(win)

        clear(win)
        if result == True:
            coins = coins + 1
            drawCoins(win, coins)
            score = score + 100

            # check if we win
            if (coins >= 4):
                clear(win)
                drawCoins(win, coins)
                result = showZombie(win)
                clear(win)
                if (result == True):
                    showPrincess(win)
                    coins = score = 0
                    visitedRooms = []
                    break
                else:
                    showGameOver(win, '')
                    coins = score = 0
                    visitedRooms = []


        else:
            coins = score = 0
            visitedRooms = []
            if answer == "north":
                showGameOver(win, roomNorthReason)
            elif answer == "south":
                showGameOver(win, roomSouthReason)
            elif answer == "east":
                showGameOver(win, roomEastReason)
            elif answer == "west":
                showGameOver(win, roomWestReason)


def main():
    win = GraphWin("Escape Castle", 1000, 500)

    showIntro(win)
    showMenu(win)

    win.close()

main()
