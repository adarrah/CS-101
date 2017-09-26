########################################################################
## CS 101
## Program #3
## Aaron Darrah
## add522@mail.umkc.edu
##
## PROBLEM: Finding a string that perfectly matches another string using random strings spliced together
##
## ALGORITHM :
##IInitialize score_list and word_list
##Set test_string to Hello World
##Start a for loop for count to 500
##	random_word is “”
##	random_score is 0
##	for char in the length of test_string
##		make letter a random character
##add letter to the end of random_word
##	add random_word to word_list
##	for char in length of test_string
##add the absolute value of the difference between test_string and random_word at\ char to score
##	add score to the end of score_list
##initialize parent1 and parent2 and best_word to “”
##set MIN to sys.maxsize
##set MIN2 to 0
##while test_string != best_word:
##	for cnt in range to 500:
##		if score_list at cnt is less than MIN:
##			parent1 is word_list at cnt
##			MIN is score_list at cnt
##		else if cnt == 0
##			parent2 is word_list at cnt
##			MIN2 is score_list at cnt
##		else if score_list at cnt is less than MIN2
##			parent2 is word_list at cnt
##			MIN2 is score_list at cnt
##	For cnt in range to 500
##		New_word = “”
##		For char in range to the length of parent1
##			Random_letter is random.random()
##			Random_parent is random.random()
##			Mutation is random.random
##If mutation is less than .1
##				Add a random character to new_word
##			If random_parent is less than .5
##				If random_letter is less than .5
##Add a letter that is one character higher than parent1 at char\ to new_word
##				Else
##Add a letter that is one character lower than parent1 at char\ to new_word
##			Else
##If random_letter is less than .5
##Add a letter that is one character higher than parent2 at char\ to new_word
##				Else
##Add a letter that is one character lower than parent2 at char\ to new_word
##
##
##
## ERROR HANDLING: None
##
########################################################################

import random
score_list = []
word_list = []
test_string = "Hello World"
length = len(test_string)
new_word = ""

print("Attempting to breed {:<}".format(test_string))
print("Generating strings now")
#loop to generate five hundred random strings
for cnt in range(500):
    random_word = ""
    score = 0
    #generates a word full of random characters
    for char in range(len(test_string)):
        random_word +=chr(random.randint(32,126))

    #calculate the score of random_word
    for char in range(len(test_string)):
        score += abs(ord(test_string[char])-ord(random_word[char]))

    #add the word and score to their respective lists
    word_list.append(random_word)
    score_list.append(score)
avg_score = int((sum(score_list)/500))

belowAvg = []
for k in range(len(score_list)):
	if score_list[k] < avg_score:
		belowAvg.append(word_list[k])

best_score = score_list.index(min(score_list))
best_string = word_list[best_score]

print("The best so far: {:^} Score:{:^5}".format(best_string,best_score))

while best_string != test_string:
    word_list = []
    score_list = []
    new_word = ""
    for cnt in range(500):
        parent1 = belowAvg[random.randint(0,len(belowAvg)-1)]
        parent2 = belowAvg[random.randint(0,len(belowAvg)-1)]

        for char in range(len(parent1)):
            random_letter = random.random()
            random_parent = random.random()
            mutation      = random.random()
            if random_parent < .5:
                character = parent1[char]
            else:
                character = parent2[char]

            if mutation < .01:
                if ord(character) == 126:
                    character = chr(ord(character)-1)
                elif ord(character) == 32:
                    character = chr(ord(character)+1)
                elif random_letter < .5:
                    character = chr(ord(character)-1)
                else:
                    character = chr(ord(character)+1)
            new_word += character

        for char in range(len(test_string)):
            score += abs(ord(test_string[char]) - ord(new_word[char]))

        # add the word and score to their respective lists
        word_list.append(new_word)
        score_list.append(score)

    avg_score = int((sum(score_list) / 500))

    belowAvg = []
    for k in range(len(score_list)):
        if score_list[k] < avg_score:
            belowAvg.append(word_list[k])

best_score = score_list.index(min(score_list))
best_string = word_list[best_score]

print("The best so far: {:^} Score:{:^5}".format(best_string,best_score))
