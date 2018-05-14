import pygame
import sys
import os
import timeit
import random


'''
Objects
'''
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.timeExisting = 0

        self.image= pygame.image.load(os.path.join('images','apple.png'))
        self.rect = self.image.get_rect()

    def placeApple(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []

        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','ant' + str(i) + '.png'))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self,x,y):
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        #left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
        #right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
        #up
        if self.movey < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
        #down
        if self.movey > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

'''
Setup
'''

worldx = 960
worldy = 720

fps = 40
ani = 4
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','background.png')).convert()
backdropbox = world.get_rect()

player = Player()
apple = Apple()

apple.placeApple(random.randint(10, worldx-10), random.randint(10,worldy-10))

player.rect.x = 0
player.rect.y = 0

player_list = pygame.sprite.Group()
player_list.add(player)
player_list.add(apple)

stepsx = 10
stepsy = 10
main = True

'''
Main Loop
'''

while main == True:
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    player.update()
    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-stepsx,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(stepsx,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -stepsy)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, stepsy)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(stepsx,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-stepsx,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, stepsy)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -stepsy)

            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
