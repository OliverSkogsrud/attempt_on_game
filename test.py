import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0,50,220))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)#hvis jeg skal ha en font må jeg laste den ned og legge den til
Player = pygame.image.load("spaceship.jpg")
small_player = pygame.transform.scale(Player, (100,100))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(small_player, (300,400))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)