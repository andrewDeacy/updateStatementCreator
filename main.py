__author__ = 'adeacy'
import re
with open("testData.txt") as infile, open("output.txt", "w") as outfile:
    table = input('Enter the name of the table you would like to update')
    column = input('Enter the name of the column you would like to update') #multiple column update to come in the future
    value = input('Enter the new value of that column')
    where = input('Enter the name of column in the datasheet')
    outfile.write('Update ' + table + '\n')
    outfile.write('Set ' + column + ' = ' + value + '\n')
    outfile.write('Where ')
    first = 0
    for line in infile:
        if first == 0:
            outfile.write(where + ' = ' + line.lower())
            first = 1
        else:
            outfile.write('or ' + where + ' = ' + line.lower())
            first = 1