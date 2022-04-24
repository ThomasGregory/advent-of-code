from utils import *
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

def read_input(myfile):
    '''reads the input file, and outputs:
        - the maximum size required on the matrix
        - a list of co-ordinates (hits)
        - a list of folds'''

    stringlist = input_to_list(myfile)
    lines = len(stringlist)
    pivot = stringlist.index('', lines//10) #guess that folding starts in the final 10% of the text for efficiency on long lists
    hitstring = stringlist[0:pivot]
    folds = stringlist[(pivot + 1): lines]

    xlist = [int(i.split(',')[0]) for i in hitstring]
    ylist = [int(i.split(',')[1]) for i in hitstring]
    hitlist = [xlist, ylist]

    size = [max(xlist), max(ylist)]

    return size, hitlist, folds


def create_grid(size, hitlist):
    '''generates a matrix of 1s (hits) and 0s representing the locations of the dots'''

    grid = np.zeros([size[1]+1, size[0]+1])
    for coord in range(0, len(hitlist[0])):
        grid[hitlist[1][coord], hitlist[0][coord]] = 1

    return grid


def do_fold(grid, fold, size):
    '''takes a grid and applies a fold'''

    f = fold.split(' ')[2].split('=')
    axis = f[0]
    line = int(f[1])

    pos = 0
    shape = np.shape(grid)

    if axis == 'x':

        for i in range(line, shape[1]):#could have refactored this better
            grid[:,(line - pos)] = np.ceil((grid[:, line + pos] + grid[:,(line - pos)])/2)
            pos += 1
        grid = grid[:,0:line]

    if axis == 'y':
        for i in range(line, shape[0]):
            grid[(line - pos),:] = np.ceil((grid[line + pos, :] + grid[line - pos, :])/2)
            pos += 1
        grid = grid[0:line, :]

    return grid


def solve_problem():
    '''carry out the problem'''

    size, hitlist, folds = read_input('inputs/13-hardmode.txt')
    mygrid = create_grid(size, hitlist)

    count = 0

    for i in folds:
        plt.imsave(f'fold_{count}.png', mygrid)
        count += 1
        print(f'\n \n now working on fold number {count} \n \n')
        mygrid = do_fold(mygrid, i, size)

    return mygrid, sum(sum(mygrid))


if __name__ == "__main__":
    startTime = time.time()
    print('testing...')
    s = solve_problem()[0]
    plt.imsave(f'hardmode.png', s)
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
