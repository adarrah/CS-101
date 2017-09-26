########################################################################
##
## CS 101
## Program #7
## Aaron Darrah
## add522@mail.umkc.edu
##
## PROBLEM :
##          The user wants to be able to search for some words and see the relative frequency of their use every year compared to another word in their selected range of time

## ERROR HANDLING:
##      Check for TypeError in getUserInput()
##      Check to make sure users words are in the all_words.csv file in wordInFile()
##
## OTHER COMMENTS:
##      The program will take a long time to process between the first and second words if your word is in the latter half of the alphabet, I apologize
##
########################################################################

import csv

 ## opens the csv file passed in
def openFile(filename):
    """Takes a csv filename, opens the file, opens it as csv file and returns it"""
    file = open(filename)
    csv_file = csv.reader(file)
    return csv_file, file

## Prints the opening menu and asks the user is they would like to run the ngram program or quit
def runAgain():
    """Prints the opening menu and asks the user is they would like to run the ngram program or quit"""
    while True:
        print("{:^36}\n{:^36}\n{:^36}\n".format("Ngram Viewer","1. Run Ngram Program","2. Quit"))
        cont = input("==> ")

        if cont == "1":
            return True
        elif cont == "2":
            return False
        else:
            print("That's not one of the options, select 1 or 2")

 ## Fills an empty dictionary with instances of the target word
def storeCSV(csv_file, csv_dict,word,lower_bound,upper_bound):
    """Takes a csv_file an empty dictionary and a target word and fills the dictionary with keys that are the year and the values are the number of times the word was used that year"""

    ## iterates over the csv file
    for line in csv_file:

            ## if the word at the 0 index of the line is the same as the word and its between the bounds it stores the number of instances in the dictionary at the year
            if line[0] == word and int(line[1]) >= lower_bound and int(line[1]) <= upper_bound:
                csv_dict[int(line[1])] = int(line[2])

 ## Fills an empty dictionary with the word counts for every year in a range
def storeTotalWords(word_count_dict, yearly_words_file, lower_bound, upper_bound):
    """Takes an empty dictionary and yearly word count file and fills the dictionary with the total words for every year between the two bounds"""

    for line in yearly_words_file:
        ## if the year at 0 index of line is in the range it stores the total words at the year in the dictionary
        if int(line[0]) >= lower_bound and int(line[0]) <= upper_bound:
            word_count_dict[int(line[0])] = int(line[1])


 ## Takes a prompt and data type, asks the user the prompt and returns the result
def getUserInput(prompt,type = str):
    """Takes a prompt and data type, asks the user the prompt and returns the result"""

    while True:
        try:
            user_input = type(input(prompt))
            return user_input

        except:
            print("That input was not valid.\n")

 ## Chekcs to see if the given word is in the given file
def wordInFile(word,file):
    """Takes a word and a file and looks for the word in the file. Returns true if it is an false if it is not."""

    file.seek(0)
    csv_file = csv.reader(file)

    ##iterates over the file
    for line in csv_file:
        ##chekcs to see if the first list value of the line(the word) is the same as the users word
        if line[0] == word:
            return True

    ## resets the starting point in the file
    all_words_file.seek(0)


def getWords():
    """Asks the user what words they would like to compare and if they are in the file returns them to the user in a tuple"""

        ## gets the words from the users
    word1 = getUserInput("Enter the first word to get frequencies ==> ",str)
    while not wordInFile(word1,all_words_file):
        print("{} was not found, try another word.".format(word1))
        word1 = getUserInput("Enter the first word to get frequencies ==> ", str)

    word2 = getUserInput("Enter the first word to get frequencies ==> ",str)
    while not wordInFile(word2,all_words_file):
        print("{} was not found, try another word.".format(word2))
        word2 = getUserInput("Enter the first word to get frequencies ==> ", str)

    return word1,word2



## Asks the user what range of years they would like to use and returns them in a tuple
def getBounds(lower_bound = 1505,upper_bound = 2008):
    """Asks the user what range of years they would like to use and returns them in a tuple"""

    lower_bound = getUserInput("Enter the year to start with ==> ",int)
    while lower_bound < 1505 or lower_bound > 2008:
        print("The year cannot be less than 1505 or greater than 2008")
        lower_bound = getUserInput("Enter the year to start with ==> ", int)

    upper_bound = getUserInput("Enter the year to end at ==> ",int)
    while upper_bound > 2008 or upper_bound < 1505 or upper_bound < lower_bound:
        print("The year cannot be more than 2008, less than 1500 or lower than the lower bound.")
        upper_bound = getUserInput("Enter the year to end at ==> ", int)

    return lower_bound,upper_bound

##takes both user words their dictionaries and a year and returns the relative frequency of each word together in a tuple
def getRelFreq(word1,word2,word1_dict, word2_dict,yearly_word_ttl_dict ,year):
    """takes both user words their dictionaries and a year and returns the relative frequency of each word together in a tuple"""

    ##sets the word frequencies to the amount in that year and if there isn't an entry it is set to 0
    word1_freq = word1_dict.get(year,0)
    word2_freq = word2_dict.get(year,0)
    year_ttl = yearly_word_ttl_dict.get(year,1)

    ## calculates relative frequencies
    word1_rel_freq = word1_freq/year_ttl * 100
    word2_rel_freq = word2_freq/year_ttl * 100

    return word1_rel_freq, word2_rel_freq
run_ngram = runAgain()
while run_ngram:
    ## initialize the dictionaries to store the words
    word1_dict = {}
    word2_dict = {}
    yearly_word_ttl_dict ={}

    ## open the all_words file the user gives
    all_words_csv,all_words_file  = openFile("all_words.csv")

    ## opens the total_counts file the user gives
    total_counts_csv,total_counts_file  = openFile("total_counts.csv")

    ## gets the two words to be used
    word1,word2 = getWords()
    ## gets the upper and lower bound
    lower_bound,upper_bound = getBounds()

    ## stores the words in their dictionaries
    all_words_file.seek(0)
    storeCSV(all_words_csv, word1_dict, word1, lower_bound, upper_bound)
    all_words_file.seek(0)
    storeCSV(all_words_csv, word2_dict,word2,lower_bound,upper_bound)

    ## stores the total word count values for the years in the user's range
    storeTotalWords(yearly_word_ttl_dict,total_counts_csv,lower_bound,upper_bound)

    print("{:^36}".format("Ngram Results"))
    print("  {:<10}{:^12}{:^12}".format("Year",word1,word2))
    print("="*36)
    for year in range(lower_bound,upper_bound+1):
        word1_rel_freq,word2_rel_freq = getRelFreq(word1,word2,word1_dict,word2_dict,yearly_word_ttl_dict, year)
        print("  {:<8}{:^12.6f}{:^12.6f}".format(year,word1_rel_freq,word2_rel_freq))

    all_words_file.close()
    total_counts_file.close()

    run_ngram = runAgain()