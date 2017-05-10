import pygame
from pygame.locals import * # Import the pygame constant

from display import Display
from maze import Maze, Player

window = Display()
window.display_window()

player = Player()

a_maze = Maze(player)
window.display_maze(a_maze.maze)

# We find the position of the start of the maze and assign it to the player position.
start = a_maze.find_in_maze(1)
player.position_x = start[0][0]
player.position_y = start[0][1]

window.display_player(player)

while True:
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

    window.display_maze(a_maze.maze)
    window.display_player(player)
    pygame.display.flip()