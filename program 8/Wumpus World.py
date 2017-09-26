import random

## creates an OffMapError that can be thrown
class OffMapError(Exception):
    """Error raised if user attempts to go off the map"""
    pass

 ## creates cell class for the map in wumpusworld.py
class Cell(object):

     ## initialize base variable
    has_wumpus = False
    has_gold = False
    has_pit = False

     ## create an instance of cell
    def __init__(self, row, col):

        self.row = row
        self.col = col

     ## just a string representation I made for testing during development, this is ignorable
    """def __str__(self):
        if self.has_wumpus == True and self.has_pit == True and self.has_gold == True:
            return "{:^5}".format("WGP.")
        elif self.has_wumpus == True and self.has_gold == True:
            return "{:^5}".format("WG")
        elif self.has_gold == True and self.has_pit == True:
            return "{:^5}".format("GP")
        if self.has_wumpus == True and self.has_pit == True:
            return  "{:^5}".format("WP")
        elif self.has_pit == True:
            return "{:^5}".format("P")
        elif self.has_wumpus ==True:
            return  "{:^5}".format("W")
        elif self.has_gold ==True:
            return  "{:^5}".format("G")
        else:
            return "({}:{})".format(self.row,self.col)"""

 ## creates a map class to be used by wumpusworld.py
class Map(object):

     ## initializes a grid list
    grid = []

     ## creates an instance of map
    def __init__(self):
        self.reset()

     ## determines if the given coordinates are in the grid list
    def onGrid(self,r,c):
        """Determines if the given coordinates are in the grid list if they are return true, otherwise return false"""

        if r in range(0,4) and c in range(0,4):
            return True
        return False

     ## determies if the given coordinates are not in the grid list
    def offGrid(self,r,c):
        """Determines if the given coordinates are not in the grid list if they aren't returns true, otherwise returns false"""
        if r not in range(0,4) or c not in range(0,4):
            return True
        return False

     ## determines if the squares surrounding the given square have the wumpus
    def isSmelly(self,r,c):
        """determines if the squares surrounding the given square are on the grid and have the wumpus, if any of them do it will return true, otherwise it returns false"""

        if self.onGrid(r,c+1) and self.hasWumpus(r,c+1):
            return True

        elif self.onGrid(r,c-1) and self.hasWumpus(r,c-1):
            return True

        elif self.onGrid(r+1,c) and self.hasWumpus(r+1,c):
            return True

        elif self.onGrid(r-1,c) and self.hasWumpus(r-1,c):
            return True

        return False

        ## determines if the squares surrounding the given square have pits
    def isBreezy(self,r,c):
        """determines if the squares surrounding the given square are on the grid and have pits, if any of them do it will return true, otherwise it returns false"""

        if self.onGrid(r,c+1) and self.hasPit(r,c+1):
            return True

        elif self.onGrid(r,c-1) and self.hasPit(r,c-1):
            return True

        elif self.onGrid(r+1,c) and self.hasPit(r+1,c):
            return True

        elif self.onGrid(r-1,c) and self.hasPit(r-1,c):
            return True

        return False

     ## determines if the given square has the gold
    def isGlinty(self,r,c):
        """determines if the given square has the gold if it does returns true, otherwise returns false"""

        if self.grid[r][c].has_gold == True:
            return True

        return False

     ## determines if the given square has the gold
    def grabGold(self,r,c):
        """determines if the given square has the gold if it does then it sets the cells has_gold to false """
        if self.hasGold(r,c):
            self.grid[r][c].has_gold = False

     ## determines if the given square has the wumpus
    def hasWumpus(self,r,c):
        """determines if the given square has the wumpus if it does then returns true, otherwise returns false"""

        if self.grid[r][c].has_wumpus == True:
            return True
        return False

     ## determines if the given square has the gold in it
    def hasGold(self,r,c):
        """determines if the given square has the gold in it if it does returns true, otherwise returns fase"""

        if self.grid[r][c].has_gold == True:
            return True

        return False

     ## determines if the given square has pit
    def hasPit(self,r,c):
        """determines if the given square has pit if it does returns true, otherwise returns false"""

        if self.grid[r][c].has_pit == True:
            return True

        return False
     ## resets the map
    def reset(self):
        """Resets the two dimensional list grid and repopulates it with cells and puts pits, the wumpus and the gold on the map"""

        self.grid = []

         ## creates a two dimensional list of cells by making a temporary list and adding cells to it and appending it to grid
        for row in range(0, 5):
            temp_list = []

            for col in range(0, 5):
                temp_list.append(Cell(row, col))
            self.grid.append(temp_list)

         ## creates the obstacles to on the map by running through the loop until seven obstacles have been place on the grid with no pits on the same square
        obstacle_count = 0

        while obstacle_count < 7:

             ## generates random row and column
            rand_row = random.randint(0, 4)
            rand_col = random.randint(0, 4)

             ## the first five obstacles will be the five pits
            if obstacle_count < 5:
                if self.hasPit(rand_row,rand_col) == False and (rand_row != 0 and rand_col != 0):
                    self.grid[rand_row][rand_col].has_pit = True
                    obstacle_count += 1

             ## the sixth object is the wumpus
            elif obstacle_count == 5:
                if rand_row != 0 and rand_col != 0:
                    self.grid[rand_row][rand_col].has_wumpus = True
                    obstacle_count += 1

             ## finally the gold is placed
            else:
                if rand_row != 0 and rand_col != 0:
                    self.grid[rand_row][rand_col].has_gold = True
                    obstacle_count += 1

    """def __str__(self):
        grid_str = ""
        for row in range(4,-1,-1):
            for col in range(0,5):
                grid_str += str(self.grid[row][col])
            grid_str += "\n"
        return grid_str"""

