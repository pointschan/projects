__author__ = 'pointschan'


from control.words_games import  *
from nose.tools import *
import unittest


control_ListOfWords = ['wordOne', 'wordTwo', 'wordThree', 'wordFour', 'wordFive', 'wordSix', 'wordSeven', 'wordEight', 'wordExtraLong', 'wordNine', 'wordTen', 'wordEleven', 'wordExtraLong']
control_ListOfWordLength = [7, 7, 9, 8, 8, 7, 9, 9, 13, 8, 7, 10, 13]
control_LongestWordLength = 13
control_LongestWordsList = ['wordExtraLong', 'wordExtraLong']
control_WordsLongerThanNineCharacters =['wordExtraLong', 'wordEleven', 'wordExtraLong']



class words_gamesTestCase(unittest.TestCase):

    def testGetWordsListFromFile(self):
        testListOfWords = getListOfWordsFile("words_list.txt")
        self.assertEqual(testListOfWords, control_ListOfWords)

    def testMapListOfWordsToListOfWordsLength(self):
        testListOfWordsLength = mapListOfWordsToListOfWordsLength(control_ListOfWords)
        self.assertEqual(testListOfWordsLength, control_ListOfWordLength)

    def testfindLongestWords(self):
        testLongestWordsLength, testLongestWordsList = findLongestWords(control_ListOfWords)
        self.assertEqual(testLongestWordsLength, control_LongestWordLength)
        self.assertEqual(testLongestWordsList, control_LongestWordsList)

    def testFindWordsLongerThanN(self):
        testWordsLongerthanNList, n = findWordsLongerThanN(control_ListOfWords, 9)
        self.assertEqual(testWordsLongerthanNList, control_WordsLongerThanNineCharacters)






