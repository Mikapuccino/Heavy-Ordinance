import pygame
from pygame.image import load
from pygame.math import Vector2
from pygame import Color

# This file is used for additional useful functions used in the game

# This function loads the proper sprite for each object,
# also removing transparent spaces in the image

def load_sprite(name, withAlpha = True):

    path = f"{name}.png"
    loadedSprite = load(path)

    if withAlpha:

        return loadedSprite.convert_alpha()

    else:

        return loadedSprite.convert()

# This function is used to display text in the center of the screen

def text(surface, text, font, color=Color("white")):

    checkText = text.strip()
    textSurface = font.render(checkText, True, color)
    rect = textSurface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(textSurface, rect)

# This function is used to display text on the screen
# at a specific height and in the middle of the screen's width 

def text_in_line(surface, text, font, pos, color=Color("white")):

    checkText = text.strip()
    textSurface = font.render(checkText, True, color)
    rect = textSurface.get_rect()
    rect.center = Vector2(500, pos)

    surface.blit(textSurface, rect)

# This function is used to display text in a specific position on the screen

def text_in_pos(surface, text, font, pos, color=Color("black")):

    checkText = text.strip()
    textSurface = font.render(checkText, True, color)
    rect = textSurface.get_rect()
    rect.center = Vector2(pos[0], pos[1])

    surface.blit(textSurface, rect)