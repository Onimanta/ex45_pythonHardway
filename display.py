import pygame

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

    def display_text_output(self):
        pass

    def display_text_input(self):
        pass

    def display_information(self):
        pass