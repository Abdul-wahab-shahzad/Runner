from sys import exit
from turtle import clear
from numpy import size
import pygame

pygame.init() # at first always intialize this function
screen=pygame.display.set_mode((800,400))  # setting the screen size it takes (width,height)
pygame.display.set_caption("First Game")   # name of the Game
text_font=pygame.font.Font('graphics/pixelart.ttf',50)  # text on screen  (style and size)
clock=pygame.time.Clock() # setting the clock speed

sky_size=(800,300)   # size of the sky surface
ground_size=(900,100)  # sizel of the ground
test_surface=pygame.image.load('graphics/sky.png')  # loading image of sky or you can use fill for color
test_surface=pygame.transform.scale(test_surface,sky_size)  # scaling the image
ground_surface=pygame.image.load('graphics/ground.png')
ground_surface=pygame.transform.scale(ground_surface,ground_size)
enemy_surface=pygame.image.load('graphics/enemy_1.png')
enemy_surface=pygame.transform.scale(enemy_surface,(50,50))
text_surface=text_font.render('My game',False,'blue') # rendering text on surface
player_surface=pygame.image.load('graphics/player_1.jpg').convert_alpha()
player_rect=player_surface.get_rect(midbottom=(50,325))
enemy_rect=enemy_surface.get_rect(midbottom=(700,325))

while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface,(0,0))  # blit is used to display surfaces on screen
    screen.blit(ground_surface,(-65,300))
    screen.blit(text_surface,(200,50))

    screen.blit(player_surface,player_rect)
    player_rect.left +=1
    enemy_rect.right-=1
    if enemy_rect.right==0:
        enemy_rect.right=800
    screen.blit(player_surface,player_rect)
    screen.blit(enemy_surface,enemy_rect)  
    if player_rect.colliderect(enemy_rect):
        print("coliison")
    pygame.display.update()  
    clock.tick(60)
