#
# Room Drawings
#
from graphics import *

# Soldier
def drawSoldier(win):
    offset = Point(0,-150)
    rect = Rectangle(Point(500+offset.x,300+offset.y), Point(590+offset.x,450+offset.y))
    rect.setFill("brown")
    rect.setOutline("red")
    rect.draw(win)
    triangle = Polygon(Point(460+offset.x,250+offset.y),Point(545+offset.x,350+offset.y), Point(630+offset.x, 250+offset.y))
    triangle.setFill("darkgreen")
    triangle.setOutline("darkgreen")
    triangle.draw(win)
    heads = Circle(Point(545+offset.x,225+offset.y),35)
    heads.setFill("beige")
    heads.setOutline("Grey")
    heads.draw(win)
    legs = Rectangle(Point(500+offset.x, 650+offset.y), Point(540+offset.x, 450+offset.y))
    legs.setFill("Chocolate")
    legs.setOutline("grey")
    legs.draw(win)
    legs2 = legs.clone()
    legs2.move(50, 0)
    legs2.draw(win)
    shoe = Rectangle(Point(500+offset.x,650+offset.y),Point(540+offset.x, 670+offset.y))
    shoe.setFill("brown")
    shoe.setOutline("Brown")
    shoe.draw(win)
    shoe2 = shoe.clone()
    shoe2.move(50,0)
    shoe2.draw(win)
    hand1 = Rectangle(Point(460+offset.x,280+offset.y), Point(500+offset.x,380+offset.y))
    hand1.setFill("chocolate")
    hand1.draw(win)
    hand2 = hand1.clone()
    hand2.move(130,0)
    hand2.draw(win)
    wrist1 = Circle(Point(480+offset.x,380+offset.y),20)
    wrist1.setFill("beige")
    wrist1.draw(win)
    wrist2 = wrist1.clone()
    wrist2.move(130,0)
    wrist2.draw(win)
    lefteyes = Circle(Point(529+offset.x, 210+offset.y), 5)
    lefteyes.setFill("white")
    lefteyes.setOutline("black")
    lefteyes.draw(win)
    righteyes = lefteyes.clone()
    righteyes.move(35, 0)
    righteyes.draw(win)
    lefteyes1 = Circle(Point(530+offset.x, 210+offset.y), 2)
    lefteyes1.setFill("black")
    lefteyes1.setOutline("black")
    lefteyes1.draw(win)
    righteyes2 = lefteyes1.clone()
    righteyes2.move(35, 0)
    righteyes2.draw(win)
    nose = Polygon(Point(540+offset.x, 220+offset.y), Point(550+offset.x,220+offset.y), Point(545+offset.x, 230+offset.y))
    nose.setFill("beige")
    nose.draw(win)
    mouth = Oval(Point(535+offset.x, 240+offset.y), Point(555+offset.x, 250+offset.y))
    mouth.setFill("Red")
    mouth.draw(win)

