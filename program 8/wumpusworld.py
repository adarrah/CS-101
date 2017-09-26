import map

 ## creates wumpusworld object for program 8.py to call to run the game
class WumpusWorld(object):

     ## initializes the map and variables
    def __init__(self):
        self.worldmap = map.Map()
        self.wumpusAlive    = True
        self.playerAlive    = True
        self.playerHasGold  = False
        self.playerHasArrow = True
        self.playerMoves    = 0
        self.playerRow      = 0
        self.playerCol      = 0


     ## moves the user east or throws an OffMapError
    def stepEast(self):
        """Moves the user east if they are on the grid if they aren't it will throw an OffMapError"""

        if self.worldmap.offGrid(self.playerRow,self.playerCol + 1):
            self.playerMoves += 1
            raise map.OffMapError("You're out of bounds dingus!")

        else:
            self.playerCol += 1
            self.playerMoves += 1

     ## moves the user west or throws an OffMapError
    def stepWest(self):
        """Moves the user west if they are on the grid if they aren't it will throw an OffMapError"""

        if self.worldmap.offGrid(self.playerRow,self.playerCol - 1):
            self.playerMoves += 1
            raise map.OffMapError("You're out of bounds dingus!")

        else:
            self.playerCol -= 1
            self.playerMoves += 1

     ## moves the user north or throws an OffMapError
    def stepNorth(self):
        """Moves the user north if they are on the grid if they aren't it will throw an OffMapError"""

        if self.worldmap.offGrid(self.playerRow + 1,self.playerCol):
            self.playerMoves += 1
            raise map.OffMapError("You're out of bounds dingus!")

        else:
            self.playerRow += 1
            self.playerMoves += 1

     ## moves the user south or throws an OffMapError
    def stepSouth(self):
        """Moves the user south if they are on the grid if they aren't it will throw an OffMapError"""

        if self.worldmap.offGrid(self.playerRow - 1,self.playerCol):
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
            for row in range(self.playerRow,-1,-1):
                if self.worldmap.grid[row][self.playerCol].has_wumpus == True:
                    self.wumpusAlive = False
                    return True

        if direction == "north" or direction[0] == "n":
            for row in range(self.playerRow,4):
                if self.worldmap.grid[row][self.playerCol].has_wumpus == True:
                    self.wumpusAlive = False
                    return True

        if direction == "west" or direction[0] == "w":
            for row in range(self.playerCol,-1,-1):
                if self.worldmap.grid[row][self.playerCol].has_wumpus == True:
                    self.wumpusAlive = False
                    return True

        if direction == "east" or direction[0] == "e":
            for row in range(self.playerRow,4):
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

        if self.worldmap.isBreezy(self.playerRow,self.playerCol):
            return True
        return False

     ## determines if the user's square has a stench
    def smellStench(self):
        """Determines if the user's square has a stench by calling the map function isSmelly returns true if there is a stench, otherwise returns false"""

        if self.worldmap.isSmelly(self.playerRow,self.playerCol):
            return True
        return False

     ## determines if the user's square has a glint
    def seeGlint(self):
        """Determines if the user is in the same square as the gold if it does it returns true, otherwise returns false"""

        if self.worldmap.grid[self.playerRow][self.playerCol].has_gold == True:
            return True
        return False

     ## determines if the user's square has the wumpus
    def hasWumpus(self,):
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