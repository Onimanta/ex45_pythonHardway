import pygame
from pygame.locals import *

from external.textrect import render_textrect
from external.pygame_textinput import TextInput

def window():
    window = pygame.display.set_mode((500, 500))
    window.fill((195, 195, 195))
    return window

def maze(window, maze):
    x = 0
    y = 0

    for line in maze:
        for column in line:
            if column == 0:
                pygame.draw.rect(window, (0, 0, 0), (x, y, 32, 32), 0)
            elif column == 1:
                pygame.draw.rect(window, (0, 0, 255), (x, y, 32, 32), 0)
            elif column == 2:
                pygame.draw.rect(window, (255, 255, 255), (x, y, 32, 32), 0)
            elif column == 3:
                pygame.draw.rect(window, (255, 0, 0), (x, y, 32, 32), 0)
            x += 32
        x = 0
        y += 32


def player(window, player):
    window.blit(player.picture, (player.position_y * 32, player.position_x * 32))

def text_output(window, text):
    #text = "I test the text output.\nI use the textrect file."

    font = pygame.font.Font(None, 22)
    rect = pygame.Rect((0, 200, 400, 150))

    rendered_text = render_textrect(text, font, rect, (0, 0, 0), (150, 150, 150), 0)

    if rendered_text:
        window.blit(rendered_text, rect.topleft)

def text_input(window):
    textinput = TextInput()

    while True:
        window.fill((195, 195, 195))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if textinput.update(events):
            return textinput.get_text()
        window.blit(textinput.get_surface(), (0, 700))
        pygame.display.flip()

def information():
    pass