# Mummy
def drawMummy(win):

    win.setBackground("light blue")

    body = Oval(Point(10, 90), Point(800, 110))
    body.setFill("DarkOliveGreen")
    body.setOutline("DarkOliveGreen")
    body.draw(win)
    body1 = Circle(Point(750, 98), 4)
    body1.setFill("Red")
    body1.setOutline("Red")
    body1.draw(win)
    body2 = Circle(Point(700, 103), 3)
    body2.setFill("indigo")
    body2.setOutline("indigo")
    body2.draw(win)
    body3 = Circle(Point(650, 99), 4)
    body3.setFill("Blue")
    body3.setOutline("Blue")
    body3.draw(win)
    body4 = Circle(Point(600, 102), 4)
    body4.setFill("Yellow")
    body4.setOutline("Yellow")
    body4.draw(win)
    body5 = Circle(Point(550, 97), 3)
    body5.setFill("Red")
    body5.setOutline("Red")
    body5.draw(win)
    body6 = Circle(Point(500, 103), 3)
    body6.setFill("Green")
    body6.setOutline("Green")
    body6.draw(win)
    body7 = Circle(Point(450, 98), 4)
    body7.setFill("Blue")
    body7.setOutline("Blue")
    body7.draw(win)
    body8 = Circle(Point(400, 102), 4)
    body8.setFill("Yellow")
    body8.setOutline("Yellow")
    body8.draw(win)
    body9 = Circle(Point(350, 99), 4)
    body9.setFill("fuchsia")
    body9.setOutline("fuchsia")
    body9.draw(win)
    body10 = Circle(Point(300, 103), 3)
    body10.setFill("magenta")
    body10.setOutline("magenta")
    body10.draw(win)
    body11 = Circle(Point(250, 98), 4)
    body11.setFill("cyan")
    body11.setOutline("cyan")
    body11.draw(win)
    body12 = Circle(Point(200, 102), 4)
    body12.setFill("lime")
    body12.setOutline("lime")
    body12.draw(win)
    body13 = Circle(Point(150, 99), 4)
    body13.setFill("violet")
    body13.setOutline("violet")
    body13.draw(win)
    body14 = Circle(Point(100, 98), 3)
    body14.setFill("navy")
    body14.setOutline("navy")
    body14.draw(win)
    body15 = Circle(Point(50, 102), 3)
    body15.setFill("coral")
    body15.setOutline("coral")
    body15.draw(win)

    head = Oval(Point(800, 75), Point(890, 125))
    head.setFill("DarkOliveGreen")
    head.setOutline("DarkOliveGreen")
    head.draw(win)
    eye1 = Circle(Point(820, 80), 7)
    eye1.setFill("MidnightBlue")
    eye1.draw(win)
    eye2 = Circle(Point(870, 80), 7)
    eye2.setFill("MidnightBlue")
    eye2.draw(win)
    mouth = Oval(Point(820, 100), Point(870, 110))
    mouth.setFill("MidnightBlue")
    mouth.draw(win)
    tongue = Oval(Point(830, 100), Point(840, 120))
    tongue.setFill("Maroon")
    tongue.setOutline("Maroon")
    tongue.draw(win)
    teeth = Polygon(Point(830, 100), Point(833, 110), Point(836, 100))
    teeth.setFill("White")
    teeth.draw(win)
    teeth2 = Polygon(Point(853, 100), Point(856, 110), Point(859, 100))
    teeth2.setFill("White")
    teeth2.draw(win)
    center = Point(400, 200)
    circ = Circle(center, 50)
    circ.setFill("gold")
    circ.setOutline("Yellow")
    circ.draw(win)
    label = Text(center, "COIN")
    label.draw(win)

    # Creating Pyramid

    triangle = Polygon(Point(100, 680), Point(300, 200), Point(550, 630))
    triangle.setFill("Gold")
    triangle.setOutline("Grey")
    triangle.draw(win)
    triangle1 = Polygon(Point(100, 680), Point(300, 200), Point(100, 490))
    triangle1.setFill("Gold")
    triangle1.setOutline("Grey")
    triangle1.draw(win)
    rect = Rectangle(Point(100, 680), Point(140, 600))
    rect.setFill("sienna")
    rect.setOutline("sienna")
    rect.draw(win)
    rect1 = Rectangle(Point(510, 630), Point(550, 550))
    rect1.setFill("sienna")
    rect1.setOutline("sienna")
    rect1.draw(win)
    flame = Polygon(Point(100, 600), Point(140, 600), Point(120, 580))
    flame.setFill("Red")
    flame.setOutline("red")
    flame.draw(win)
    flame2 = Polygon(Point(510, 550), Point(530, 530), Point(550, 550))
    flame2.setFill("Red")
    flame2.setOutline("red")
    flame2.draw(win)

    # creating mummy
    legm = Rectangle(Point(660, 650), Point(700, 500))
    legm.setFill("White")
    legm.setOutline("grey")
    legm.draw(win)
    legm2 = legm.clone()
    legm2.move(50, 0)
    legm2.draw(win)
    bodym = Oval(Point(660, 350), Point(750, 500))
    bodym.setFill("white")
    bodym.setOutline("white")
    bodym.draw(win)
    headm = Rectangle(Point(670, 290), Point(740, 350))
    headm.setFill("white")
    headm.setOutline("grey")
    headm.draw(win)
    lefteyem = Circle(Point(680, 300), 3)
    lefteyem.setFill("red")
    lefteyem.setOutline("black")
    lefteyem.draw(win)
    righteyem = lefteyem.clone()
    righteyem.move(50, 0)
    righteyem.draw(win)

