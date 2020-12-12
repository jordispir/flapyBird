import pygame
import random

pygame.init()
pygame.font.init()

fps = pygame.time.Clock()
fps.tick(60)

anchura, altura = 1800, 900 
window = pygame.display.set_mode((anchura, altura))

tuberias = pygame.sprite.Group()
imageListUp = ["tuberiaUp100.png", "tuberiaUp150.png", "tuberiaUp200.png", "tuberiaUp300.png"]    

outDisplay1 = False
outDisplay2 = False
flapyBird = None
font = None
textVidas = None

xFlapy, yFlapy = 100, (altura/2)
xInicial, yInicial = xFlapy, yFlapy

xTuberia = random.randrange(100, anchura)
xTuberia2 = random.randrange(100, anchura)
yTuberia2 = 0 
xVidas = anchura - 200
yVidas = 50

velocity = 1

vidas = 3

def tuberia_incial():
    global tuberiaUp
    global yTuberia
    global tuberiaWidth
    global tuberiaHeight

    tuberia = random.choice(imageListUp)
    tuberiaUp = pygame.image.load(tuberia)
    tuberiaWidth = tuberiaUp.get_width()
    tuberiaHeight = tuberiaUp.get_height()
    yTuberia = altura - tuberiaHeight 

def load_obstaculos():
    global tuberiaDownSprite
    global tuberiaUpSprite
    tuberiaUpSprite = pygame.sprite.Sprite()
    tuberiaUpSprite.image = tuberiaUp
    tuberiaUpSprite.rect = tuberiaUp.get_rect()
    tuberiaUpSprite.rect.x = xTuberia 
    tuberiaUpSprite.rect.y = yTuberia

    tuberiaDown = pygame.image.load("tuberiaDown.png")
    tuberiaDownSprite = pygame.sprite.Sprite()
    tuberiaDownSprite.image = tuberiaDown
    tuberiaDownSprite.rect = tuberiaDown.get_rect()
    tuberiaDownSprite.rect.x = xTuberia2
    tuberiaDownSprite.rect.y = yTuberia2

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
        tuberiaUpSprite.rect.x = anchura  
        outDisplay2 = True

    else:
        outDisplay1, outDisplay2 = False, False


def move_flapyBird():
    global xFlapy, yFlapy

    key = pygame.key.get_pressed()

    xFlapy += velocity
    yFlapy += velocity 

    if key[pygame.K_SPACE]:
        yFlapy -= (velocity/2 * 10)

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



def endGame():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            return True


    return False

tuberia_incial()
load_flapyBird()
load_obstaculos()
while not endGame():
    window.fill((0, 255, 255))

    move_flapyBird()
    colision()

    load_font()
    dibuja()
    update_x()
    #updateY()
    pygame.display.flip()

