#!/usr/bin/env python3
'''
Utility which returns a list of the 100 most common three word sequences (phrases) from a given text
'''
import sys
import string
from collections import defaultdict 

def process_text(file):
    # convert to lower case
    text = file.lower()

    # convert to ascii - removes /u characters
    text = text.encode("ascii", "ignore").decode()

    # remove line breaks  - Line Feed and Carriage Return
    text = text.replace("\n"," ")
    text = text.replace("\r"," ")

    # remove puncutation
    # translate faster than alternative methods: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    # static list used instead of string.punctuation so ' is not eliminated for contractions
    text = text.translate(str.maketrans('', '', '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'))

    # split into list by using spaces
    words=text.split(" ")

    # filter empty strings
    words=list(filter(None, words))

    # count the frequency of each 3 word phrase group
    phrase_counts = phrase_frequency(words,3)

    # sort the top 100 phrases
    top_phrases = sort_phrase_counts(phrase_counts,100)

    # print the counts of the top 100 phrases
    print_counts(top_phrases)

def phrase_frequency(word_list,group_size):
    # initialize a default dictionary to increment counts of reused phrases
    phrase_counts = defaultdict(int)
    #iterate through the list of words
    for i in range(len(word_list)-1):
        # select group_size words at a time and increment the counter for each unique tuple
        phrase_counts[tuple(word_list[i : i + group_size])]+=1
    return phrase_counts

def sort_phrase_counts(phrase_counts,top_n):
    # sorts the list of phrases which have already been counted by frequency
    top_phrases = sorted(phrase_counts.items(), key=lambda t: (-t[1], t[0]))[:top_n]
    return top_phrases

def print_counts(top_phrases):
    # prints the results for the provided phrase set (3 word tuple + count of frequency)
    for phrase in top_phrases:
        print(" ".join(phrase[0]) + " " + str(phrase[1]))


if __name__ == '__main__':
    # retrive the current script name, to be used for help/usage
    script = sys.argv[0]
    # the rest of the arguments are expected to be 1 or more filenames
    filenames = sys.argv[1:]
    # if filenames are specified concatinate the contents and process the text
    if len(filenames) >=1:
        read_data=""
        for file in filenames:
            #print ("Processing %s :" % file)
            with open(file,'r') as afile:
                read_data += afile.read()
        process_text(read_data)
    else:
        if not sys.stdin.isatty():
            # no file names specified, process the text of stdin if not tty (terminal)
            #print ("Processing stdin:")
            process_text(sys.stdin.read())   
        else:
            # no file names specified and no stdin, print help information
            print ("\nUtility which returns a list of the 100 most common three word sequences from a given text\n\nUsage: python3 %s file1.txt file2.txt ...\n" % script)
