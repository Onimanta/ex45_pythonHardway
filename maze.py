import pygame

class Room(object):

    def __init__(self):
        pass

class Start(Room):

    def enter(self):
        print "Enter start room."

class Empty(Room):

    def enter(self):
        print "Enter empty room."

class End(Room):

    def enter(self):
        print "Enter end room."


class Player(object):

    def __init__(self):
        self.life_point = 10
        self.position_x = 0
        self.position_y = 0
        self.picture = pygame.image.load("player.png").convert()
        self.picture.set_colorkey((255,255,255))


class Maze(object):

    rooms = {
        1: Start(),
        2: Empty(),
        3: End()
    }

    def __init__(self, player):
        self.maze = [[1, 0, 3], [2, 0, 2], [2, 2, 2]]
        self.player = player

    def find_in_maze(self, room):
        """Search for all occurences of room in the maze (2d list) and return coordinates"""
        position = [(index, row.index(room)) for index, row in
                    enumerate(self.maze) if room in row]
        return position

    def position_ok(self, x, y):
        """Check if the player can be on a given position in the is maze."""
        ok = False

        # Check if the given x and y coordinate don't exceed the size of the maze
        if x > len(self.maze) - 1 or x < 0 or y > len(self.maze[x]) - 1 or y < 0:
            ok = False
        else:
            # Then check if there is not a wall at the given position
            if self.maze[x][y] == 0:
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

        # If the position hasn't changed don't enter the room again
        if position != previous_position:
            self.enter_room()

    def enter_room(self):
        player_position = self.maze[self.player.position_x][self.player.position_y]
        room = Maze.rooms.get(player_position)
        room.enter()