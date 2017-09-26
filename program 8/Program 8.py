########################################################################
##
## CS 101
## Program #8
## Aaron Darrah
## add522@mail.umkc.edu
##
## PROBLEM : Wumpus are running amok in a maze that has a large fortune in it and we have to create a simulation for
##           the user to determine the best possible path through the maze to get the gold
##
##
## ERROR HANDLING:
##      Have to handle OffMapError I raised
##      Have to handle IndexError if the player doesn't specify a direction to fire in
##
## OTHER COMMENTS:
##      The import statements work if you place both the map and wumpusworld files in the directory containing python on your computer
##      I am going to leave the map generation functions in the code for you to make it easier to test things like falling in a pit,
##      killing the wumpus, being eaten by the wumpus and finding the gold will be easier. You will have to un-comment it though.
##
########################################################################


from map import OffMapError
import wumpusworld

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
    ww = wumpusworld.WumpusWorld()
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

