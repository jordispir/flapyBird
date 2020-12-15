import pygame
import random

pygame.init()
pygame.font.init()
<<<<<<< HEAD

anchura, altura = 1200, 800
window = pygame.display.set_mode((anchura, altura))
out = False

clock = pygame.time.Clock()
clock.tick(30)

xFlapy, yFlapy = 100, (altura/2)
velocity = 1


tuberias = pygame.sprite.Group()
flapyBird = None
backGround = None
xTuberia = random.randrange(100, anchura-100)


vidasText = None
xVidas, yVidas = 800, 100

vidas = 3


def loadObstaculos():
    tuberiaUp = pygame.image.load("tuberiaUp.png")
    tuberiaUpSprite = pygame.sprite.Sprite()
    tuberiaUpSprite.image = tuberiaUp
    tuberiaUpSprite.rect = tuberiaUp.get_rect()
    tuberiaUpSprite.rect.x = random.randrange(100, anchura-100)
    tuberiaUpSprite.rect.y = altura - tuberiaUp.get_height()

    tuberiaDown = pygame.image.load("tuberiaDown.png")
    tuberiaDownSprite = pygame.sprite.Sprite()
    tuberiaDownSprite.image = tuberiaDown
    tuberiaDownSprite.rect = tuberiaDown.get_rect()
    tuberiaDownSprite.rect.x = random.randrange(100, anchura-100)
    tuberiaDownSprite.rect.y = 0

    tuberias.add(tuberiaUpSprite)
    tuberias.add(tuberiaDownSprite)


def loadFlapyBird():
    global flapyBird
    flapyBirdImage = pygame.image.load("flapyBird.png")
    flapyBird = pygame.sprite.Sprite()
    flapyBird.image = flapyBirdImage
    flapyBird.rect = flapyBirdImage.get_rect()
    flapyBird.rect.x = xFlapy
    flapyBird.rect.y = yFlapy

def loadBackGround():
    global backGround
    backGround = pygame.image.load("bg.jpg")

def statusVida():
    global vidasText 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    vidasText = myfont.render("vidas:" + str(vidas), False, (0, 0, 0))

def dibuja():
    window.blit(backGround, (0, 0))
    window.blit(vidasText, (xVidas, yVidas))
    tuberias.draw(window)
    window.blit(flapyBird.image, (flapyBird.rect.x, flapyBird.rect.y))

=======

fps = pygame.time.Clock()
fps.tick(60)

anchura, altura = 1800, 900 
window = pygame.display.set_mode((anchura, altura))

tuberias = pygame.sprite.Group()
imageListUp = ["tuberiaUp100.png", "tuberiaUp150.png", "tuberiaUp200.png", "tuberiaUp300.png"]    
imageListDown = ["tuberiaDown100.png", "tuberiaDown150.png", "tuberiaDown200.png", "tuberiaDown300.png"]    

outDisplay1 = False
outDisplay2 = False
flapyBird = None
font = None
textVidas = None

xFlapy, yFlapy = 100, (altura/2)
xInicial, yInicial = xFlapy, yFlapy

xTuberiaUp = random.randrange(100, anchura)
xTuberiaDown = random.randrange(100, anchura)
xVidas = anchura - 200
yVidas = 50

velocity = 1

vidas = 3
>>>>>>> 983b66a8d624ddc1d737fb39b4d7b062a902df13

def tuberiaUp_inicial():
    global tuberiaUp
    global yTuberiaUp
    global tuberiaUpWidth
    global tuberiaUpHeight

    tuberia = random.choice(imageListUp)
    tuberiaUp = pygame.image.load("tuberiaUp/"+ tuberia)
    tuberiaUpWidth = tuberiaUp.get_width()
    tuberiaUpHeight = tuberiaUp.get_height()
    yTuberiaUp = altura - tuberiaUpHeight 

def tuberiaDown_inicial():
    global tuberiaDown
    global yTuberiaDown
    global tuberiaDownWidth
    global tuberiaDownHeight

    tuberia = random.choice(imageListDown) 
    tuberiaDown = pygame.image.load("tuberiaDown/" + tuberia)
    tuberiaDownWidth = tuberiaDown.get_width()
    tuberiaDownHeight = tuberiaDown.get_height()
    yTuberiaDown = 0