class WumpusWorld(object):

         ## initializes the map and variables
        def __init__(self):
             self.worldmap = Map()
             self.wumpusAlive = True
             self.playerAlive = True
             self.playerHasGold = False
             self.playerHasArrow = True
             self.playerMoves = 0
             self.playerRow = 0
             self.playerCol = 0


             ## moves the user east or throws an OffMapError

        def stepEast(self):
             """Moves the user east if they are on the grid if they aren't it will throw an OffMapError"""

             if self.worldmap.offGrid(self.playerRow, self.playerCol + 1):
                 self.playerMoves += 1
                 raise map.OffMapError("You're out of bounds dingus!")

             else:
                 self.playerCol += 1
                 self.playerMoves += 1

                 ## moves the user west or throws an OffMapError

        def stepWest(self):
             """Moves the user west if they are on the grid if they aren't it will throw an OffMapError"""

             if self.worldmap.offGrid(self.playerRow, self.playerCol - 1):
                 self.playerMoves += 1
                 raise map.OffMapError("You're out of bounds dingus!")

             else:
                 self.playerCol -= 1
                 self.playerMoves += 1

                 ## moves the user north or throws an OffMapError

        def stepNorth(self):
             """Moves the user north if they are on the grid if they aren't it will throw an OffMapError"""

             if self.worldmap.offGrid(self.playerRow + 1, self.playerCol):
                 self.playerMoves += 1
                 raise map.OffMapError("You're out of bounds dingus!")

             else:
                 self.playerRow += 1
                 self.playerMoves += 1

                 ## moves the user south or throws an OffMapError

        def stepSouth(self):
             """Moves the user south if they are on the grid if they aren't it will throw an OffMapError"""

             if self.worldmap.offGrid(self.playerRow - 1, self.playerCol):
                 self.playerMoves += 1
                 raise map.OffMapError("You're out of bounds dingus!")

             else:
                 self.playerRow -= 1
                 self.playerMoves += 1

                 ## grabs the gold if it is in the square

        def grabGold(self):
             """Grabs the gold if the user and gold are in the same square and returns true, otherwise returns false"""

             self.playerMoves += 1
             if self.worldmap.grid[self.playerRow][self.playerCol].hasGold():
                 self.worldmap.grid[self.playerRow][self.playerCol].grabGold()
                 self.playerHasGold = True
                 return True

             return False

             ## fires an arrrow in the given direction

        def fire(self, direction):
             """Fires an arrow in the given direction and if it hits the wumpus returns true, otherwise it returns false but still fires the arrow"""

             self.playerMoves += 1
             self.playerHasArrow = False

             if direction == "south" or direction[0] == "s":
                 for row in range(self.playerRow, -1, -1):
                     if self.worldmap.grid[row][self.playerCol].has_wumpus == True:
                         self.wumpusAlive = False
                         return True

             if direction == "north" or direction[0] == "n":
                 for row in range(self.playerRow, 4):
                     if self.worldmap.grid[row][self.playerCol].has_wumpus == True:
                         self.wumpusAlive = False
                         return True

             if direction == "west" or direction[0] == "w":
                 for row in range(self.playerCol, -1, -1):
                     if self.worldmap.grid[row][self.playerCol].has_wumpus == True:
                         self.wumpusAlive = False
                         return True

             if direction == "east" or direction[0] == "e":
                 for row in range(self.playerRow, 4):
                     if self.worldmap.grid[row][self.playerCol].has_wumpus == True:
                         self.wumpusAlive = False
                         return True

             return False

             ## determines if the user can climb from the current square

        def canClimb(self):
             """Determines if the user is in square 0,0 and if they are returns true, otherwise returns false"""

             self.playerMoves += 1
             if self.playerRow == 0 and self.playerCol == 0:
                 return True
             return False

             ## determinse if the square the user is in has a breeze

        def feelBreeze(self):
             """Determines if the user's square has a breeze by calling the map function isBreezy returns true if there is a breeze, otherwise returns false"""

             if self.worldmap.isBreezy(self.playerRow, self.playerCol):
                 return True
             return False

             ## determines if the user's square has a stench

        def smellStench(self):
             """Determines if the user's square has a stench by calling the map function isSmelly returns true if there is a stench, otherwise returns false"""

             if self.worldmap.isSmelly(self.playerRow, self.playerCol):
                 return True
             return False

             ## determines if the user's square has a glint

        def seeGlint(self):
             """Determines if the user is in the same square as the gold if it does it returns true, otherwise returns false"""

             if self.worldmap.grid[self.playerRow][self.playerCol].has_gold == True:
                 return True
             return False

             ## determines if the user's square has the wumpus

        def hasWumpus(self, ):
             """Determines if the user's square has the wumpus if it does returns true, otherwise returns false"""

             if self.worldmap.grid[self.playerRow][self.playerCol].has_wumpus == True:
                 return True
             return False

             ## determines if the user's square has a pit

        def hasPit(self):
             """Determines if the user's square has a pit if it does returns true, otherwise returns false"""

             if self.worldmap.grid[self.playerRow][self.playerCol].has_pit == True:
                 return True
             return False

 ## asks the user if they would like to continue playing the game and returns true if they do and false if they don't
