import pygame
from pygame.image import load
from pygame.math import Vector2
from pygame import Color

def load_sprite(name, withAlpha = True):

    path = f"{name}.png"
    loadedSprite = load(path)

    if withAlpha:

        return loadedSprite.convert_alpha()

    else:

        return loadedSprite.convert()

def text(surface, text, font, color=Color("white")):

    checkText = text.strip()
    textSurface = font.render(checkText, True, color)
    rect = textSurface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(textSurface, rect)

def text_in_line(surface, text, font, pos, color=Color("white")):

    checkText = text.strip()
    textSurface = font.render(checkText, True, color)
    rect = textSurface.get_rect()
    rect.center = Vector2(500, pos)

    surface.blit(textSurface, rect)