#!/usr/bin/python
# -*- coding:utf-8 -*-

#gettysburg address analysis
#count words,unique words,common words

def makeWordList(gFile):
    """Create a list of words from the file."""
    speech = []

    for lineString in gFile:
        lineList = lineString.split()
        for word in lineList:
            word = word.lower()
            word = word.strip('.,')
            if word != "--":
                speech.append(word)
    return speech

def makeUnique(speech):
    """Create a list of unique words."""
    unique = [] #list of unique words:initialized to be empty

    for word in speech:
        if word not in unique:
            unique.append(word)
    return unique

gFile = open("gettysburg.txt","rU")
speech = makeWordList(gFile)

print "Length:",len(speech)

unique = makeUnique(speech)
print unique
print "Length:",len(unique)
