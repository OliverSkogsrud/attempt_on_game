import pygame
import math
import time
import threading
import random
from typing import List
import sys, os
import os

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

transparent = (0, 0, 0, 0)
#variables

player_x = 300

points = 0

highscore = 0

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

pygame.mixer.music.load(os.path.join(application_path, "lavgutt.mp3"))

pygame.mixer.Channel(0).play(pygame.mixer.Sound((os.path.join(application_path, "lavgutt.mp3"))),loops=100000)

hp_value = 10
hp = pygame.font.Font(None,50)
hp_text = hp.render("Hp: "+ str(hp_value), False, "red")

high_font = pygame.font.Font(None,40)
high_text = high_font.render("highscore: " + str(highscore), False, "red")

test_font = pygame.font.Font(None, 50)#hvis jeg skal ha en font må jeg laste den ned og legge den til
text = test_font.render("score:  " + str(points), False, "red")
#images
#player
Player = pygame.image.load(os.path.join(application_path, "spaceship2.png"))
small_player = pygame.transform.scale(Player, (100,100))
player_rect = small_player.get_rect(center = (player_x,400))

#bullet


class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((50,50))     
        self.image.fill((0,255,0))   
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 4
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


def reset():
    global points
    global hp_value
    points = 0
    enemies.clear()
    hp_value = 10
    pygame.mixer.music.load(os.path.join(application_path, "death.wav"))
    pygame.mixer.music.play()

    


spawnenemy()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.load(os.path.join(application_path, "named.wav"))

                pygame.mixer.music.play()
                bullet = Bullet(player_x + 50, 500)
                bullets.append(bullet)
    player_rect.x = player_x
    player_rect.y = 500
    #enemy = Enemy(400,0),
    #enemies.append(enemy)


    screen.fill((0,75,200))

    for bullet in bullets:
        for enemy in enemies:
            if pygame.Rect.colliderect(bullet.rect, enemy.rect):
                pygame.mixer.music.load(os.path.join(application_path, "kill.wav"))
                pygame.mixer.music.set_volume(20.0)
                pygame.mixer.music.play()
                bullets.remove(bullet)
                enemies.remove(enemy)
                points += 1
                

        bullet.update()
        bullet.draw()

    
    for enemy in enemies:
        enemy.update()
        enemy.draw()
        if pygame.Rect.colliderect(enemy.rect, player_rect):
            enemies.remove(enemy)
            hp_value -= 1
        if enemy.rect.y >= 610:
            enemies.remove(enemy)
            hp_value -= 1 

    hp_text = hp.render("Hp: "+ str(hp_value),False, "red")
    text = test_font.render("score:  " + str(points), False, "red")
    high_text = high_font.render("highscore: " + str(highscore), False, "red")


    #movement and bullet
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 9

    if keys[pygame.K_RIGHT]:
        player_x += 9
    
    if hp_value <= 0:
        reset()

    if points >= highscore:
        highscore = points
        
    screen.blit(high_text, (600, 200))
    screen.blit(small_player, (player_x ,500))
    screen.blit(text,(400, 50))
    screen.blit(hp_text,(200,50))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()