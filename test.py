import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("game")

clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 50)#hvis jeg skal ha en font må jeg laste den ned og legge den til
#images
Player = pygame.image.load("spaceship.jpg")
small_player = pygame.transform.scale(Player, (100,100))
bullet = pygame.image.load("bullet_pixel.png")


player_x = 300

running = True

while running:
    screen.fill((0,50,220))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += 25
            if event.key == pygame.K_LEFT:
                player_x -= 25
            if event.key == pygame.K_SPACE:
                
    
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
        #player_x + 1
        #print("pressed space")
    
    
    screen.blit(small_player, (player_x ,400))
    
    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)