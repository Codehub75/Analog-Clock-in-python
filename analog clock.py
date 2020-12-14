import pygame
import math
import datetime
pygame.init()

height = 600
width = 600

display = pygame.display.set_mode((width,height))

bg_color = (0,0,0)


def clock():
    now = datetime.datetime.today()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    sec_angle = 2*math.pi - (seconds*6*math.pi)/180 + math.pi/2
    min_angle = 2*math.pi - (minutes*6*math.pi)/180 + math.pi/2


    if hours >12:
        hours = hours%12
    hour_angle = 2*math.pi - (hours*30*math.pi)/180 + math.pi/2

    pygame.draw.arc(display,(0,0,255),[width/4,height/4,width/2,height/2],sec_angle,math.pi/2,7)
    pygame.draw.arc(display,(0,255,0),[12+width/4,12+height/4,-24+width/2,-24+height/2],min_angle,math.pi/2,7)
    pygame.draw.arc(display,(255,32,3),[24+width/4,24+height/4,-48+width/2,-48+height/2],hour_angle,math.pi/2,7)
    
    pygame.draw.line(display,(0,0,255),(width/2,height/2),(width/2 + 110*math.sin((seconds*6*math.pi)/180),height/2 - 110*math.cos((seconds*6*math.pi)/180)),7)
    pygame.draw.line(display,(0,255,0),(width/2,height/2),(width/2 + 90*math.sin((minutes*6*math.pi)/180),height/2 - 90*math.cos((minutes*6*math.pi)/180)),7)
    pygame.draw.line(display,(255,32,3),(width/2,height/2),(width/2 + 70*math.sin((hours*30*math.pi)/180),height/2 - 70*math.cos((hours*30*math.pi)/180)),7)

loop = True

while loop:
    display.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    clock()
    pygame.display.update()