def load_sprites():
    global tuberiaDownSprite
    global tuberiaUpSprite

    tuberiaUpSprite = pygame.sprite.Sprite()
    tuberiaUpSprite.image = tuberiaUp
    tuberiaUpSprite.rect = tuberiaUp.get_rect()
    tuberiaUpSprite.rect.x = xTuberiaUp 
    tuberiaUpSprite.rect.y = yTuberiaUp

    tuberiaDownSprite = pygame.sprite.Sprite()
    tuberiaDownSprite.image = tuberiaDown
    tuberiaDownSprite.rect = tuberiaDown.get_rect()
    tuberiaDownSprite.rect.x = xTuberiaDown
    tuberiaDownSprite.rect.y = yTuberiaDown

    tuberias.add(tuberiaUpSprite)
    tuberias.add(tuberiaDownSprite)


def load_flapyBird():
    global flapyBird
    global flapyBirdImageHeight
    global flapyBirdImageWidth
    flapyBirdImage = pygame.image.load("flapyBird.png")
    flapyBirdImageHeight = flapyBirdImage.get_height()
    flapyBirdImageWidth= flapyBirdImage.get_width()
    flapyBird = pygame.sprite.Sprite()
    flapyBird.image = flapyBirdImage
    flapyBird.rect = flapyBirdImage.get_rect()
    flapyBird.rect.x = xFlapy
    flapyBird.rect.y = yFlapy

def load_font():
    global font
    global textVidas
    font = pygame.font.SysFont("comicsans", 50)
    textVidas = font.render("vidas: "+ str(vidas), False, (0, 0, 0))


def dibuja():
    tuberias.draw(window)
    window.blit(textVidas, (xVidas, yVidas))
    window.blit(flapyBird.image, (flapyBird.rect.x, flapyBird.rect.y))

def update_x():
    global outDisplay1, outDisplay2
    tuberiaDownSprite.rect.x -= 4
    tuberiaUpSprite.rect.x -= 4

    if tuberiaDownSprite.rect.x < 0:
        tuberiaDownSprite.rect.x = anchura  
        outDisplay1 = True
    elif tuberiaUpSprite.rect.x < 0:
        outDisplay2 = True

    else:
        outDisplay1, outDisplay2 = False, False

def update_y():
    global tuberiaUpSprite
    if outDisplay2:

        tuberia = random.choice(imageListUp)
        tuberiaNew = pygame.image.load("tuberiaUp/"+ tuberia)
        tuberiaNewHeight = tuberiaNew.get_height()

        tuberiaNewSprite = pygame.sprite.Sprite()
        tuberiaNewSprite.image = tuberiaNew
        tuberiaNewSprite.rect = tuberiaNew.get_rect()
        tuberiaNewSprite.rect.x = anchura 
        tuberiaNewSprite.rect.y = altura - tuberiaNewHeight 

        tuberias.add(tuberiaNewSprite)

        tuberiaNewSprite.rect.x -= 4


def move_flapyBird():
    global xFlapy, yFlapy

    key = pygame.key.get_pressed()

    xFlapy += velocity
    yFlapy += velocity 

    if key[pygame.K_SPACE]:
        yFlapy -= (velocity/2 * 10)
<<<<<<< HEAD

    flapyBird.rect.x = xFlapy
    flapyBird.rect.y = yFlapy

def colision():
    global vidas
    if (pygame.sprite.spritecollideany(flapyBird, tuberias)):
        vidas -= 1


=======

    flapyBird.rect.x = xFlapy
    flapyBird.rect.y = yFlapy

def colision():
    global vidas
    global xFlapy, yFlapy

    if (pygame.sprite.spritecollideany(flapyBird, tuberias)):
        vidas -= 1

        xFlapy, yFlapy = xInicial, yInicial

    elif yFlapy == altura - flapyBirdImageHeight:
        vidas -= 1
        xFlapy, yFlapy = xInicial, yInicial
    elif yFlapy < 0: 
        vidas -= 1
        xFlapy, yFlapy = xInicial, yInicial
    elif xFlapy == anchura - flapyBirdImageWidth:
        vidas -= 1
        xFlapy, yFlapy = xInicial, yInicial



>>>>>>> 983b66a8d624ddc1d737fb39b4d7b062a902df13
def endGame():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            return True
<<<<<<< HEAD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True



    if vidas == 0:
        return True

    return False

def update():
    window.scroll(int(-xFlapy), int(-yFlapy))

loadFlapyBird()
loadObstaculos()
loadBackGround()
while not endGame():
    window.fill((0, 255, 255))

    moveFlapyBird()
    colision()

    statusVida()
    dibuja()
=======


    return False

tuberiaDown_inicial()
tuberiaUp_inicial()
load_flapyBird()
load_sprites()
while not endGame():
    window.fill((0, 255, 255))

    move_flapyBird()
    colision()

    load_font()
    dibuja()
    update_x()
    update_y()
>>>>>>> 983b66a8d624ddc1d737fb39b4d7b062a902df13
    pygame.display.flip()