# Snow Man
def shapes(win, x, y, dx, dy):
    for i in range(3):
        cloud = Oval(Point(y - 50, x), Point(dy, 80))
        cloud.setFill('grey')
        cloud.setOutline('grey')
        cloud.draw(win)
        shape = Oval(Point(x, y), Point(dx, dy))
        shape.setFill('white')
        shape.setOutline('white')
        shape.draw(win)
        tri = Polygon(Point(270, y - 50), Point(x + 170, y + 10), Point(dx + 200, y + 10))
        tri.setFill('green')
        tri.setOutline('green')
        tri.draw(win)
        x = x - 10
        y = y + 50
        dx = dx + 10
        dy = dy + 55
        tri = Polygon(Point(x + 150, y + 50), Point(x + 125, y - 25), Point(x + 175, y - 25))
    return shapes


def drawSnowMan(win):

    win.setBackground('dimgrey')

    land = Oval(Point(-150, 280), Point(500, 500))
    land.setFill('gray92')
    land.setOutline('gray')
    land.draw(win)
    trunk = Line(Point(270, 200), Point(270, 350))
    trunk.setOutline('chocolate')
    trunk.setWidth(10)
    trunk.draw(win)
    shapes(win, 50, 150, 120, 210)
    eye1 = Circle(Point(70, 175), 5)
    eye1.setFill('black')
    eye1.draw(win)
    eye2 = eye1.clone()
    eye2.move(30, 0)
    eye2.draw(win)
    mouth = Oval(Point(70, 190), Point(100, 195))
    mouth.setFill('red')
    mouth.draw(win)
    nose = Polygon(Point(85, 175), Point(80, 185), Point(90, 185))
    nose.setFill('orange')
    nose.draw(win)
    rect = Rectangle(Point(20, 312), Point(150, 350))
    rect.setFill('gray92')
    rect.setOutline('gray92')
    rect.draw(win)
    scarf = Polygon(Point(58, 205), Point(85, 220), Point(85, 240), Point(85, 220), Point(112, 205), Point(85, 220))
    scarf.setOutline('black')
    scarf.setWidth('10')
    scarf.draw(win)


#dragon
def drawDragon(win):

    # win.setCoords(0.0, 0.0, 10.0, 10.0)

    # body = Circle(Point(5, 4), 1.5)
    # body.setFill("light green")
    # body.draw(win)
    #
    # cover1 = Rectangle(Point(3, 4.5), Point(7, 7))
    # cover1.setFill("black")
    # cover1.draw(win)
    #
    # tri = Polygon(Point(4.3, 4.5), Point(4.7, 4.5), Point(4.5, 5))
    # tri.setFill("blue")
    # tri.draw(win)
    #
    # mtri = tri.clone()
    # mtri.move(0.5, 0)
    # mtri.draw(win)
    #
    # ttri = tri.clone()
    # ttri.move(1, 0)
    # ttri.draw(win)
    #
    # ntri = tri.clone()
    # ntri.move(1.5, 0)
    # ntri.draw(win)
    #
    # ltri = tri.clone()
    # ltri.move(-0.5, 0)
    # ltri.draw(win)
    #
    # face = Rectangle(Point(5.7, 3.7), Point(7.3, 5.5))
    # face.setFill("blue")
    # face.draw(win)
    #
    # eye = Circle(Point(6, 5), 0.2)
    # eye.setFill("yellow")
    # eye.setOutline("red")
    # eye.draw(win)
    #
    # fire = Oval(Point(7, 4), Point(9, 4.5))
    # fire.setFill("red")
    # fire.draw(win)
    #
    # fiire = Oval(Point(7, 4.1), Point(8.7, 4.4))
    # fiire.setFill("orange")
    # fiire.draw(win)
    #
    # firre = Oval(Point(7, 4.2), Point(8.4, 4.3))
    # firre.setFill("yellow")
    # firre.draw(win)
    #
    # eye = Circle(Point(6, 4.9), 0.1)
    # eye.setFill("black")
    # eye.setOutline("white")
    # eye.draw(win)
    #
    # mouth = Polygon(Point(6.5, 4.5), Point(6.7, 4.5), Point(6.6, 4.2))
    # mouth.setFill("white")
    # mouth.draw(win)
    #
    # mouthh = mouth.clone()
    # mouthh.move(0.2, 0)
    # mouthh.draw(win)
    #
    # mouthhh = mouth.clone()
    # mouthhh.move(0.4, 0)
    # mouthhh.draw(win)
    #
    # moutth = Polygon(Point(6.6, 4), Point(6.8, 4), Point(6.7, 4.3))
    # moutth.setFill("white")
    # moutth.draw(win)
    #
    # l = moutth.clone()
    # l.move(0.2, 0)
    # l.draw(win)
    #
    # face = Rectangle(Point(4.7, 2), Point(4.5, 2.8))
    # face.setFill("blue")
    # face.draw(win)
    #
    # face = Rectangle(Point(5.3, 2), Point(5.5, 2.8))
    # face.setFill("blue")
    # face.draw(win)

    dragon = Image(Point(500, 180), "dragon.png")
    dragon.draw(win)

