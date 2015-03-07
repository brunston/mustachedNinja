#-------------------------------------------------------------------------------
# Name:        grid
# Purpose: creates a grid per thinkpython
#
# Author:      B Poon
#
# Created:     20 12 2013
# Copyright:   (c) B Poon 2013
# Licence:     CC BY-SA 4.0
#-------------------------------------------------------------------------------

def gridDiv(partitionsNum,betweenNum):
    betStr = "-"*betweenNum
    carryStr ="+" + betStr
    endStr = carryStr*partitionsNum + "+"
    return endStr
def midDiv(columns, size):
    sizeStr = " "*size
    columnsStr = "|"+sizeStr
    final = columnsStr*columns + "|"
    return final
def printer(rowNum, colNum,sizeNum):
    for i in range(rowNum):
        print(gridDiv(colNum,sizeNum))
        for i in range(sizeNum):
            print(midDiv(colNum,sizeNum))
    print(gridDiv(colNum,sizeNum))
def main(intWarn): #doesn't work because of input being stored as str not int
    if intWarn is False:
        row = input("Rows? ") #how to make input an integer ie purge str and convert.
        col = input("Columns? ")
        size = input("Size? ")
    else:
        print("Please enter integers as params.")
        row = input("Rows? ")
        col = input("Columns? ")
        size = input("Size? ")
    printer(row, col, size)


main(True)
