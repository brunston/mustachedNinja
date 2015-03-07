#-------------------------------------------------------------------------------
# Name:        Right justify
# Purpose: Justifies text right
#
# Author:      B Poon
#
# Created:     19 12 2013
# Copyright:   (c) B Poon 2013
# Licence:     CC BY-SA 4.0 Intl.
#-------------------------------------------------------------------------------

def rightJustify(actString):
    strlen = len(actString)
    repeat = " " #to move over string
    moveover = 70-strlen
    newString = repeat*moveover + actString
    print(newString)

carrystr = input("String?")
rightJustify(carrystr)