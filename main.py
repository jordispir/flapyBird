import pygame
import random

pygame.init()
pygame.font.init()

anchura, altura = 1200, 800
window = pygame.display.set_mode((anchura, altura))

xFlapy, yFlapy = 100, (altura/2)
xInicial, yInicial = xFlapy, yFlapy
velocity = 0.5

tuberias = pygame.sprite.Group()
flapyBird = None
font = None
textVidas = None
xTuberia = random.randrange(100, anchura-100)

vidas = 3
xVidas, yVidas = 800, 100

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
    global flapyBirdImageHeight
    flapyBirdImage = pygame.image.load("flapyBird.png")
    flapyBirdImageHeight = flapyBirdImage.get_height()
    flapyBird = pygame.sprite.Sprite()
    flapyBird.image = flapyBirdImage
    flapyBird.rect = flapyBirdImage.get_rect()
    flapyBird.rect.x = xFlapy
    flapyBird.rect.y = yFlapy

def loadFont():
    global font
    global textVidas
    font = pygame.font.SysFont("comicsans", 50)
    textVidas = font.render("vidas: "+ str(vidas), False, (0, 0, 0))


def dibuja():
    window.blit(textVidas, (xVidas, yVidas))
    tuberias.draw(window)
    window.blit(flapyBird.image, (flapyBird.rect.x, flapyBird.rect.y))


def moveFlapyBird():
    global xFlapy, yFlapy

    key = pygame.key.get_pressed()

    xFlapy += velocity
    yFlapy += velocity 

    if key[pygame.K_SPACE]:
        yFlapy -= (0.25 * 10)

    flapyBird.rect.x = xFlapy
    flapyBird.rect.y = yFlapy

def colision():
    global vidas
    global xFlapy, yFlapy

    if (pygame.sprite.spritecollideany(flapyBird, tuberias)):
        vidas -= 1

        xFlapy, yFlapy = xInicial, yInicial

    if yFlapy == altura - flapyBirdImageHeight or yFlapy < 0 or xFlapy == anchura:
        xFlapy, yFlapy = xInicial, yInicial



def endGame():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            return True


    return False

loadFlapyBird()
loadObstaculos()
while not endGame():
    window.fill((0, 255, 255))

    moveFlapyBird()
    colision()

    loadFont()
    dibuja()
    pygame.display.flip()

