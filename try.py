import pygame
import random

pygame.init()

clock = pygame.time.Clock()



image = pygame.image.load("tuberia.png")
image = pygame.transform.rotate(image, 180)


window = pygame.display.set_mode((1200, 800))

y = random.randrange(-image.get_height(), (800/2)- image.get_height())
print (y, image.get_height())
birdSprite = [pygame.image.load('menumenuSprites/1.png'), pygame.image.load('menumenuSprites/1.png'), pygame.image.load('menumenuSprites/1.png'), pygame.image.load('menumenuSprites/1.png'), pygame.image.load('menumenuSprites/1.png'),
              pygame.image.load('menumenuSprites/2.png'),pygame.image.load('menumenuSprites/2.png'), pygame.image.load('menumenuSprites/2.png'), pygame.image.load('menumenuSprites/2.png'), pygame.image.load('menumenuSprites/2.png'),
              pygame.image.load('menumenuSprites/3.png'), pygame.image.load('menumenuSprites/3.png'), pygame.image.load('menumenuSprites/3.png'), pygame.image.load('menumenuSprites/3.png'), pygame.image.load('menumenuSprites/3.png'),
              pygame.image.load('menumenuSprites/4.png'), pygame.image.load('menumenuSprites/4.png'), pygame.image.load('menumenuSprites/4.png'), pygame.image.load('menumenuSprites/4.png'), pygame.image.load('menumenuSprites/4.png'),
              pygame.image.load('menumenuSprites/5.png'), pygame.image.load('menumenuSprites/5.png'), pygame.image.load('menumenuSprites/5.png'), pygame.image.load('menumenuSprites/5.png'), pygame.image.load('menumenuSprites/5.png'),
              pygame.image.load('menumenuSprites/6.png'), pygame.image.load('menumenuSprites/6.png'), pygame.image.load('menumenuSprites/6.png'), pygame.image.load('menumenuSprites/6.png'), pygame.image.load('menumenuSprites/6.png'),
              pygame.image.load('menumenuSprites/7.png'), pygame.image.load('menumenuSprites/7.png'), pygame.image.load('menumenuSprites/7.png'), pygame.image.load('menumenuSprites/7.png'), pygame.image.load('menumenuSprites/7.png'),
              pygame.image.load('menumenuSprites/8.png'), pygame.image.load('menumenuSprites/8.png'), pygame.image.load('menumenuSprites/8.png'), pygame.image.load('menumenuSprites/8.png'), pygame.image.load('menumenuSprites/8.png')]

    
count = 0

out = False
while not out:
    event = pygame.event.poll()
    window.fill((255, 0, 0))

    window.blit(image, (0, y) )
    window.blit(birdSprite[count], (400, 200))
    count += 1

    clock.tick(30)
    if count == 40:
        count = 0

    print (clock.get_fps())
        
    if event.type == pygame.QUIT:
        out = True

    pygame.display.flip()

