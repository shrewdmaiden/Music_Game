__author__ = 'gregory'
''' quiz_dictionary_style101.py
using a keyword:definitions_list dictionary for a flashcard-like quiz
tested with Python27 and Python33  by  vegaseat  08nov2013
'''
import random
# make string input work with Python2 or Python3
try: input = raw_input
except: pass
# a simple sample dictionary 'pick the right color'
# keyword:[def1, def2, def3, correct_def_ix]
# could use module pickle to dump/load this dictionary
mydict = {
'sun' : ['black', 'yellow', 'blue', 1],
'water' : ['red', 'white', 'blue', 2],
'grass' : ['white', 'green', 'orange', 1],
'coal' : ['black', 'purple', 'red', 0]
}
keyword_list = list(mydict.keys())
# shuffle the keywords in place
random.shuffle(keyword_list)
print('Pick the right color:')
correct = 0
wrong = 0
for keyword in keyword_list:
    sf = '''\
{}
A) {}
B) {}
C) {}
'''
    print(sf.format(keyword, mydict[keyword][0],
                    mydict[keyword][1],mydict[keyword][2]))
    letter = input("Enter letter of your choice (A B C): ").upper()
    if letter == 'ABC'[mydict[keyword][3]]:
        print('correct')
        correct += 1
    else:
        print('wrong')
        wrong += 1
    print('-'*30)
# final
sf = "Answers given --> {} correct and {} wrong"
print(sf.format(correct, wrong))