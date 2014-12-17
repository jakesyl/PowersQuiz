#!/usr/bin/env python

from random import randint

while True:
    choose = randint(1,2)
    number = randint(2,14)
    if number>10:
        exponent = 2
    elif number<10 and number>6:
        exponent=3
    elif number<6 and number>3:
        exponent = 4
    else:
        exponent=4
        
    if choose == 1:
        #why doesn't python have a switch case?
        #end = "th"
        if exponent == 2:
            end = "nd"
        elif exponent == 3:
            end = "rd"
        elif exponent>4:
            end = "th"
        
        print str(exponent) + end +  " root of " + str(number**exponent)
        answer = input("Please enter your answer: ")
        if answer!=number:
            print "Wrong, the answer was " + str(number)
        else:
            print "correct!"
    else:
        print str(number) + "^" + str(exponent)
        answer = input("what is the result of these two numbers: ")
        if answer!=(number**exponent):
            print "Wrong, the answer was  " + str(number**exponent)
        else:
            print "correct"