def keep_playing():
    while True:
        """asks the user if they would like to continue playing the game and returns true if they do and false if they don't"""

        user_in = input("Would you like to play again Y/N ==> ")
        if user_in.lower() == 'y':
            return True
        elif user_in.lower() == "n":
            return False
        else:
            print("Enter Y or N")
cont_game = True

 ## while cont_game variable is true, cont_game is updated at bottom by calling keep_playing()
while cont_game:

     ## initialize the wumpusworld instance and create a player score to be updated throughout the program
    ww = WumpusWorld()
    player_score = 0

    print("Welcome to Wumpus World!\nYour goal is to find the goal and avoid the stinky Wumpus")
    ##print(ww.worldmap)

     ## while the player is still alive it will run the loop again and ask for another command
    while ww.playerAlive:

         ## prints initial conditions each turn ie. if there is a pit in the column to the right you feel a breeze
        if ww.feelBreeze():
            print("You feel a breeze.")

        if ww.smellStench():
            print("You smell an awful stench.")

        if ww.seeGlint():
            print("You see a glint.")

        elif ww.seeGlint() == False and ww.smellStench() == False and ww.feelBreeze() == False:
            print("It is dark.")

         ## gets the user input to determine which move to make
        command = input("What would you like to do? ")

         ## based on the command given it runs the method in wumpus world to make that move
        try:
             ## moves east
            if command.lower() == 'east':
                ww.stepEast()

             ## moves west
            elif command.lower() == 'west':
                ww.stepWest()

             ## moves north
            elif command.lower() == 'north':
                ww.stepNorth()

             ## moves south
            elif command.lower() == 'south':
                ww.stepSouth()

             ## climbs out of wumpus world
            elif command.lower() == 'climb':
                if ww.canClimb():
                    if ww.playerHasGold:
                        player_score += 1000

                    else:
                        player_score += 100
                    print("You climb up out of Wumpus World.")
                    ww.playerAlive = False

                else:
                    print("You cannot climb here!")

             ## grabs the gold
            elif command.lower() == 'grab':
                if ww.grabGold():
                    print("You pick up the gold.")

                else:
                    print("There is no gold here.")

             ## fires the arrow
            elif 'fire' in command.lower():
                player_score -= 10
                 ## if you don't have an error the program says there is no arrow
                if ww.playerHasArrow == False:
                    print("You try to fire but you don't have an arrow.")

                 ## if you have an arrow you shoot and if you hit the wumpus
                elif ww.fire(command.lower().split()[1]):
                    print("You shoot an arrow")
                    print("You hear a terrible scream in the darkness.")

                 ## if you have an arrow and it shoots and doesn't hit the wumpus
                else:
                    print("You shoot an arrow.")

            elif command.lower() == 'help':
                print("Here are a list of commands you can execute.\nNorth, South, East, West: will move you around wumpus world\n"\
                      "Grab: will grab the gold if it is in the same space as you\nFire [direction]: will fire in arrow in the cardinal direction you give it"\
                      "\nClimb: will climb out of Wumpus World if you in the starting space")

            else:
                print("That is not a valid move.")

        except OffMapError:
            print("You feel a bump as you run into the wall")

        except IndexError:
            print("You must enter a direction to fire your arrow.")

        player_score -= 1

        if ww.hasPit():
            print("You have fallen into a pit.")
            player_score = 0
            ww.playerAlive = False

        elif ww.hasWumpus():
            if ww.wumpusAlive:
                print("There is a live Wumpus here!")
                print("You were eaten by the Wumpus")
                player_score = 0
                ww.playerAlive = False

            else:
                print("There is a dead Wumpus here.")

    print("You scored {} points!".format(player_score))
    cont_game = keep_playing()