#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import unittest
from collections import OrderedDict

class TestFileParsing(unittest.TestCase):
    fileName = 'testwords'
    lines = ['Love love love \n' , 'Love love love \n', 'There\'s nothing you can do that can\'t be done! \n']
    
    def setUp(self):
        #Create test file with known contents
        testFile = open(self.fileName,'w')
        testFile.write(self.lines[0]);
        testFile.write(self.lines[1]);
        testFile.write(self.lines[2]);
        testFile.close();

    def testNonExistentFile(self):
        words = parse_file(' ')
        self.assertTrue(len(words)==0)
        
    def testRealFile(self):
        words = parse_file(self.fileName)
        
        #sanity check!
        self.assertTrue(len(words)>0)
        
        #check contents
        trueWords = self.lines[0].split() + self.lines[1].split() + self.lines[2].split()
        self.assertTrue(words==trueWords)

class TestWordCounting(unittest.TestCase):
    testWords = ['the','quick','fox','fox','jumped','jumped','jumped']
    
    def testCounting(self):
        wordCount = count_words(self.testWords)
        self.assertTrue(wordCount[self.testWords[0]]==1);
        self.assertTrue(wordCount[self.testWords[1]]==1);
        self.assertTrue(wordCount[self.testWords[2]]==2);
        self.assertTrue(wordCount[self.testWords[4]]==3);

def count_words(words):
    wordCount = {};
    
    for word in words:
        if word in wordCount:
            wordCount[word] +=1;
        else:
            wordCount[word] = 1;


    return wordCount


def print_words(filename):
    '''
        /name   print_words
        /brief  Prints the words in lexigraphically sorted order
                with the wordcount. 
        /param  words - the list of words to be processed.
    '''
    words = parse_file(filename)
    wordCount = count_words(words)

    for word in wordCount:
        'Word: {0} count: {1}'.format(word,wordCount[word])
    
    return
  
def print_top(filename):
    '''
        /name   print_top
        /brief  Prints the top20 most occuring words in words
        /param  words - the list of words to be processed
    '''
        
    words = parse_file(filename)
    wordCount = count_words(words)
    
    #Create sorted tuple
    orderedDict = OrderedDict(sorted(wordCount.items(),key=lambda t: t[1],reverse=True))
    count = 0;
    for word in orderedDict:
        if(count < 20):
            print('Word: %s Count: %d' % (word,orderedDict[word]))
            count +=1
    return

def parse_file(filename):
    '''
        /name   parse_file
        /brief  parses the file at the path given, and returns a list of words in it
        /param  filename - the path of the file to be parsed
    '''
    words = []
    
    #1. Open file
    try:
        wordFile = open(filename,'r')    
    except IOError:
        print('No such file!')
        return words

    #2 Get lines of testfile
    lines = list(wordFile)
    
    #3. Create "giant" list of words
    for line in lines:
        wordsInLine = line.split()
        words += wordsInLine
    
    #3. Return list with contents
    return words
    



# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():

  
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  #unittest.main()
  main()
