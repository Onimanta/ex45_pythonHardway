from time import sleep # Used to display the end screen

import pygame
from pygame.locals import * # Import the pygame constant

from external.textrect import render_textrect

class Display():

    window = None
    maze = None
    player = None
    information = None

    def display_maze(self):
        # We start with coordinates set to 10 to shift a bit the maze in the x and y axis
        x = 10
        y = 10

        # We load the entire tileset.
        tileset = pygame.image.load('images/tiles.png')

        # We create a 32*32 surface and then we move the tileset to display
        # only the tile we need in the 32*32 surface.
        room = pygame.Surface((32, 32))

        for line in Display.maze:
            for column in line:

                if column == 'wall':
                    room.blit(tileset, (0, 0), (0, 0, 96, 64))
                elif column == 'start':
                    room.blit(tileset, (0, 0), (64, 0, 96, 64))
                elif column == 'empty':
                    room.blit(tileset, (0, 0), (32, 0, 96, 64))
                elif column == 'foe':
                    room.blit(tileset, (0, 0), (32, 32, 96, 64))
                elif column == 'trap':
                    room.blit(tileset, (0, 0), (64, 32, 96, 64))
                elif column == 'health':
                    room.blit(tileset, (0, 0), (0, 64, 96, 64))
                elif column == 'end':
                    room.blit(tileset, (0, 0), (0, 32, 96, 64))
                else:
                    # If the element in the list is unknown we just draw a
                    # black square to know that there is something wrong.
                    pygame.draw.rect(Display.window, (0, 0, 0), (x, y, 32, 32), 0)

                Display.window.blit(room, (x, y))

                x += 32 # Next room will be displayed 32px further in x axis
            x = 10
            y += 32

    def display_information(self):
        # We get the width of the window to have a relative position to blit the text.
        x = Display.window.get_width()

        # We draw a rectangle over the previous text to erase it.
        pygame.draw.rect(Display.window, (181, 230, 29), (x - 65, 275, 50, 100), 0)

        font_health = pygame.font.Font(None, 18)
        health = font_health.render("Health", 1, (21, 108, 48))
        Display.window.blit(health, (x - 60, 290))

        font_lp = pygame.font.Font(None, 30)
        life_point = font_lp.render(str(Display.player.life_point), 1, (21, 108, 48))
        Display.window.blit(life_point, (x - 52, 310))

    def display_player(self):
        # Blit the player on the screen according to its position in the maze.
        # We do "position + 10" to place the player correctly on the maze.
        Display.window.blit(Display.player.picture, (Display.player.position_y * 32 + 10, Display.player.position_x * 32 + 10))

    def display_text_output(self, text):
        font = pygame.font.Font(None, 22)
        rect = pygame.Rect((15, 275, 500, 100))

        rendered_text = render_textrect("\n" + text, font, rect, (21, 108, 48), (181, 230, 29), 1)

        if rendered_text:
            Display.window.blit(rendered_text, rect.topleft)
        else:
            print "Can't render text."

    def display_title_screen(self):
        title = True
        title_image = pygame.image.load("images/title.png").convert()

        Display.window.blit(title_image, (0, 0))
        pygame.display.flip()

        while title:
            for event in pygame.event.get():

                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN and event.key == K_RETURN:
                    Display.window.fill((34, 177, 76))  # Erase the title screen
                    title = False
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    exit()

    def display_gameover(self):
        gameover = pygame.image.load("images/gameover.png").convert()
        Display.window.blit(gameover, (0, 0))
        pygame.display.flip()

        sleep(5)

    def display_end(self):
        end = pygame.image.load("images/end.png").convert()
        Display.window.blit(end, (0, 0))
        pygame.display.flip()

        sleep(5)

    def display_window(self):
        """Display all the elements of the game"""
        self.display_maze()
        self.display_player()
        self.display_information()
        pygame.display.flip()