def drawPrincess(win):

    #Princess
    win.setBackground("white")

    #Landscape
    sky = Rectangle(Point(1000,0), Point(0,325))
    sky.setFill("skyblue")
    sky.draw(win)

    grass = Rectangle(Point(1000,325), Point(0,500))
    grass.setFill("spring green")
    grass.draw(win)

    cloud = Circle(Point(800, 100), 50)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(860, 100), 40)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(900, 110), 20)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)
    cloud = Circle(Point(750, 100), 20)
    cloud.setFill("white")
    cloud.setOutline("white")
    cloud.draw(win)

    # wall = Rectangle(Point(250,0), Point(300, 500))
    # wall.setFill("sienna")
    # wall.draw(win)

    boubble = Circle(Point(150, 60), 50)
    boubble.setFill("white")
    boubble.setOutline("white")
    boubble.draw(win)
    message = Text(Point(150, 60),"You won!\nThank you!\nYou saved me")
    message.draw(win)

    # boubble2 = Circle(Point(650, 60), 50)
    # boubble2.setFill("white")
    # boubble2.setOutline("white")
    # boubble2.draw(win)
    # message = Text(Point(650, 60),"My princess,\nI will soon be back\n to save you")
    # message.draw(win)

    # boubble3 = Circle(Point(460, 60), 60)
    # boubble3.setFill("white")
    # boubble3.setOutline("white")
    # boubble3.draw(win)
    # message = Text(Point(460, 50),"Stop!,\nYou need to pay \n5 golden coins!!!\n\nConcor all the evil\n in the six rooms")
    # message.draw(win)

    #Head
    trunk = Rectangle(Point(90, 195), Point(110, 175))
    trunk.setFill("moccasin")
    trunk.draw(win)
    center = Point(100,150)
    circ = Circle(center, 32)
    circ.setFill("moccasin")
    circ.draw(win)

       #Crown
    crown = Polygon(Point(120, 125), Point(80, 125), Point(100, 80))
    crown.setFill("gold")
    crown.setOutline("yellow")
    crown.draw(win)
    crown = Polygon(Point(120, 125), Point(100, 125), Point(120, 90))
    crown.setFill("gold")
    crown.setOutline("yellow")
    crown.draw(win)
    crown = Polygon(Point(120, 125), Point(80, 125), Point(80, 90))
    crown.setFill("gold")
    crown.setOutline("yellow")
    crown.draw(win)

    stone = Circle(Point(100,95), 3)
    stone.setFill("aqua")
    stone.setOutline("fuchsia")
    stone.draw(win)

    stone1 = Circle(Point(99.9,88), 1.5)
    stone1.setFill("aqua")
    stone1.setOutline("fuchsia")
    stone1.draw(win)
    stone2 = stone1.clone()
    stone2.move(0, 13)
    stone2.draw(win)

    #Eyes
    leftEye = Circle(Point(90,145), 5)
    leftEye.setFill("white")
    leftEye.setOutline("black")

    rightEye = leftEye.clone()

    rightEye.move(20,0)
    leftEye.draw(win)
    rightEye.draw(win)

    leftEye = Circle(Point(90,145), 1.5)
    leftEye.setFill("blue")
    leftEye.setOutline("midnightblue")

    rightEye = leftEye.clone()

    rightEye.move(20,0)
    leftEye.draw(win)
    rightEye.draw(win)

    # Mouth
    mouth = Circle(Point(100, 160), 10)
    mouth.setFill("salmon")
    mouth.setOutline("salmon")
    mouth.draw(win)

    noseleft = Circle(Point(97, 160), 1.0)
    noseleft.setFill("black")
    noseleft.setOutline("black")

    noseright = noseleft.clone()

    noseright.move(7, 0)
    noseleft.draw(win)
    noseright.draw(win)

    #Ears
    earleft = Polygon(Point(121, 125), Point(126, 130), Point(127, 120))
    earleft.setFill("peachpuff")
    earleft.setOutline("salmon")
    earleft.draw(win)

    earright = Polygon(Point(75, 130), Point(81, 125), Point(72, 120))
    earright.setFill("peachpuff")
    earright.setOutline("salmon")
    earright.draw(win)

    # Feet

    #Body
    legleft = Rectangle(Point(95, 350), Point(88, 370))
    legleft.setFill("moccasin")
    legleft.draw(win)

    rightleg = legleft.clone()
    rightleg.move(20,0)
    rightleg.draw(win)

    #Arms
    armleft = Rectangle(Point(70, 190), Point(77, 250))
    armleft.setFill("moccasin")
    armleft.draw(win)

    armright = armleft.clone()
    armright.move(52,0)
    armright.draw(win)

    center = Point(70, 250)
    handleft = Circle(center, 7)
    handleft.setOutline("black")
    handleft.setFill("moccasin")
    handleft.draw(win)

    handright = handleft.clone()
    handright.move(57, 0)
    handright.draw(win)

    footleft = Rectangle(Point(88, 370), Point(100, 380))
    footleft.setOutline("black")
    footleft.setFill("darkgoldenrod")
    footleft.draw(win)

    footright = footleft.clone()
    footright.move(20, 0)
    footright.draw(win)

    # Dress-lower
    dresslower = Polygon(Point(35, 350), Point(100, 220), Point(165, 350))
    dresslower.setFill("hotpink")
    dresslower.draw(win)

    #Dress-upper
    dressupper = Polygon(Point(60, 190), Point(100, 250), Point(140, 190))
    dressupper.setFill("violet")
    dressupper.draw(win)

    coin1 = Circle(Point(45,344), 2.5)
    coin1.setFill("gold")
    coin1.setOutline("yellow")

    coin2 = coin1.clone()
    coin2.move(10,0)

    coin3 = coin1.clone()
    coin3.move(20,0)

    coin4 = coin1.clone()
    coin4.move(30,0)

    coin5 = coin1.clone()
    coin5.move(40,0)

    coin6 = coin1.clone()
    coin6.move(50,0)

    coin7 = coin1.clone()
    coin7.move(60,0)

    coin8 = coin1.clone()
    coin8.move(70,0)

    coin9 = coin1.clone()
    coin9.move(80,0)

    coin10 = coin1.clone()
    coin10.move(90,0)

    coin11 = coin1.clone()
    coin11.move(100,0)

    coin12 = coin1.clone()
    coin12.move(110,0)

    coin1.draw(win)
    coin2.draw(win)
    coin3.draw(win)
    coin4.draw(win)
    coin5.draw(win)
    coin6.draw(win)
    coin7.draw(win)
    coin8.draw(win)
    coin9.draw(win)
    coin10.draw(win)
    coin11.draw(win)
    coin12.draw(win)


    #Prince

       #Head
    trunk = Rectangle(Point(590, 195), Point(610, 175))
    trunk.setFill("moccasin")
    trunk.draw(win)
    center = Point(600,150)
    circ = Circle(center, 32)
    circ.setFill("moccasin")
    circ.draw(win)

       #Crown
    crown = Polygon(Point(620, 125), Point(580, 125), Point(600, 80))
    crown.setFill("gold")
    crown.draw(win)
    crown = Polygon(Point(620, 125), Point(600, 125), Point(620, 90))
    crown.setFill("gold")
    crown.draw(win)
    crown = Polygon(Point(620, 125), Point(580, 125), Point(580, 90))
    crown.setFill("gold")
    crown.draw(win)

    #Eyes
    leftEye = Circle(Point(590,145), 5)
    leftEye.setFill("white")
    leftEye.setOutline("black")

    rightEye = leftEye.clone()

    rightEye.move(20,0)
    leftEye.draw(win)
    rightEye.draw(win)

    leftEye = Circle(Point(590,145), 1.5)
    leftEye.setFill("blue")
    leftEye.setOutline("midnightblue")

    rightEye = leftEye.clone()

    rightEye.move(20,0)
    leftEye.draw(win)
    rightEye.draw(win)

       #Mouth
    mouth = Circle(Point(600, 160), 10)
    mouth.setFill("salmon")
    mouth.setOutline("salmon")
    mouth.draw(win)

    noseleft = Circle(Point(597,160), 1.0)
    noseleft.setFill("black")
    noseleft.setOutline("black")

    noseright = noseleft.clone()

    noseright.move(7,0)
    noseleft.draw(win)
    noseright.draw(win)

    #Ears
    earleft = Polygon(Point(620, 125), Point(626, 130), Point(627, 120))
    earleft.setFill("peachpuff")
    earleft.setOutline("salmon")
    earleft.draw(win)

    earright = Polygon(Point(575, 130), Point(581, 125), Point(572, 120))
    earright.setFill("peachpuff")
    earright.setOutline("salmon")
    earright.draw(win)

    #Body
    legleft = Rectangle(Point(590, 350), Point(583, 370))
    legleft.setFill("moccasin")
    legleft.draw(win)

    rightleg = legleft.clone()
    rightleg.move(30,0)
    rightleg.draw(win)


    #Clothes
    upperbody = Rectangle(Point(565, 190), Point(635, 270))
    upperbody.setFill("maroon")
    upperbody.draw(win)

    center = Point(560,195)
    shoulder1 = Circle(center, 15)
    shoulder1.setFill("gold")
    shoulder1.draw(win)

    shoulder2 = shoulder1.clone()
    shoulder2.move(80,0)
    shoulder2.draw(win)

    pantleft = Rectangle(Point(573, 350), Point(599, 270))
    pantleft.setFill("gray")
    pantleft.draw(win)

    pantright = pantleft.clone()
    pantright.move(30,0)
    pantright.draw(win)

    #Arms
    armleft = Rectangle(Point(565, 210), Point(555, 250))
    armleft.setFill("moccasin")
    armleft.draw(win)

    armright = armleft.clone()
    armright.move(80,0)
    armright.draw(win)

    #Feet
    center = Point(557, 250)
    handleft = Circle(center, 8)
    handleft.setOutline("black")
    handleft.setFill("moccasin")
    handleft.draw(win)

    handright = handleft.clone()
    handright.move(85, 0)
    handright.draw(win)

    footleft = Rectangle(Point(580, 370), Point(600,385))
    footleft.setOutline("black")
    footleft.setFill("black")
    footleft.draw(win)

    footright = footleft.clone()
    footright.move(30,0)
    footright.draw(win)

    coin1 = Circle(Point(600,220), 2.5)
    coin1.setFill("gold")
    coin1.setOutline("yellow")
    coin1.draw(win)

    coin2 = coin1.clone()
    coin2.move(0,15)
    coin2.draw(win)

    coin3 = coin1.clone()
    coin3.move(0,30)
    coin3.draw(win)



    # #Guard
    # neck = Rectangle(Point(375, 165), Point(390, 195))
    # neck.setFill("moccasin")
    # neck.draw(win)
    #
    # center = Point(385, 150)
    # head = Circle(center, 25)
    # head.setFill("moccasin")
    # head.draw(win)
    #
    # eye = Circle(Point(397, 150), 4)
    # eye.setOutline("black")
    # eye.setFill("white")
    # eye.draw(win)
    #
    # pupil = Circle(Point(397.4, 150), 1)
    # pupil.setFill("midnightblue")
    # pupil.setOutline("blue")
    # pupil.draw(win)
    #
    # chest = Rectangle(Point(365, 190), Point(400, 270))
    # chest.setFill("light slate grey")
    # chest.draw(win)
    #
    # center = Point(381,195)
    # armpuff = Circle(center, 15)
    # armpuff.setFill("white")
    # armpuff.draw(win)
    #
    # arm = Rectangle(Point(378, 195), Point(450, 205))
    # arm.setFill("moccasin")
    # arm.draw(win)
    #
    # leg = Rectangle(Point(373, 350), Point(390, 270))
    # leg.setFill("mintcream")
    # leg.draw(win)
    #
    # foot = Rectangle(Point(370, 350), Point(400, 365))
    # foot.setOutline("black")
    # foot.setFill("black")
    # foot.draw(win)
    #
    # hat = Rectangle(Point(360, 70), Point(410, 135))
    # hat.setFill("black")
    # hat.draw(win)
    #
    # shield = Rectangle(Point(450, 220), Point(460, 135))
    # shield.setFill("silver")
    # shield.draw(win)
