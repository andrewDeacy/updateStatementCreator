__author__ = 'adeacy'
import re
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    table = input('Enter the name of the table you would like to update')
    column = input('Enter the name of the column you would like to update') #multiple column update to come in the future
    value = input('Enter the value you would like to set the column to')
    outfile.write('Update ' + table)
    outfile.write('Set ' + column + '= ' + value)
    outfile.write('Where ')
    
    for line in infile:
        outfile.write('input = ' + line.lower())