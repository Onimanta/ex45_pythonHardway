from random import choice  # Used for random choice of the foe.

import pygame
from pygame.locals import *

from display import Display


class Room(object):

    def __init__(self):
        self.display = Display()

class Start(Room):

    def enter(self, player):
        self.display.display_text_output("You've come back to the start.")
        return False

class Empty(Room):

    def enter(self, player):
        self.display.display_text_output("You walk on the grass.")
        return False

class Foe(Room):

    def __init__(self):
        super(Foe, self).__init__()

        foes_list = [
            {'name': "Evil Mushroom", 'place': "hidden at the foot of a bush.",
             'strength': 3, 'action': "call is friends and they punch your feet."},
            {'name': "Grass Goblin", 'place': "lying on the ground.",
             'strength': 4, 'action': "stands, jumps on you and bites your arm."},
            {'name': "Warrior Tree", 'place': "standing in the middle of the path.",
             'strength': 6, 'action': "smashes you with his wooden spear."}
        ]
        self.foe = choice(foes_list)

    def enter(self, player):
        self.display.display_text_output(
            "You encounter a " + self.foe['name'] + "\n"
            "He is " + self.foe['place'] + "\n"
            "He " + self.foe['action'] + "\n"
            "You take " + str(self.foe['strength']) + " damage.\n"
            "The " + self.foe['name'] + " disappaer in the bushes."
        )
        player.life_point -= self.foe['strength']
        self.display.display_window()

        return True

class Trap(Room):

    def enter(self, player):
        self.display.display_text_output(
            "You see a hole in front of you.\n"
            "What do you do?\n"
            "1. Jump over the hole\n"
            "2. Jump onto the hole"
        )
        self.display.display_window()

        loop = True
        while loop:
            for event in pygame.event.get():

                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN and event.key == K_1:
                    self.display.display_text_output("You jump over the hole and "
                                                     "continue your way.")
                    loop = False
                elif event.type == KEYDOWN and event.key == K_2:
                    self.display.display_text_output(
                        "You jump in the hole and you hurt you.\n" +
                        "You take 5 damage.\n" +
                        "You manage to rise to the surface and you continue your way."
                    )
                    player.life_point -= 5
                    loop = False
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    exit()

        return False

class Health(Room):

    def enter(self, player):
        """When the player will enter this room, it will recover some life points."""
        health = 3

        self.display.display_text_output("You find some berries and you eat them.\n" +
                                         "You recover " + str(health) + " life points.")
        player.life_point += health
        self.display.display_window()

        return True

class End(Room):

    def enter(self, player):
        self.display.display_end()
        exit()


class Player(object):

    def __init__(self):
        self.life_point = 10
        self.position_x = 0
        self.position_y = 0
        self.picture = pygame.image.load("images/player.png").convert()
        self.picture.set_colorkey((255, 255, 255))


class Maze(object):

    rooms = {
        'start': Start(),
        'empty': Empty(),
        'foe': Foe(),
        'trap': Trap(),
        'health': Health(),
        'end': End()
    }

    def __init__(self, player):
        self.maze = []

        with open('maze.csv') as file:
            for line in file:
                line = line.replace('\n', '')
                self.maze.append(line.split(','))

        self.player = player

    def find_in_maze(self, room):
        """Search for all occurrences of "room" in the maze (2d list) and return coordinates"""
        position = [(index, row.index(room)) for index, row in enumerate(self.maze) if room in row]
        return position

    def position_ok(self, x, y):
        """Check if the player can be on a given position in the maze."""
        ok = False

        position_out_of_maze = x > len(self.maze) - 1 or x < 0 or y > len(self.maze[x]) - 1 or y < 0

        # We check if the given x and y coordinate don't exceed the size of the maze.
        if position_out_of_maze:
            ok = False
        else:
            # Then we check if there is not a wall at the given position.
            if self.maze[x][y] == 'wall':
                ok = False
            else:
                ok = True

        return ok

    def move_player(self, direction):
        """Change the position of the player in the maze depending of a given direction.

        :param direction: text which indicate in which direction the player will move.
        """
        shift_vect = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        player_position = previous_position = [self.player.position_x, self.player.position_y]

        def shift_by(pos, shift):
            return pos[0] + shift[0], pos[1] + shift[1]

        new_position = shift_by(player_position, shift_vect[direction])

        if self.position_ok(new_position[0], new_position[1]):
            player_position = new_position
            self.player.position_x = player_position[0]
            self.player.position_y = player_position[1]

        # We don't enter the room again if the position of the player hasn't changed.
        if player_position != previous_position:
            self.enter_room()

    def enter_room(self):
        """Enter the room at the current player position."""
        player_position = self.maze[self.player.position_x][self.player.position_y]
        room = Maze.rooms.get(player_position)
        disappear = room.enter(self.player)

        if disappear:
            # We replace the room with an empty room.
            self.maze[self.player.position_x][self.player.position_y] = 'empty'
