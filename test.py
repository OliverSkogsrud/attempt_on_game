import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("game")

clock = pygame.time.Clock()

transparent = (0, 0, 0, 0)
#variables
player_x = 300
bullet_y = 400
  

test_font = pygame.font.Font(None, 50)#hvis jeg skal ha en font må jeg laste den ned og legge den til
#images
#player
Player = pygame.image.load("spaceship.jpg")
small_player = pygame.transform.scale(Player, (100,100))
player_rect = small_player.get_rect(topleft = (player_x,400))
#bullet
bullet = pygame.image.load("bullet_pixel.png")
small_bullet = pygame.transform.scale(bullet, (50,50))
bullet_rect = small_bullet.get_rect(topleft = (player_x, bullet_y))
bullet_copy = small_bullet.copy()
bullet_copy_rect = bullet_copy.get_rect(topleft = (player_x, 400))

        

running = True

while running:
    screen.fill((0,75,220))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Movement
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                bullet_rect.y -= 200
                if bullet_rect.y <= -10 and event.key == pygame.K_SPACE: 
                    
                    bullet_copy_rect.y -= 100
                
             
            
    
    
    #movement and bullet
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        screen.blit(small_bullet, bullet_rect)
        screen.blit(bullet_copy, bullet_copy_rect)
        screen.blit(small_bullet, (player_x, bullet_y))
        while True:
            bullet_copy_rect.y += 10
            if bullet_copy_rect.y <= -100:
                bullet_copy_rect.y == 400
                bullet_rect.x == player_x
        
   
        

    if keys[pygame.K_LEFT]:
        player_x -= 7

    if keys[pygame.K_RIGHT]:
        player_x += 7
            

        
        
    
    screen.blit(small_player, (player_x ,400))
    
    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)

