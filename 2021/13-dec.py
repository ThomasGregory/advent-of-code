from utils import *
import numpy as np
import pandas as pd

def read_input(myfile):
    '''reads the input file, and outputs:
        - the maximum size required on the matrix
        - a list of co-ordinates (hits)
        - a list of folds'''

    c = input_to_list(myfile)
    lines = len(c)
    pivot = c.index('', lines//10) #guess that folding starts in the final 10% of the text for efficiency on long lists
    hitstring = c[0:pivot]
    folds = c[(pivot + 1): lines]

    xlist = [int(i.split(',')[0]) for i in hitstring]
    ylist = [int(i.split(',')[1]) for i in hitstring]
    hitlist = [xlist, ylist]

    size = [max(xlist), max(ylist)]

    return size, hitlist, folds


def create_grid(size, hitlist):
    '''generates a matrix of 1s (hits) and 0s representing the locations of the dots'''

    gridzz = np.zeros(size[0], size[1])
    print(gridzz)

    #raise NotImplementedError

    #return grid


def do_fold(grid, fold):
    '''takes a grid and applies a fold'''

    raise NotImplementedError

    return grid


def solve_problem():
    '''carry out the problem'''

    size, hitlist, folds = read_input('inputs/13-tutorial.txt')
    mygrid = create_grid(size, hitlist)



    raise NotImplementedError

    return solution

if __name__ == "__main__":
#    print('Solution to Problem 1 is: ' + read_input('inputs/13-tutorial.txt'))
#    print('Solution to Problem 2 is: ' + str(solve_problem('inputs/5-tutorial.txt', part = 2)))
    print('testing...')