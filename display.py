import pygame
from pygame.locals import *

from external.textrect import render_textrect
from external.pygame_textinput import TextInput

class Display():

    window = None
    maze = None
    player = None
    informations = None
    text_output = None
    text_input = None

    def __init__(self):
        pygame.init()
        Display.window = pygame.display.set_mode((500, 500))
        Display.window.fill((195, 195, 195))

    def display_maze(self):
        x = 0
        y = 0

        for line in Display.maze:
            for column in line:
                if column == 0:
                    pygame.draw.rect(Display.window, (0, 0, 0), (x, y, 32, 32), 0)
                elif column == 1:
                    pygame.draw.rect(Display.window, (0, 0, 255), (x, y, 32, 32), 0)
                elif column == 2:
                    pygame.draw.rect(Display.window, (255, 255, 255), (x, y, 32, 32), 0)
                elif column == 3:
                    pygame.draw.rect(Display.window, (255, 0, 0), (x, y, 32, 32), 0)
                x += 32
            x = 0
            y += 32

    def display_information(self):
        pass

    def display_player(self, player):
        Display.window.blit(player.picture, (player.position_y * 32, player.position_x * 32))

    def display_text_output(self, text):
        font = pygame.font.Font(None, 22)
        rect = pygame.Rect((0, 200, 400, 150))

        rendered_text = render_textrect(text, font, rect, (0, 0, 0), (150, 150, 150), 0)

        if rendered_text:
            Display.window.blit(rendered_text, rect.topleft)

    # def display_text_input(self):
    #     textinput = TextInput()
    #
    #     while True:
    #
    #         events = pygame.event.get()
    #         for event in events:
    #             if event.type == pygame.QUIT:
    #                 exit()
    #
    #         if textinput.update(events):
    #             return textinput.get_text()
    #         Display.window.blit(textinput.get_surface(), (0, 500))
    #         pygame.display.flip()