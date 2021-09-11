import pygame
import random
import sys
from pygame import mixer




red = (255,0,0)
green=(0,255,0)
blue=(0,0,255)
black= (0,0,0)
white=(255,255,255)

wdt = 550
ht=600
fps = 30
exti_game = False
game_over=False
snake_x=150
snake_y=150
snake_size=10
fd_x=random.randint(0,wdt)
fd_y=random.randint(0,wdt)
fd_size=10
score=0
snake_list= []
snake_length=1



vel_x=0
vel_y=0


pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((wdt,ht))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()


def mytext(text,color,x,y):
    font= pygame.font.SysFont('arial',25)
    screentext=font.render(text,True,color)
    win.blit(screentext,(x,y))

def plotsnake(window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(window,color,(x,y,snake_size,snake_size))    

while not exti_game:

    if game_over:
        win.fill(white)
        mytext("GAME OVER    "+ str(score),red,170,90)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exti_game = True

        clock.tick(fps)
        pygame.display.update()
           

    else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exti_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        vel_y=-5
                        vel_x=0

                    if event.key == pygame.K_DOWN:
                        vel_y=5
                        vel_x=0

                    if event.key == pygame.K_LEFT:
                        vel_y=0
                        vel_x=-5   

                    if event.key == pygame.K_RIGHT:
                        vel_y=0
                        vel_x=5          

            
            snake_x=snake_x+vel_x
            snake_y=snake_y+vel_y

            if abs(snake_x-fd_x)<10 and abs(snake_y-fd_y)<10:
                score=score+10
                
                fd_x=random.randint(0,wdt-50)
                fd_y=random.randint(0,wdt-50)
                snake_length=snake_length+5

            head=[]
            head.append(snake_x)   
            head.append(snake_y)    
            snake_list.append(head) 

            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True

            if snake_x <0 or snake_x>wdt or snake_y<0 or snake_y>ht:
                game_over=True        

            win.fill(black)
            mytext("Score : "+str(score),white,5,5)
            plotsnake(win,green,snake_list,snake_size)
            pygame.draw.rect(win,red,(fd_x,fd_y,fd_size,fd_size))
            clock.tick(fps)
            pygame.display.update()


pygame.quit()
quit() 

