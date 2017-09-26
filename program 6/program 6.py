########################################################################
##
## CS 101
## Program 6
## Aaron Darrah
## add522@mail.umkc.edu
##
## PROBLEM : The problem was to open a user given directory of PPM files and use them to tile a new image that is the composite of strips from the images in the directory
##
## ALGORITHM :
##open an out_file for writing
##initialize a ppm_list
##for file in file_list:
##    image = open(directory + "\\" + file)
##    get the height and width of the file using a small for loop to run to the second line and split the line into the variables
##    initialize and image_list
##    for idx,line in enumerate(image):
##        if the idx is greater than 0:
##            append the line to the image_list
##    append the image_list to the ppm_list
##hmake height the integer value of height
##make width the integer value of width
#print the ppm header to the out_file
##assign the length of the ppm_list to num_strips
##for row in a range from 0 to the height
##    for strip in range from 0 to the num_strips
##        assign ppm_list at strip to ppm
##        for idx in the range from (strip * int((width * 3 /num_strips))) to ((strip + 1) * int((width * 3 / num_strips)))
##            print the ppm at row times teh width times 3 plus the index to the out_file
##
## ERROR HANDLING:
##      None
##
########################################################################

import os

##Asks the user whether they would like to use the program or quit
def runProgram():
    """Asks the user whether they would like to use the program or quit, returns true if they want to continue and false if they don't"""
    while True:
        print("Welcome to the image slicer. You can provide a directory that has several images of the same size,\nand this program will take equal vertical slices out of each\nand construct a new image.\n")
        user_input = input("1.Slice a PPM image\n2.Quit\n\n===> ")
        if user_input == "1":
            return True
        elif user_input == "2":
            return False
        else:
            print("You must enter either 1 or 2")

##gets user input and opens output file
def getOutputFile():
    """Asks the user for the name of the output file, opens it and returns the file"""
    while True:
        try:
            file_name = input("Enter the file to save the ppm to ==>")
            file = open(file_name,'w')
            return file
        except IOError:
            print("Could not open {} for write access. Please try another file.".format(file_name))

##opens the directory the user gives and returns the directory name and a list of the file_names of files in the directory
def openDirectory():
    """opens the directory the user gives and returns the directory name and a list of the file_names of files in the directory"""
    while True:
            directory = input("Please enter the name of the dircetory you want to use ===>")
            if os.path.isdir(directory):
                file_list = os.listdir(directory)
                idx = 0
                while idx < len(file_list):
                    ##removes non ppm files from the file list
                    if ".ppm" not in file_list[idx]:
                        file_list.remove(file_list[idx])
                        idx -= 1
                    idx += 1
                return file_list, directory
            else:
                print('That directory doesn\'t exist')

## takes a ppm_file and returns the height and width of the file as a tuple
def getStripHeightWidth(ppm_file):
    """takes a ppm_file and returns the height and width of the file as a tuple"""
    for idx,line in enumerate(ppm_file):
        if idx == 1:
            height,width = line.split(" ")
            return height,width

## compares all the files in a directory to check that they are compatible with each other returns true if they are and false if they aren't
def compareDirectoryFiles(file_list,directory):
    """compares all the files in a directory to check that they are compatible with each other returns true if they are and false if they aren't"""
    height_list = []
    width_list = []
    bitdepth_list = []
    firstLine_list = []
    standard_list = []
    good_dir = True

    for file in file_list:
        image = open(directory + "\\" + file)
        for idx,line in enumerate(image):
            if idx == 0:
                firstLine_list.append(line.strip())
            if idx == 1:
                height,width = line.split(" ")
                height_list.append(height)
                width_list.append(width)
            if idx == 2:
                bitdepth_list.append(line.strip())
    for idx in range(len(file_list)):
        if idx == 0:
            standard_list.append(firstLine_list[idx])
            standard_list.append(height_list[idx])
            standard_list.append(width_list[idx])
            standard_list.append(bitdepth_list[idx])
            standard_list.append(int(height_list[idx]) * int(width_list[idx]) - 1)
        else:
            if firstLine_list[idx] != standard_list[0]:
                print("{} does not have {} as its first line".format(file_list[idx],firstLine_list[idx]))
                good_dir = False
            if height_list[idx] != standard_list[1]:
                print("{} does not have the same width {} as {}".format(file_list[idx],standard_list[1],file_list[0]))
                good_dir = False
            if width_list[idx] != standard_list[2]:
                print("{} does not have the same width {} as {}".format(file_list[idx], standard_list[2], file_list[0]))
                good_dir = False
            if bitdepth_list[idx] != standard_list[3]:
                print("{} does not have a bitdepth of {}".format(file_list[idx],standard_list[3]))
                good_dir = False
            if (int(height_list[idx]) * int(width_list[idx]) - 1) != standard_list[4]:
                print("{} does not have the correct number of pixels, {} X {} != {}".format(file_list[idx],height_list[idx],width_list[idx],standard_list[4]))
                good_dir = False
    return good_dir
run_program = runProgram()

while run_program:
    file_list, directory = openDirectory()
    height = width = 0
    good_dir = compareDirectoryFiles(file_list,directory)
    out_file = getOutputFile()
    ppm_list = []
    if good_dir:
        for file in file_list:
            image = open(directory + "\\" + file)
            height, width = getStripHeightWidth(image)
            image_list = []
            for idx,line in enumerate(image):
                if idx > 0:
                    image_list.append(line.strip())
            ppm_list.append(image_list)

        height = int(height)
        width = int(width)

        print("P3\n{} {}\n255".format(height,width),file = out_file)
        num_strips = len(ppm_list)
        for row in range(height):
            for strip in range(num_strips):
                ppm = ppm_list[strip]
                for idx in range((strip * int((width * 3 /num_strips))),((strip + 1) * int((width * 3 / num_strips)))):
                    print(ppm[row*width*3 + idx],file = out_file)
    else:
        print("The files in the directory you gave were not good and we couldn't run the program please try again")
    run_program = runProgram()




