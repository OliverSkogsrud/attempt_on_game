import pygame
import math
import time
import threading
import random
from typing import List

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("game")

clock = pygame.time.Clock()

transparent = (0, 0, 0, 0)
#variables
player_x = 300

points = 0


test_font = pygame.font.Font(None, 50)#hvis jeg skal ha en font må jeg laste den ned og legge den til
text = test_font.render(str(points), False, "red")
#images
#player
Player = pygame.image.load("spaceship.jpg")
small_player = pygame.transform.scale(Player, (100,100))
player_rect = small_player.get_rect(topleft = (player_x,400))
#bullet



class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((50,50))     
        self.image.fill((0,255,0))   
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 3
        self.angle = 300
        self.dx = self.speed * math.cos(self.angle) 
        self.dy = -self.speed * math.sin(self.angle)
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
    
    def draw(self):
        screen.blit(self.image, self.rect)

enemies: List[Enemy] = list()

class Bullet:
    def __init__(self,x,y):
        self.image = pygame.Surface((10,20))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 5
        self.angle = -300
        self.dx = self.speed * math.cos(self.angle) 
        self.dy = -self.speed * math.sin(self.angle)


    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self):
        screen.blit(self.image, self.rect)

bullets: List[Bullet] = list()


running = True

def spawnenemy():
    enemy = Enemy(random.randint(0,800),0)
    enemies.append(enemy)
    if running:
        threading.Timer(1.0, spawnenemy).start()



spawnenemy()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.load("named.wav")
                
                pygame.mixer.music.play()
                bullet = Bullet(player_x, 400)
                bullets.append(bullet)
  
    #enemy = Enemy(400,0),
    #enemies.append(enemy)

    screen.fill((0,75,220))

    for bullet in bullets:
        for enemy in enemies:
            if pygame.Rect.colliderect(bullet.rect, enemy.rect):
                pygame.mixer.music.load("kill.wav")
                pygame.mixer.music.play()
                bullets.remove(bullet)
                enemies.remove(enemy)
                points += 1
                text = test_font.render(str(points), False, "red")
        bullet.update()
        bullet.draw()

    for enemy in enemies:
        enemy.update()
        enemy.draw()   


    #movement and bullet
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 7

    if keys[pygame.K_RIGHT]:
        player_x += 7
    

    screen.blit(small_player, (player_x ,400))
    screen.blit(text,(400, 50))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()