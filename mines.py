#!/usr/bin/python

import Miner
import argparse


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
    miner = Miner.setmines(length=int(options.length),
                           width=int(options.width),
                           minecount=int(options.setmines))
    miner.draw_board(miner.placemines())

if __name__ == '__main__':
    main()
