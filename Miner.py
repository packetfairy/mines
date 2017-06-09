import random


class setmines:
    def __init__(self, length=10, width=10, minecount=10):
        self.length = length
        self.width = width
        self.minecount = minecount
        self.totalspaces = self.length * self.width


    def placemines(self):
        '''uses the predefined length, width, and minecount, to return a
           dictionary of dictionaries in the form of {l: {w: T/F}}, which will
           be used to draw the board (ie: T=mine, F=emptyspace)'''
        mines = []
        count = 0
        mines_at = {}
        for m in range(0, self.minecount):
            mines.append(self.getrandnum(maxnumber=self.totalspaces,
                                         mines=mines))
        atlong = 0
        for l in range(0, self.length):
            atwide = 0
            for w in range(0, self.width):
                count += 1
                if count in mines:
                    try:
                        mines_at[atlong][atwide] = True
                    except KeyError:
                        mines_at[atlong] = {}
                        mines_at[atlong][atwide] = True
                else:
                    try:
                        mines_at[atlong][atwide] = False
                    except KeyError:
                        mines_at[atlong] = {}
                        mines_at[atlong][atwide] = False
                atwide += 1
            atlong += 1
        return(mines_at)


    def draw_board(self, mines_at):
        '''parses the dictionary returned by placemines. draws the board
           according to the following rules:
           
           . in empty spaces with no adjacent mines
           * in spaces occupied by a mine
           digits 1-8 in spaces adjacent to 1-8 mines'''
        for l in range(0, self.length):
            for w in range(0, self.width):
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


    def getrandnum(self, maxnumber, mines):
        '''takes a maximum number (ie: the total number of spaces) and an
           array of integers as inputs, and returns another integer which is
           not currently within the array'''
        mynumber = random.randint(0, maxnumber)
        if mynumber in mines:
            return(self.getrandnum(maxnumber=maxnumber, mines=mines))
        else:
            return(mynumber)
