import os # To choose where the window appear on the screen
import pygame
from pygame.locals import * # Import the pygame constant

from display import Display
from maze import Maze, Player

# We choose where the window appear on the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "600, 200"

pygame.init()

Display.window = pygame.display.set_mode((600, 390), pygame.NOFRAME)
Display.window.fill((34, 177, 76))

display = Display()

# We display the title screen of the game.
title = True
display.display_title_screen()
while title:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN and event.key == K_RETURN:
            Display.window.fill((34, 177, 76)) # Erase the title screen
            title = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exit()

player = Player()
Display.player = player

a_maze = Maze(player)
Display.maze = a_maze.maze

display.display_text_output(
    "You awake and notice that you're in the back of your garden.\n"
    "However it feels a bit different..\n"
    "You get up and decide to go back to your home."
)

# We find the position of the start of the maze and assign it to the player position.
start = a_maze.find_in_maze('start')
player.position_x = start[0][0]
player.position_y = start[0][1]

while player.life_point > 0:
    # We go through the list of all received events.
    for event in pygame.event.get():
        if event.type == QUIT:  # If event is of type QUIT
            exit()
        elif event.type == KEYDOWN and event.key == K_UP:
            a_maze.move_player('up')
        elif event.type == KEYDOWN and event.key == K_DOWN:
            a_maze.move_player('down')
        elif event.type == KEYDOWN and event.key == K_LEFT:
            a_maze.move_player('left')
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            a_maze.move_player('right')
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exit()


    display.display_window()

display.display_gameover()
exit()