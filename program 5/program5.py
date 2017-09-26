########################################################################
##
## CS 101
## Program #5
## Aaron Darrah
## add522@mail.umkc.edu
##
## PROBLEM : To figure out which person the mystery speechs are most alike with
##
## ALGORITHM :
##Create a function remove_punct that takes arguments line and punct_list
##	Assign 0 to idx
##	While idx < length of line
##		For char in line
##			If char is in punct_list
##				Line = line.replace(char,””)
##			Else
##				Add one to idx
##	Return line.lower()
##Create a function next_word that takes arguments line and begin_idx
##	Word = “”
##	While idx is less than length of line
##		If line at begin_idx does not equal “ “ and begin_idx is less than length of line
##			Add char to word
##			Add one to begin_idx
##		Else
##			Add one to beg_idx
##			Return word,beg_idx
##Create a function isStop that takes arguments word and stop_list
##	If word is in stop_list
##		Return True
##	Else
##		Return False
##Create a function called convert_to_dict that takes arguments file_name and fileName_dict
##assign the opening of filename for reading to inFile + “.txt”
##	for line in inFile:
##		idx = 0
##		newLine = remove_punt(line)
##		while idx is less than the length of newline
##			nextWord,idx = next_word(newline, idx)
##			if the opposite of isStop:
##				if word in fileName_dict
##					add one to fileName_dict at word
##				else
##					set fileName_dict at word to one
##create a function called total_words that takes argument speech_dict:
##	totalWords = 0
##	for word in speech_dict
##		add word[-1] to totalWords
##	return totalWords
##create a function called shared_words that takes arguments comp_speech and speech_dict:
##	commonWords is 0
##for word in speech_dict
##		if word[0] in comp_speech
##			add one to commonWords
##	return commonWords
##create a function called find_rms_freq that takes arguments speech_dict and comp_speech and sharedWords
##	freq_sum is 0
##	total1 = total_words(speech_dict)
##	total2 = total_words(comp_speech)
##	for word in speech dict
##		if word[0] in comp_speech
##			add square root of the absolute value of word[-1] divided by total1 – comp_speech[word[0]][-1] divided by total2 to freq_sum
##	return the square root of freq_sum divided by sharedWords
##Make dictionarys for all of the texts called fileName_dict and add them to a list called dict_list
##file_list = [“mystery1”,”mystery2”,’mystery3’,”mystery4”,”Romney”,”Obama”,”Clinton”,”Trump”]
##for dict,index in enumerate dict_list
##	convert_to_dict(file_list at index, dict)
##
##outerCounter is 0
##innerCounter is 4
##while outerCounter is less than or equal to 3
##	word_commonality is []
##	rel_freq is []
##	speech_dict is dict_list at outerCounter
##	while innerCounter is less than or equal to 8
##		comp_speech is dict_list at innerCounter
##		sharedWords  is shared_words(comp_speech,speech_dict)
##		distinctWords is length of comp_speech + length of speech_dict – sharedWords
##		add sharedWords/distinctWords to word_commonality
##		add find_rms_freq(speech_dict,comp_speech,sharedWords) to rel_freq
##	assign max of word_commonality to mostCommon
##	assign the index of mostCommon to commIndex
##	assign the min of rel_freq to bestFreq
##	assign the index of bestFreq to freqIndex
##	print(“The text {} has the highest word commonality with {} {}” formatted with file_list at outerCounter, file_list at commIndex + 4, mostCommon)
##	print(“The text {} has the highest frequency similarity with {} {}” formatted with file_list at outerCounter, file_list at freqIndex + 4, bestFreq)
##
## ERROR HANDLING: None
##
########################################################################
import math

def create_dicts(dict_list,file_list):

    idx = 0
    for dictionary in dict_list:
        inFile = open(file_list[idx] + ".txt")
        speech_list =[]
        for line in inFile:
            speech_list += remove_punct(line.strip()).lower().split(" ")
        remove_punct(speech_list)
        for item in speech_list:
            if item not in STOPWORDS:
                try:
                    dictionary[item] += 1
                except KeyError:
                    dictionary[item] = 1
        idx +=1
def remove_punct(line):
    new_line = ""
    for char in line:
        if char not in ".!:;,-_?":
            new_line += char
    return new_line

def total_words(dictionary):
    ttlWords = 0
    for word in dictionary:
        ttlWords += dictionary[word]
    return ttlWords

def shared_words(speech,comp_speech):
    comp_list = list(comp_speech)
    commonWords = 0
    for word in speech:
        if word in comp_list:
            commonWords += speech[word]
    return commonWords

def find_rms_freq(speech,comp_speech,ttlSharedWords):
    freq_sum = 0
    total1 = total_words(speech)
    total2 = total_words(comp_speech)
    speech_list = list(speech)
    comp_list = list(comp_speech)
    for word in speech_list:
        if word in comp_list:
            freq_sum += math.pow(speech[word]/total1 - speech[word]/total2,2)
    return math.sqrt(freq_sum/ttlSharedWords)



stopText = open("stopWords.txt")
STOPWORDS = stopText.read().strip()

mystery1 = {}
mystery2 = {}
mystery3 = {}
mystery4 = {}
obama = {}
romney = {}
clinton = {}
trump = {}

dict_list = [mystery1, mystery2, mystery3, mystery4, obama, romney, clinton, trump]
file_list = ["mystery1","mystery2","mystery3","mystery4","obama","romney","clinton","trump"]

create_dicts(dict_list,file_list)

def main():
    outerCounter = 0
    innerCounter = 4
    while outerCounter <= 3:
        word_commonality_list = []
        freq_list = []
        speech_dict = dict_list[outerCounter]
        while innerCounter <= 7:
            comp_dict = dict_list[innerCounter]
            sharedWords = shared_words(speech_dict,comp_dict)
            distinctWords = len(list(comp_dict)) + len(list(speech_dict)) - sharedWords
            word_commonality_list.append(sharedWords/distinctWords * 100)
            freq_list.append(find_rms_freq(speech_dict, comp_dict, sharedWords))
            innerCounter += 1
        innerCounter = 4
        outerCounter += 1

        mostCommon = max(word_commonality_list)
        commIndex = word_commonality_list.index(mostCommon)
        bestFreq = min(freq_list)
        freqIndex = freq_list.index(bestFreq)

        print("The text {} has the highest word commonality with {}: {:.6}%".format(file_list[outerCounter],file_list[commIndex + 4],mostCommon))
        print("The text {} has the highest frequency similarity with {}: {:.4f}".format(file_list[outerCounter], file_list[freqIndex + 4], bestFreq))
        print()

main()