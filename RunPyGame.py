import pygame
from pygame.locals import *
from sys import exit
import numpy as np
import math
import random

pygame.init()
screen = pygame.display.set_mode((1200, 600))



global point_count, points, radius, slider_pos
slider_pos = (20, 20)
point_count = 0
points = []
radius = 6


add_button = pygame.Surface((20, 20))
add_button.fill((0, 255, 0))

sub_button = pygame.Surface((20, 20))
sub_button.fill((255, 0, 0))


def main():
    global point_count, points, radius, slider_pos
    point_count = 3
    points = [(30, 30), (100, 100), (30, 200)]
    point_selected = -1
    run = True

    #pygame loop
    while run:
        mouse_pos = pygame.mouse.get_pos()
            
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #check if clicking on a draggable point, if so, start dragging that point
                for i in range(len(points)):
                    if within(pygame.mouse.get_pos(), points[i]) and point_selected == -1:
                        point_selected = i
                        #print("selecting " + str(point_selected))
                    if point_selected >= 0:
                        points[point_selected] = mouse_pos
                #Work in progress slider
                if within(mouse_pos, slider_pos):
                    pass
            #checks if one of the interactable buttons were clicked. 
            elif event.type == pygame.MOUSEBUTTONUP:
                point_selected = -1;
                if add_button.get_rect().collidepoint((mouse_pos[0] - 20, mouse_pos[1] - 500)):
                    #print(point_count)
                    point_count += 1
                    update_points()
                if sub_button.get_rect().collidepoint((mouse_pos[0] - 20, mouse_pos[1] - 535)):
                    point_count -= 1
                    update_points()
                    
                
            elif event.type == pygame.MOUSEMOTION:
                if point_selected >= 0:
                    points[point_selected] = pygame.mouse.get_pos()

                
                

        #check if need to add or subtract points from the screen
        if point_count != len(points):
            update_points()

        #drawing objects
        screen.fill((255, 255, 255))
        screen.blit(add_button, (20, 500))
        screen.blit(sub_button, (20, 535))

        for p in points:
            pygame.draw.circle(screen, (0), p, radius)

        # determines the amount of 'in between points' to make the illusion of a line.
        for t in np.arange(0, 1, 0.001):
            px = 0
            py = 0

            # calculates the position the point should be on according to the Bezier curve formula
            for i in range(len(points)):
                t_coeff = i
                binomial_coeff = math.comb(len(points) - 1, i)
                px += binomial_coeff * points[i][0]*((1-t)**(len(points) - 1 - t_coeff))*(t**t_coeff)
                py += binomial_coeff * points[i][1]*((1-t)**(len(points) - 1 - t_coeff))*(t**t_coeff)
            #px = p0[0]*(1-t)**2 + 2*(1-t)*t*p1[0] + p2[0]*t**2
            
            #py = p0[1]*(1-t)**2 + 2*(1-t)*t*p1[1] + p2[1]*t**2       
            pygame.draw.circle(screen, (250, 0, 0), (px, py), 4)

        pygame.display.update()
    print(run)
    
# adds or subtracts points if needed
def update_points():
    global point_count, points
    print(point_count)
    while point_count > len(points):
        newPoint = (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))
        points.append(newPoint)
        #print(points)
    while point_count < len(points):
        points.pop(-1)
    
"""
    if point_count > len(points):
        points.append((250, 250))
    elif point_count < len(points):
        points.remove(len(points) - 1)
   """ 

#check if mousePos is within a certain radius
def within(mousePos, circlePos):
    global radius
    distance = (int(mousePos[0]) - int(circlePos[0])) ** 2 + (int(mousePos[1]) - int(circlePos[1])) ** 2
    distance = math.sqrt(distance)
    #print(distance < radius)
    return distance < radius

        
if __name__ == '__main__':
    print('test')
    main()
