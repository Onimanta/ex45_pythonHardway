import pygame
from pygame.locals import * # Import the pygame constant
from random import choice # For random choice of the foe

from display import Display

class Room(object):

    def __init__(self):
        self.display = Display()

class Start(Room):

    def enter(self, player):
        self.display.display_text_output("Enter start room.")

        return False

class Empty(Room):

    def enter(self, player):
        self.display.display_text_output("Enter empty room.")

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
            "You encounter a " + self.foe['name'] + "\n" +
            "He is " + self.foe['place'] + "\n" +
            "He " + self.foe['action'] + "\n" +
            "You take " + str(self.foe['strength']) + " damage.\n" +
            "The " + self.foe['name'] + " disappaer in the bushes."
        )
        player.life_point -= self.foe['strength']
        self.display.display_window()

        return True

class Trap(Room):

    def enter(self, player):
        self.display.display_text_output(
            "Enter trap room.\n" +
            "What do you do?\n" +
            "1. Walk\n" +
            "2. Walk carefully"
        )
        self.display.display_window()

        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == QUIT:  # If event is of type QUIT
                    exit()
                elif event.type == KEYDOWN and event.key == K_1:
                    self.display.display_text_output("You get hurt by the trap.")
                    player.life_point -= 5
                    loop = False
                elif event.type == KEYDOWN and event.key == K_2:
                    self.display.display_text_output("You avoid the trap.")
                    loop = False

        return False

class End(Room):

    def enter(self, player):
        self.display.display_end("The End")
        exit()

class Player(object):

    def __init__(self):
        self.life_point = 10
        self.position_x = 0
        self.position_y = 0
        self.picture = pygame.image.load("player.png").convert()
        self.picture.set_colorkey((255,255,255))


class Maze(object):

    rooms = {
        'start': Start(),
        'empty': Empty(),
        'foe': Foe(),
        'trap': Trap(),
        'end': End()
    }

    def __init__(self, player):
        self.maze = []

        with open('maze.csv') as file:
            for line in file:
                line = line.replace('\n', '')
                self.maze.append(line.split(','))

        # We convert the items of the 2d list to int.
        # for idx, line in enumerate(self.maze):
        #     for idy, number in enumerate(line):
        #         self.maze[idx][idy] = int(self.maze[idx][idy])

        self.player = player

    def find_in_maze(self, room):
        """Search for all occurences of room in the maze (2d list) and return coordinates"""
        position = [(index, row.index(room)) for index, row in
                    enumerate(self.maze) if room in row]
        return position

    def position_ok(self, x, y):
        """Check if the player can be on a given position in the maze."""
        ok = False

        # We check if the given x and y coordinate don't exceed the size of the maze.
        if x > len(self.maze) - 1 or x < 0 or y > len(self.maze[x]) - 1 or y < 0:
            ok = False
        else:
            # Then we check if there is not a wall at the given position.
            if self.maze[x][y] == 'wall':
                ok = False
            else:
                ok = True

        return ok

    def move_player(self, direction):
        """Change the position of the player in the maze depending of a given direction."""
        previous_position = [self.player.position_x, self.player.position_y]

        if direction == 'up' and self.position_ok(self.player.position_x - 1, self.player.position_y):
            self.player.position_x -= 1
        elif direction == 'down' and self.position_ok(self.player.position_x + 1, self.player.position_y):
            self.player.position_x += 1
        elif direction == 'left' and self.position_ok(self.player.position_x, self.player.position_y - 1):
            self.player.position_y -= 1
        elif direction == 'right' and self.position_ok(self.player.position_x, self.player.position_y + 1):
            self.player.position_y += 1

        position = [self.player.position_x, self.player.position_y]

        # If the position of the player has changed, enter the room
        if position != previous_position:
            self.enter_room()

    def enter_room(self):
        player_position = self.maze[self.player.position_x][self.player.position_y]
        room = Maze.rooms.get(player_position)
        # The room return if it remain or if it disapear.
        disappear = room.enter(self.player)

        if disappear:
            # Replace the room with an empty room
            self.maze[self.player.position_x][self.player.position_y] = 'empty'