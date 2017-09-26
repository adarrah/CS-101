########################################################################
##
## CS 101
## Program #4
## Aaron Darrah
## add522@mail.umkc.edu
##
## PROBLEM : To correctly handle file to gather information on latitudes and longitudes
##           within the files and use the numbers from the file in calculations without errors
##
## ALGORITHM :
##Create a function file_input that takes two arguments: in_or_out and prompt
## 	Run an infinite while loop
## 		Try
## 			Assign input(prompt) to file_name
## 			If in_or_out is “INPUT”
## 				Open file_name for reading and assign it to inFile
## 				Return inFile
## 			Else if in_or_out is “OUTPUT”
## 				Open file_name for writing and assign it to outFile
## 				Return outFile
## 		Except any IOErrors
## 			Print please enter a valid file name
## Create function get_lat that takes a string called line
## 	Return line from -55 to -39 stripped and as an float
## Create function get_lon that takes a string called line
## 	Return line from -40 to -24 stripped and as a float
## Create function float_input that takes a string called prompt
## 	Infinite while loop
## 		Try
## 			Get the float value of input using prompt and assign it to fl_input
## 			Return fl_input
## 		Except any ValueErrors
## 			Print please enter a valid number
## Create function get_dist_miles that takes four int arguments lat1,lat2,long1,long2
## 	Subtract long1 from long2 and assign to diffLong
## 	Assign the difference of lat2 and lat1 to diffLat
## 	Assign sin(diffLat/2)^2 + cos(lat1) * cos(lat2) * sin(diffLong/2)^2 to a
## 	Assign 2 *atan2(squareroot of a and squareroot of 1-a) to c
## 	Assign the product of c and 3961 to d
## 	Return d
## Create function cont_prog with no arguments
## 	Infinite while loop
## 		Assign the input from “continue playing” to cont
## 		If cont is “Y”
## 			Return True
## 		Else if cont is “N”
## 			Return False
## 		Else
## 			Print please enter Y or N
## Create function int_input with string argument prompt
## 	Infinite while loop
## 		Try
## 			Get the int value of input using prompt and assign it to intInput
## 			Return intInput
## 		Except any ValueErrors
## 			Print please enter a valid number
## keep_going  is true
## While keep_going
## Call file_input with arguments INPUT and “please enter the name of the input file” and assing it to mtr_file
## Call file_input with arguments OUTPUT and “please enter the name of the output file” and assign it to output_file
## userLat = 91
## userLong = 181
## userRad = -1
## Infinite while loop
## 	If userLat >90 or userLat < -90
## 		Call float_input with argument “please enter lat between -90 and 90” and assign it to userLat
## 	Else
## 		Break
## Infinite while loop
## 	If userLong >180 or userLong < -180
## Call float_input with argument “please enter lat between -180 and 180” and assign it \ to userLong
## 	Else
## 		Break
## Infinite while loop
## 	If userRad < 0
## Call int_input with argument “please enter radius to search for meterors” and assign it\ userRad
## 	Else
## 		Break
##
## For line in mtr_file
## 	Call get_lat with line and assing it to mtr_lat
## 	Call get_long with line and assign it to mtr_long
## Call get_dist_miles with arguments userLat, mtr_lat, userLong, mtr_long and assing it to\ dist_from_pt
## If  dist_from_pt < userRad
## 	Output_file.write(line + “\n”)
## Call Cont_prog() and assign it to keep_going
##
## ERROR HANDLING:
##          In the valid_input function handling ValueErrors to stop users from entering non-numeric input
##          In the file_input function handling IOError to stop users from entering bad file names
##          In the get_lat and get_long functions handling ValueErrors to stop the function from
##          crashing due to bad longitudes and latitudes in the users file
##
########################################################################

from math import radians, cos, sin, asin, sqrt

## gets file input and opens read or write file
def file_input(read_or_write,prompt):
    """Gets the input or output file and returns it to user"""
    while True:
        try:
            file_name = input(prompt)
            inFile = open(file_name,read_or_write,encoding = "utf-8")
            return inFile
        except IOError:
            print("Please enter a valid file name.")

## gets the latitude of a meteor landing
def get_lat(line):
    """takes a line from the input file and returns the latitude on that line"""
    try: 
        lat = float(line[-56:-41].strip())
        return lat
    except ValueError:
        return None

## gets the longitude of a meteor landing
def get_long(line):
    """takes a line from the input file and returns the longitude on that line"""
    try:
        long = float(line[-44:-26].strip())
        return long
    except ValueError:
        return None
    
## gets float input and returns it to user
def valid_input(prompt,valType):
    """Takes a prompt and variable type and returns valid user input"""
    while True:
        try:
            valid_input = valType(input(prompt))
            return valid_input
        except ValueError:
            print("Please enter a valid number.")


## calculates the distance in miles between two (lat,long) points and returns it to user
def get_dist_miles(lon1, lat1, lon2, lat2):
    """takes two lat,long points and returns the distance in miles between them"""

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # distance formula
    diffLong = lon2 - lon1
    diffLat = lat2 - lat1
    sqHalfCord = sin(diffLat/2)**2 + cos(lat1) * cos(lat2) * sin(diffLong/2)**2
    angularDist = 2 * asin(sqrt(sqHalfCord))
    miles = 3961 *angularDist
    return miles

## asks user if they would like to continue using the program
def cont_game():
    """asks the user if they would like to continue the program and returns a true or false value to the caller"""
    while True:
        cont = input("Would you like to continue Y/N ===>")
        if cont.upper() == "Y":
            return True
        elif cont.upper() == "N":
            return False
        else:
            print("Please enter Y or N!\n")


def main():
    keep_going = True
    while keep_going:
        ##open the files and set intitial conditions for the user-inputed variables
        mtr_file = file_input('r',"Enter the name of the input file ===>")
        output_file = file_input('w',"Enter the name of the output file ===>")
        userLat = 91
        userLong = 181
        userRad = -1

        ## all three loops make the user continue to enter input until they give valid input
        while userLat > 90 or userLat <-90:
            userLat = valid_input("Enter your lattitude ===>",float)

        while userLong > 180 or userLong <-180:
            userLong = valid_input("Enter your longitude ===>",float)

        while userRad <= 0:
            userRad = valid_input("Enter the radius for your search ===>",int)

        for line in mtr_file:
            ## the if makes sure the first line isn't used
            if "name" not in line:
                mtr_lat = get_lat(line)
                mtr_long = get_long(line)
                if mtr_lat != None and mtr_long != None:
                    dist_from_pt = get_dist_miles(userLong,userLat,mtr_long,mtr_lat)
                if dist_from_pt <= userRad:
                    print(dist_from_pt)
                    print(line,file=output_file)


        mtr_file.close()
        output_file.close()

        keep_going = cont_game()

main()



