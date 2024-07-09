import pygame
from pygame.locals import *
from sys import exit
import numpy as np
import math

pygame.init()
screen = pygame.display.set_mode((1200, 600))




def main():
    point_count = 3
    points = [(30, 30), (100, 100), (30, 200)]
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("down")
                
                

        if point_count != len(points):
            update_points()

        
        #p0 = 30,30
    
        points[1] = pygame.mouse.get_pos()
        #p2 = 30,190
    
        screen.fill((255, 255, 255))
        #pygame.draw.circle(screen, (0), )
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

        
if __name__ == '__main__':
    print('test')
    main()
