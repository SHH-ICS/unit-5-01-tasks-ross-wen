# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

pygame.init()

gameDisplay = display.set_mode(SCREEN_SIZE)

gameDisplay.fill(Color('lightblue'))

draw.rect(gameDisplay, Color('white'), Rect( 100,  350, 50, 50))
draw.polygon(gameDisplay, Color('red'), [(100, 350), (150, 350), (125, 300)])

draw.rect(gameDisplay, Color('green'), Rect(0, 400, 500, 100))

draw.circle(gameDisplay, Color('yellow'), (50, 50), 50)

display.flip()

input("Press enter to exit")
