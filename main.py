import pygame
import random

pygame.init()
pygame.font.init()

fps = pygame.time.Clock()
fps.tick(30)

anchura, altura = 1200, 800 
window = pygame.display.set_mode((anchura, altura))

tuberias = pygame.sprite.Group()

global out
global activaMenu
out = False
activaMenu = False

class creaTuberia:
    def __init__(self):
        
        self.xTuberiaUp = anchura - 100
        self.yTuberiaUp = random.randrange(altura/2, altura)
        tuberia = pygame.image.load("tuberia.png")
        self.tuberiaUpSprite = pygame.sprite.Sprite()
        self.tuberiaUpSprite.image = tuberia
        self.tuberiaUpSprite.rect = tuberia.get_rect()
        self.tuberiaUpSprite.rect.x = self.xTuberiaUp 
        self.tuberiaUpSprite.rect.y = self.yTuberiaUp

        self.tuberiaHeight = tuberia.get_height()

        self.xTuberiaDown = anchura - 100
        self.yTuberiaDown = random.randrange(-500, 0)
        tuberiaDown = pygame.transform.rotate(tuberia, 180)
        self.tuberiaDownSprite = pygame.sprite.Sprite()
        self.tuberiaDownSprite.image = tuberiaDown
        self.tuberiaDownSprite.rect = tuberiaDown.get_rect()
        self.tuberiaDownSprite.rect.x = self.xTuberiaDown 
        self.tuberiaDownSprite.rect.y = self.yTuberiaDown

        tuberias.add(self.tuberiaDownSprite)
        tuberias.add(self.tuberiaUpSprite)

        self.count = 0
        self.velocity = 2

        self.diferencia = 100

    def dibuja(self):
        tuberias.draw(window)

    def update(self):
        self.tuberiaDownSprite.rect.x -= self.velocity
        self.tuberiaUpSprite.rect.x -= self.velocity

        if self.tuberiaDownSprite.rect.x < 0:
            self.tuberiaDownSprite.rect.x = anchura
            pos1 = random.randrange(-self.tuberiaHeight, (altura/2) - self.tuberiaHeight) #TODO optimizar 
            self.tuberiaDownSprite.rect.y = pos1

            self.count += 1

        if self.tuberiaUpSprite.rect.x < 0:
            self.tuberiaUpSprite.rect.x = anchura
            pos2 = random.randrange(altura/2, altura - 100) 

            self.diferencia = (pos2) - (pos1 + self.tuberiaHeight)

            print (self.diferencia)

            if self.diferencia < 100:
                pos2 += 100

            self.tuberiaUpSprite.rect.y = pos2 

        if self.count == 5:
            self.velocity += 2
            if self.velocity == 10:
                self.velocity = 2
            self.count = 0

        #print (self.count, self.tuberiaDownSprite.rect.x, self.tuberiaUpSprite.rect.x)

