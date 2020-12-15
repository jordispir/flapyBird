import pygame
import random

pygame.init()
pygame.font.init()

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


def moveFlapyBird():
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
    if (pygame.sprite.spritecollideany(flapyBird, tuberias)):
        vidas -= 1


def endGame():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            return True
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
    pygame.display.flip()

