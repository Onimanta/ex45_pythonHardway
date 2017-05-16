import pygame
from pygame.locals import * # Import the pygame constant

from display import Display
from maze import Maze, Player

pygame.init()

Display.window = pygame.display.set_mode((500, 500))
Display.window.fill((195, 195, 195))

display = Display()

# We display the title screen of the game.
title = True
display.display_title_screen()
while title:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN and event.key == K_RETURN:
            Display.window.fill((195, 195, 195)) # Erase the title screen
            title = False

player = Player()
Display.player = player

a_maze = Maze(player)
Display.maze = a_maze.maze

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

    display.display_window()

display.display_end("Game Over")
exit()