import pygame
import sys
import os


'''
Objects
'''
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','ant' + str(i) + '.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

'''
Setup
'''

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
worldx = 960
worldy = 720
fps   = 40  # frame rate
ani   = 4   # animation cycles
clock = pygame.time.Clock()
pygame.init()

world    = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','background.png')).convert()
backdropbox = world.get_rect()

player = Player()

player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)

main = True

# put run-once code here

'''
Main Loop
'''
while main == True:
    world.blit(backdrop, backdropbox)
    pygame.display.flip()
    clock.tick(fps)
    player_list.draw(world)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
