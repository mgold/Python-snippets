"""
Angles in Pygame
A demonstration by Max Goldstein, Tufts University '14

In pygame, +y is down. Python's arctangent functions expect +y to be up.
This wreaks havoc with the unit circle if you want to find the angle between
two points (for, say, collision detection or aiming a gun).

Note that math.atan2(numerator, denominator) does the division for you.

This applet demonstrates the confusing result. The range of the arctangent
(-pi, pi], which is mathematically accurate but hard to work with. Much worse
is that the  direction of increasing angular measure is reversed!

You can avoid the problem entirely by calling atan2(-y, x) and adding 2*pi to
the result if it's negative.

Controls: move the mouse near the axes.

"""

import pygame, sys, os
from pygame.locals import *
from math import atan2, degrees, pi
halfpi = pi/2.0

def quit():
    pygame.quit()
    sys.exit()

pygame.init()
screenDimensions = (400, 600)
window = pygame.display.set_mode(screenDimensions)
pygame.display.set_caption('Angles in Pygame')
screen = pygame.display.get_surface() 

clock = pygame.time.Clock()
FPS = 50
time_passed = 0

pos = (200, 200)
origin = (200, 200)

white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0)
blue  = (0, 0, 255)
purple= (200, 0, 200)
green = (0, 200, 0)

font = pygame.font.Font(None, 30)

arcRect = pygame.Rect(180, 180, 40, 40)

#Game loop
while True:
    time_passed = clock.tick(FPS)

    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
        elif event.type == MOUSEMOTION:
            if 0 < event.pos[0] < 400 and 0 < event.pos[1] < 400:
                pos = event.pos

    x = pos[0] - origin[0]
    y = pos[1] - origin[1]
    theta = atan2(y,x)

    screen.fill(white)

    pygame.draw.circle(screen, black, origin, 5)
    pygame.draw.line(screen, black, (0, 440), (440, 440), 3)
    pygame.draw.line(screen, black, (200, 15), (200, 380))
    screen.blit(font.render("-pi/2", True, black), (180,10))
    screen.blit(font.render( "pi/2", True, black), (187, 380))
    pygame.draw.line(screen, black, (10, 200), (355, 200))
    screen.blit(font.render("-pi", True, black), (5,  180))
    screen.blit(font.render( "pi", True, black), (12, 200))
    screen.blit(font.render("0", True, black), (360, 190))

    pygame.draw.line(screen, blue, origin, (pos[0], origin[1]), 2)
    pygame.draw.line(screen, red, (pos[0], origin[1]), (pos[0], pos[1]), 2)
    pygame.draw.line(screen, purple, origin, pos, 2)
    if theta < 0:
        pygame.draw.arc(screen, green, arcRect, 0, -theta, 4)
    else:
        pygame.draw.arc(screen, green, arcRect, -theta, 0, 4)

    screen.blit(font.render(str(x)+" x", True, blue), (10, 450))
    screen.blit(font.render(str(y)+" y", True, red), (100, 450))
    screen.blit(font.render(str((x**2 + y**2)**.5)+" d", True, purple), (10, 480))
    screen.blit(font.render("arctangent(y/x) =", True, black), (10, 510))
    screen.blit(font.render(str(degrees(theta))+" deg", True, green), (30, 540))
    screen.blit(font.render(str(theta/pi)+"*pi rad", True, green), (30, 570))

    pygame.display.flip() 