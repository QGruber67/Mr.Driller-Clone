from character import *
from level import *
from pygame.locals import *


def keydownHandle(event, currentLine, surface, level):

    if event.key == K_g:
        if currentLine < len(level):
            pygRenderNxtLine(surface, currentLine, level)
            currentLine += 1
        return currentLine


def movementHandle(event, surface, player, level, movKeys):

    if event.key == movKeys[2]:
        player.move(surface, 3, level)
    elif event.key == movKeys[1]:
        player.move(surface, 2, level)
    elif event.key == movKeys[0]:
        player.move(surface, 1, level)


def breaking(event, surface, player, level):

    if event.key == K_UP:
        player.breakBlock(surface, 1, level)
    elif event.key == K_RIGHT:
        player.breakBlock(surface, 2, level)
    elif event.key == K_DOWN:
        player.breakBlock(surface, 3, level)
    elif event.key == K_LEFT:
        player.breakBlock(surface, 4, level)