class flapyBird:
    def __init__(self):
        self.xFlapy, self.yFlapy = 100, (altura/2)
        self.xInicial, self.yInicial = self.xFlapy, self.yFlapy
        flapyBirdImage = pygame.image.load("left/1.png")
        self.birdSpriteLeft = [pygame.image.load('left/1.png'), pygame.image.load('left/1.png'), pygame.image.load('left/1.png'), pygame.image.load('left/1.png'), pygame.image.load('left/1.png'),
              pygame.image.load('left/2.png'),pygame.image.load('left/2.png'), pygame.image.load('left/2.png'), pygame.image.load('left/2.png'), pygame.image.load('left/2.png'),
              pygame.image.load('left/3.png'), pygame.image.load('left/3.png'), pygame.image.load('left/3.png'), pygame.image.load('left/3.png'), pygame.image.load('left/3.png'),
              pygame.image.load('left/4.png'), pygame.image.load('left/4.png'), pygame.image.load('left/4.png'), pygame.image.load('left/4.png'), pygame.image.load('left/4.png'),
              pygame.image.load('left/5.png'), pygame.image.load('left/5.png'), pygame.image.load('left/5.png'), pygame.image.load('left/5.png'), pygame.image.load('left/5.png'),
              pygame.image.load('left/6.png'), pygame.image.load('left/6.png'), pygame.image.load('left/6.png'), pygame.image.load('left/6.png'), pygame.image.load('left/6.png'),
              pygame.image.load('left/7.png'), pygame.image.load('left/7.png'), pygame.image.load('left/7.png'), pygame.image.load('left/7.png'), pygame.image.load('left/7.png'),
              pygame.image.load('left/8.png'), pygame.image.load('left/8.png'), pygame.image.load('left/8.png'), pygame.image.load('left/8.png'), pygame.image.load('left/8.png')]
        self.birdSpriteRight = [pygame.image.load('right/1.png'), pygame.image.load('right/1.png'), pygame.image.load('right/1.png'), pygame.image.load('right/1.png'), pygame.image.load('right/1.png'),
              pygame.image.load('right/2.png'),pygame.image.load('right/2.png'), pygame.image.load('right/2.png'), pygame.image.load('right/2.png'), pygame.image.load('right/2.png'),
              pygame.image.load('right/3.png'), pygame.image.load('right/3.png'), pygame.image.load('right/3.png'), pygame.image.load('right/3.png'), pygame.image.load('right/3.png'),
              pygame.image.load('right/4.png'), pygame.image.load('right/4.png'), pygame.image.load('right/4.png'), pygame.image.load('right/4.png'), pygame.image.load('right/4.png'),
              pygame.image.load('right/5.png'), pygame.image.load('right/5.png'), pygame.image.load('right/5.png'), pygame.image.load('right/5.png'), pygame.image.load('right/5.png'),
              pygame.image.load('right/6.png'), pygame.image.load('right/6.png'), pygame.image.load('right/6.png'), pygame.image.load('right/6.png'), pygame.image.load('right/6.png'),
              pygame.image.load('right/7.png'), pygame.image.load('right/7.png'), pygame.image.load('right/7.png'), pygame.image.load('right/7.png'), pygame.image.load('right/7.png'),
              pygame.image.load('right/8.png'), pygame.image.load('right/8.png'), pygame.image.load('right/8.png'), pygame.image.load('right/8.png'), pygame.image.load('right/8.png')]
        self.flapyBirdImageHeight = flapyBirdImage.get_height()
        self.flapyBirdImageWidth= flapyBirdImage.get_width()
        self.flapyBird = pygame.sprite.Sprite()
        self.flapyBird.image = self.birdSpriteRight
        self.flapyBird.rect = flapyBirdImage.get_rect()
        self.flapyBird.rect.x = self.xFlapy
        self.flapyBird.rect.y = self.yFlapy

        self.jump = False
        self.velocity = 1
        self.count = 0

    def dibuja(self):
        window.blit(self.birdSpriteRight[self.count], (self.xFlapy, self.yFlapy))
        self.count += 1

        if self.count == 40:
            self.count = 0

    def move_flapyBird(self):
        key = pygame.key.get_pressed()

        self.yFlapy += self.velocity 

        if key[pygame.K_SPACE]:
            self.yFlapy -= (self.velocity/2 * 5)

        self.flapyBird.rect.y = self.yFlapy

    def colision(self, vidas):
        if (pygame.sprite.spritecollideany(self.flapyBird, tuberias)):
            self.xFlapy, self.yFlapy = self.xInicial, self.yInicial #rect.x para colisiones con otros menuSprites.
            vidas.vidas -= 1

        elif self.yFlapy > altura - self.flapyBirdImageHeight:
            self.xFlapy, self.yFlapy = self.xInicial, self.yInicial
            vidas.vidas -= 1

        elif self.yFlapy < 0: 
            self.xFlapy, self.yFlapy = self.xInicial, self.yInicial
            vidas.vidas -= 1

        elif self.xFlapy > anchura - self.flapyBirdImageWidth:
            self.xFlapy, self.yFlapy = self.xInicial, self.yInicial
            vidas.vidas -= 1

class endGame:
    def __init__(self):
        self.xVidas, self.yVidas = anchura - 200, 50
        self.vidas = 3
        self.font = pygame.font.SysFont("comicsans", 50)
        self.textVidas = self.font.render("vidas: "+ str(self.vidas), False, (0, 0, 0))
    
    
    def update(self):
        self.textVidas = self.font.render("vidas: "+ str(self.vidas), False, (0, 0, 0))

    def dibuja(self):
        window.blit(self.textVidas, (self.xVidas, self.yVidas))

    def out(self):
        global activaMenu
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    activaMenu = True

        if self.vidas == 0:
            pass #Condición correcta.
        
        if out:
            return True

        return False

