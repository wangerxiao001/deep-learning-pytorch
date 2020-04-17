#write on 17/04/2020
import os
import sys

def addfilesuffix(in_file, suffix, outfile):
    '''
    :param in_file: this is the file list needed to add suffix, can be .txt file
    :param suffix: this is the suffix to add
    :param outfile: the file to store the suffix-added file list
    :return: file name list with suffix

    >>> python addsuffix.py train.txt .xml trainsuffix1.txt
    trainsuffix1.txt
    '''
    with open(in_file, "r+") as f1:
        file = open(outfile, "w")  #open file for write mode
        if not file:
            print("cannot open the file %s for writing" % outfile)
        for name in f1:
            name = name.split('\n')[0]   #can be adjusted
            file_name = name + suffix  # add suffix
            file.write(file_name + "\n")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('3 auguments are need.')
        exit(1)
    addfilesuffix(sys.argv[1], sys.argv[2], sys.argv[3])

