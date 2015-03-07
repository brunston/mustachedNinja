#-------------------------------------------------------------------------------
# Name:        doTwice
# Purpose:
#
# Author:      B Poon
#
# Created:     19 12 2013
# Copyright:   (c) B Poon 2013
# Licence:     CC BY-SA 4.0 Intl.
#-------------------------------------------------------------------------------
def doTwice(f,arg):
    f(arg)
    f(arg)
def printTwice(string):
    print(string)

doTwice(printTwice,"spam")
