

from graphics import *
from random import *

def clear(win):
    # As found on stackoverflow.com to eliminate repeating undraws
    for item in win.items[:]:
        item.undraw()
    win.update

def getTime():
    return int(round(time.time() * 1000))

def showZombie(win):

    win.setBackground('dimgrey')

    # show intro
    titleText = Text(Point(500, 200), "CONGRATS")
    titleText.setSize(25)
    titleText.setStyle('bold')

    descText = Text(Point(500, 300), "Oh no! It looks like the guard turned into a zombie!\n"
                                     "Once you've clicked to get started, fight him off by clicking on him!")
    descText.setSize(20)

    titleText.draw(win)
    descText.draw(win)

    click = win.getMouse()
    clear(win)

    # Load an image and display in window
    zombie = Image(Point(200,200), "zombie.png")
    zombie.draw(win)

    rspcatch = Text(Point(887,80), "Gotcha!!")
    rspcatch.setSize(30)
    rspcatch.setStyle('bold')

    score = Text(Point(887, 30), "Score: 0")
    score.setSize(20)
    score.setStyle('bold')
    score.draw(win)

    lstTime = startTime = getTime()

    points = 0

    while True:
        click = win.checkMouse()

        # Check if we have a click
        if click is not None:
            anchor = zombie.getAnchor()
            hwidth = zombie.getWidth()/2
            hheight = zombie.getHeight()/2
            if anchor.x - hwidth <= click.x <= anchor.x + hwidth and \
                anchor.y - hheight <= click.y <= anchor.y + hheight:
                # Successful click
                rspcatch.undraw()
                rspcatch.draw(win)
                points += 150
                score.setText("Score: " + str(points))
                score.undraw()
                score.draw(win)
            else:
                rspcatch.undraw()

        # Check if we need to move the zombie
        if getTime() >= lstTime + 1000:
            hwidth = zombie.getWidth()/2
            hheight = zombie.getHeight()/2
            zombie.undraw()
            zombie = Image(Point(randint(0+hwidth,1000-hwidth),randint(0+hheight,500-hheight)), "zombie.png")
            zombie.draw(win)
            lstTime = getTime()

        # Check if winner
        if points >= 750:
            return True


        # Check if game is over
        if getTime() >= startTime + 10000:
            rspcatch.undraw()
            zombie.undraw()
            gameOver = Text(Point(400,240), "GAME OVER!")
            exit = Text(Point(400, 300), "click to exit")
            gameOver.draw(win)
            exit.draw(win)
            click = win.getMouse()
            return False

