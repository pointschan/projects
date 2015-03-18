__author__ = 'pointschan'

import os
from random import randint

file_location =  "/home/vagrant/workspaces/projects/app/docs/"
fn = "words_list.txt"

#Write a program that maps a list of words into a
#list of integers representing the lengths of the corresponding words.
def getListOfWordsFile(filename):
    a = ''
    b = []
    try:
        f = open(os.path.join(file_location, filename))
    except IOError:
        print "%s file not found" % filename
    else:
        for line in f:
            if not a:
                a = (line.rstrip('\n'))
            else:
                a = a + ',' + (line.rstrip('\n'))
        b = a.split(',')
        f.close()
        return b

def mapListOfWordsToListOfWordsLength(templist):
    listOfInts = []
    for i in range(len(templist)):
        listOfInts.append(len(templist[i]))
    return listOfInts


def mapListOfWordsToListOfWordsLengthWithListComprehensionMethod(templist):
    """
    the above function can be done in 1 line, to use list comprehension
    """
    LC_listOfInts = [len(x) for x in templist]
    return LC_listOfInts

#Write a function find_longest_word() that takes a list of words and returns the length of the longest one
def findLongestWords(templist):
    tmpLongestWordsList = []
    tmpLongestWordLength = 0
    for member in templist:
        if len(member)==tmpLongestWordLength:
            tmpLongestWordsList.append(member)
        elif len(member) > tmpLongestWordLength:
            tmpLongestWordLength = len(member)
            tmpLongestWordsList=[]
            tmpLongestWordsList.append(member)
    return tmpLongestWordLength, tmpLongestWordsList

#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
def findWordsLongerThanN(tmplist, n):
    tmpWordsLongerthanNList = []
    for member in tmplist:
        if len(member) > n:
            tmpWordsLongerthanNList.append(member)
    return tmpWordsLongerthanNList, n

#List of words:['wordOne', 'wordTwo', 'wordThree', 'wordFour', 'wordFive', 'wordSix', 'wordSeven', 'wordEight', 'wordNine', 'wordTen']
listOfWords = getListOfWordsFile(fn)
listOfWordsLength = mapListOfWordsToListOfWordsLength(listOfWords)
LC_lowl = mapListOfWordsToListOfWordsLengthWithListComprehensionMethod(listOfWords)
longestWordLength, listOfWordsLongestWords = findLongestWords(listOfWords)
wordsLongerThanNList, n = findWordsLongerThanN(listOfWords,randint(6,len(listOfWords)))


print ("List of words:"+str(listOfWords))
print ("List of wordlength:"+str(listOfWordsLength))
print ("List of wordlength LC: "+str(LC_lowl))
print ("Longest Word length:"+' '+str(longestWordLength)+' '+str(listOfWordsLongestWords))
print ("n="+str(n)+' '+str(wordsLongerThanNList))

