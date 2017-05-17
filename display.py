import pygame
from time import sleep # Used to display the end screen

from external.textrect import render_textrect

class Display():

    window = None
    maze = None
    player = None
    information = None

    def display_maze(self):
        x = 10
        y = 10

        tileset = pygame.image.load('images/tiles.png')
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

                Display.window.blit(room, (x, y))

                x += 32
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

    def display_title_screen(self):
        title = pygame.image.load("images/title.png").convert()
        Display.window.blit(title, (0, 0))
        pygame.display.flip()

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