class menu:
    def __init__(self):
        self.Count = 0
        self.bg = pygame.image.load("menuBg.png")
        self.uso = pygame.image.load("uso.png")
        self.font = pygame.font.SysFont("fugazone", 80)
        self.titulo = self.font.render("Flapy Bird", False, (0, 0 , 0))
        self.jugar = self.font.render("Jugar", False, (0, 0, 0))
        self.salir = self.font.render("Salir", False, (0, 0, 0))
        self.birdSprite = [pygame.image.load('menuSprites/1.png'), pygame.image.load('menuSprites/1.png'), pygame.image.load('menuSprites/1.png'), pygame.image.load('menuSprites/1.png'), pygame.image.load('menuSprites/1.png'),
              pygame.image.load('menuSprites/2.png'),pygame.image.load('menuSprites/2.png'), pygame.image.load('menuSprites/2.png'), pygame.image.load('menuSprites/2.png'), pygame.image.load('menuSprites/2.png'),
              pygame.image.load('menuSprites/3.png'), pygame.image.load('menuSprites/3.png'), pygame.image.load('menuSprites/3.png'), pygame.image.load('menuSprites/3.png'), pygame.image.load('menuSprites/3.png'),
              pygame.image.load('menuSprites/4.png'), pygame.image.load('menuSprites/4.png'), pygame.image.load('menuSprites/4.png'), pygame.image.load('menuSprites/4.png'), pygame.image.load('menuSprites/4.png'),
              pygame.image.load('menuSprites/5.png'), pygame.image.load('menuSprites/5.png'), pygame.image.load('menuSprites/5.png'), pygame.image.load('menuSprites/5.png'), pygame.image.load('menuSprites/5.png'),
              pygame.image.load('menuSprites/6.png'), pygame.image.load('menuSprites/6.png'), pygame.image.load('menuSprites/6.png'), pygame.image.load('menuSprites/6.png'), pygame.image.load('menuSprites/6.png'),
              pygame.image.load('menuSprites/7.png'), pygame.image.load('menuSprites/7.png'), pygame.image.load('menuSprites/7.png'), pygame.image.load('menuSprites/7.png'), pygame.image.load('menuSprites/7.png'),
              pygame.image.load('menuSprites/8.png'), pygame.image.load('menuSprites/8.png'), pygame.image.load('menuSprites/8.png'), pygame.image.load('menuSprites/8.png'), pygame.image.load('menuSprites/8.png')]
        
        self.xFlapy, self.yFlapy = 300, 325
        self.xTitulo, self.yTitulo = 400, 100
        self.xJugar, self.yJugar = 600, 300 
        self.xSalir, self.ySalir = 600, 500 

        self.UP = True 
        self.DOWN = False

        self.play = False

    def dibuja(self):
        window.blit(self.bg, (0, 0))
        window.blit(self.uso, (50, altura - 100))
        window.blit(self.titulo, (self.xTitulo, self.yTitulo))
        window.blit(self.jugar, (self.xJugar, self.yJugar))
        window.blit(self.salir, (self.xSalir, self.ySalir))
        window.blit(self.birdSprite[self.Count], (self.xFlapy, self.yFlapy))

        self.Count += 1

        if self.Count == 40:
            self.Count = 0
    
    def opcion(self):
        global out
        global activaMenu
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.yFlapy = self.ySalir
                    self.DOWN = True
                    self.UP = False
                
                elif event.key == pygame.K_UP:
                    self.yFlapy = self.yJugar
                    self.UP = True
                    self.DOWN = False

                elif event.key == pygame.K_RETURN and self.DOWN:
                    out = True
                    #return?

                elif event.key == pygame.K_RETURN and self.UP:
                    self.play = True
                    activaMenu = False

                elif event.key == pygame.K_RETURN and self.yFlapy == self.yJugar:
                    self.play = True
                    activaMenu = False
                    
                    
tuberia = creaTuberia()
flapy = flapyBird()
end = endGame()
menu = menu()
opcion = menu.opcion()

while not end.out():
    window.fill((0, 255, 255))

    if menu.play and not(activaMenu):
        tuberia.update()
        tuberia.dibuja()
        flapy.move_flapyBird()
        flapy.dibuja()
        flapy.colision(end) #parámetro end para utilizar sus atributos.
        end.update()
        end.dibuja()
    else:
        menu.dibuja()
        menu.opcion()
    
    pygame.display.flip()

