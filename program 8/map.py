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