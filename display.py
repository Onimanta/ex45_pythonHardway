import pygame

from external.textrect import render_textrect

class Display(object):

    def __init__(self):
        pygame.init()

    def display_window(self):
        self.window = pygame.display.set_mode((500, 500))
        self.window.fill((195, 195, 195))

    def display_maze(self, maze):
        x = 0
        y = 0

        for line in maze:
            for column in line:
                if column == 0:
                    pygame.draw.rect(self.window, (0, 0, 0), (x, y, 32, 32), 0)
                elif column == 1:
                    pygame.draw.rect(self.window, (0, 0, 255), (x, y, 32, 32), 0)
                elif column == 2:
                    pygame.draw.rect(self.window, (255, 255, 255), (x, y, 32, 32), 0)
                elif column == 3:
                    pygame.draw.rect(self.window, (255, 0, 0), (x, y, 32, 32), 0)
                x += 32
            x = 0
            y += 32


    def display_player(self, player):
        self.window.blit(player.picture, (player.position_y * 32, player.position_x * 32))

    def display_text_output(self, text):
        text = "I test the text output.\nI use the textrect file."

        font = pygame.font.Font(None, 22)
        rect = pygame.Rect((0, 200, 400, 150))

        rendered_text = render_textrect(text, font, rect, (0, 0, 0), (150, 150, 150), 0)

        if rendered_text:
            self.window.blit(rendered_text, rect.topleft)

    def display_text_input(self):
        pass

    def display_information(self):
        pass