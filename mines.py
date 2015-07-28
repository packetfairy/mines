#!/usr/bin/python

import random
import argparse


def getrandnum(maxnumber, mines):
    mynumber = random.randint(0, maxnumber)
    if mynumber in mines:
        return(getrandnum(maxnumber, mines))
    else:
        return(mynumber)


def setmines(length, width, setmines):
    totalspaces = length * width
    mines = []
    for m in range(0, setmines):
        mines.append(getrandnum(totalspaces, mines))
    count = 0
    for l in range(0, length):
        for w in range(0, width):
            if count in mines:
                print '*',
            else:
                print '.',
            count += 1
        print ''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', action='store',
                        help='board length')
    parser.add_argument('-w', '--width', action='store',
                        help='board width')
    parser.add_argument('-m', '--mines', action='store', dest='setmines',
                        help='number of mines on the board')
    options = parser.parse_args()
    if not options.length:
        options.length = raw_input('enter board length: ')
    if not options.width:
        options.width = raw_input('enter board width: ')
    if not options.setmines:
        options.setmines = raw_input('enter number of mines: ')
    setmines(int(options.length), int(options.width), int(options.setmines))


if __name__ == '__main__':
    main()
