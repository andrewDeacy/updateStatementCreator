__author__ = 'adeacy'
import re
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write('input = ' + line.lower())