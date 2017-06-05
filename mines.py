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
    long = 0
    mines_at = {}
    for l in range(0, length):
        wide = 0
        for w in range(0, width):
            count += 1
            if count in mines:
                try:
                    mines_at[long][wide] = True
                except KeyError:
                    mines_at[long] = {}
                    mines_at[long][wide] = True
            else:
                try:
                    mines_at[long][wide] = False
                except KeyError:
                    mines_at[long] = {}
                    mines_at[long][wide] = False
            wide += 1
        long += 1
    return(mines_at)


def draw_board(length, width, mines_at):
    for l in range(0, length):
        for w in range(0, width):
            if mines_at[l][w] is True:
                print '*',
            else:
                nearby_count = 0
                for checklong in l, l-1, l+1:
                    for checkwide in w, w-1, w+1:
                        try:
                            if mines_at[checklong][checkwide] is True:
                                nearby_count += 1
                        except KeyError:
                            pass
                if nearby_count == 0:
                    print '.',
                else:
                    print nearby_count,
        print


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
    mines_at = setmines(int(options.length),
                        int(options.width),
                        int(options.setmines))
    draw_board(int(options.length), int(options.width), mines_at)


if __name__ == '__main__':
    main()
