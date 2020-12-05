import pygame
import random

anchura, altura = 1200, 800
window = pygame.display.set_mode((anchura, altura))
out = False

xFlapy, yFlapy = 100, (altura/2)
velocity = 0.5


xTuberia = random.randrange(100, anchura-100)

vidas = 3


def loadObstaculos():
    tuberiaUp = pygame.image.load("tuberiaUp.png")
    tuberiaDown = pygame.image.load("tuberiaDown.png")

    blitObstaculos(tuberiaUp, tuberiaDown)

def blitObstaculos(tuberiaUp, tuberiaDown):

    alturaTuberia = tuberiaUp.get_height()
    anchuraTuberia = tuberiaUp.get_width()


    window.blit(tuberiaUp, (xTuberia, altura - alturaTuberia))
    window.blit(tuberiaDown, (0 + 100, 0))    
    
    colision(anchuraTuberia, alturaTuberia)

def loadFlapyBird():
    flapyBird = pygame.image.load("flapyBird.png")

    blitFlapyBird(flapyBird)

def blitFlapyBird(flapyBird):
    global xFlapy, yFlapy
    window.blit(flapyBird, (xFlapy,yFlapy))

    moveFlapyBird()

def moveFlapyBird():
    global xFlapy, yFlapy

    key = pygame.key.get_pressed()

    xFlapy += velocity
    yFlapy += velocity 

    if key[pygame.K_SPACE]:
        yFlapy -= (velocity * abs(velocity) * 10)

def colision(anchuraTuberia, alturaTuberia):
    global xFlapy, yFlapy, xTuberia, vidas

    if xFlapy > xTuberia and xFlapy < xTuberia + anchuraTuberia and yFlapy > (altura - alturaTuberia):
        vidas -= 1

    if vidas == vidas - 1:
        endGame()


def endGame():
   pass 

while not out:
    pygame.display.flip()
    window.fill((0, 255, 255))

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            out = True


    loadObstaculos()
    loadFlapyBird()
