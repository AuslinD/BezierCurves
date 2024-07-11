import pygame
from pygame.locals import *
from sys import exit
import numpy as np
import math

pygame.init()
screen = pygame.display.set_mode((1200, 600))

global point_count, points
point_count = 0
points = []

def main():
    point_count = 3
    points = [(30, 30), (100, 100), (30, 200)]
    point_selected = -1
    run = True
    while run:
        
            
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(points)):
                    if within(pygame.mouse.get_pos(), points[i]) and point_selected == -1:
                        point_selected = i
                        print("selecting " + str(point_selected))
                    if point_selected >= 0:
                        points[point_selected] = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                point_selected = -1;
            elif event.type == pygame.MOUSEMOTION:
                if point_selected >= 0:
                    points[point_selected] = pygame.mouse.get_pos()

                
                

        #if point_count != len(points):
            #update_points()

        
        #p0 = 30,30
    
        #points[1] = pygame.mouse.get_pos()
        #p2 = 30,190
    
        screen.fill((255, 255, 255))
        #pygame.draw.circle(screen, (0), )
        if point_count != len(points):
            update_points()

        
        for p in points:
            pygame.draw.circle(screen, (0), p, 5)
        for t in np.arange(0, 1, 0.01):
            px = 0
            py = 0
            
            for i in range(point_count):
               t_coeff = i
               binomial_coeff = math.comb(point_count - 1, i)
               px += binomial_coeff * points[i][0]*((1-t)**(point_count - 1 - t_coeff))*(t**t_coeff)
               py += binomial_coeff * points[i][1]*((1-t)**(point_count - 1 - t_coeff))*(t**t_coeff)
            #px = p0[0]*(1-t)**2 + 2*(1-t)*t*p1[0] + p2[0]*t**2
            
            #py = p0[1]*(1-t)**2 + 2*(1-t)*t*p1[1] + p2[1]*t**2       
            pygame.draw.circle(screen, (0, 0, 0), (px, py), 4)

        pygame.display.update()
    print(run)
    

def update_points():
    if point_count > len(points):
        points.append((50, 50))
    elif point_count < len(points):
        points.remove(len(points) - 1)
    

def within(mousePos, circlePos):
    radius = 5
    distance = (int(mousePos[0]) - int(circlePos[0])) ** 2 + (int(mousePos[1]) - int(circlePos[1])) ** 2
    distance = math.sqrt(distance)
    print(distance < radius)
    return distance < radius

        
if __name__ == '__main__':
    print('test')
    main()
