import pygame
from time import sleep # Used to display the end screen

from external.textrect import render_textrect

class Display():

    window = None
    maze = None
    player = None
    information = None

    def display_maze(self):
        x = 0
        y = 0

        tileset = pygame.image.load('tiles.png')
        room = pygame.Surface((32, 32))

        for line in Display.maze:
            for column in line:
                if column == 0:
                    room.blit(tileset, (0, 0), (0, 0, 96, 64))
                elif column == 1:
                    room.blit(tileset, (0, 0), (64, 0, 96, 64))
                elif column == 2:
                    room.blit(tileset, (0, 0), (32, 0, 96, 64))
                elif column == 3:
                    room.blit(tileset, (0, 0), (32, 32, 96, 64))
                elif column == 4:
                    room.blit(tileset, (0, 0), (64, 32, 96, 64))
                elif column == 5:
                    room.blit(tileset, (0, 0), (0, 32, 96, 64))

                Display.window.blit(room, (x, y))

                x += 32
            x = 0
            y += 32

    def display_information(self):
        # We get the width of the window to have a relative position to blit the text.
        x = Display.window.get_width()

        font = pygame.font.Font(None, 22)
        label = font.render(str(Display.player.life_point), 1, (0, 0, 0))
        # We draw a rectangle over the previous text to erase it.
        pygame.draw.rect(Display.window, (255, 255, 255), (x - 50, 0, 50, 100), 0)
        Display.window.blit(label, (x - 50, 25))

    def display_player(self):
        Display.window.blit(Display.player.picture, (Display.player.position_y * 32, Display.player.position_x * 32))

    def display_text_output(self, text):
        font = pygame.font.Font(None, 22)
        rect = pygame.Rect((0, 200, 400, 150))

        rendered_text = render_textrect(text, font, rect, (0, 0, 0), (150, 150, 150), 0)

        if rendered_text:
            Display.window.blit(rendered_text, rect.topleft)

    def display_end(self, text):
        Display.window.fill((195, 195, 195))

        x, y = Display.window.get_size()

        font = pygame.font.Font(None, 50)
        end_text = font.render(str(text), 1, (0, 0, 0))
        Display.window.blit(end_text, (x / 2 - 100, y / 2 - 50))
        pygame.display.flip()

        sleep(3)

    def display_window(self):
        """Display all the elements of the game"""
        self.display_maze()
        self.display_player()
        self.display_information()
        pygame.display.flip()