from utils import *
import numpy as np
import pandas as pd
import time

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

    # print(size)
    # print(hitlist)
    # print(folds)

    return size, hitlist, folds


def create_grid(size, hitlist):
    '''generates a matrix of 1s (hits) and 0s representing the locations of the dots'''

    grid = np.zeros([size[1]+1, size[0]+1])
    for coord in range(0, len(hitlist[0])): #!!for loop!!
        grid[hitlist[1][coord], hitlist[0][coord]] = 1

    return grid


def do_fold(grid, fold, size):
    '''takes a grid and applies a fold'''

    f = fold.split(' ')[2].split('=')
    axis = f[0]
    line = int(f[1])

    if axis == 'y':
        altgrid = np.fliplr(grid)
    if axis == 'x':
        altgrid = np.flipud(grid)

    print(line)
    print(size)
    print(grid)
    print(axis)
    pos = 0


    # if axis == 'y':
    #     for j in range(line, size[1]+1):
    #         print(j)
    #         grid[(line - j):,:] = np.ceil((grid[j:,:] + grid[(size[1] - j):,:]) / 2)
    #         print(grid)

    # if axis == 'x':
    #     print('\n boop \n')
    #     for i in range(line, size[0]+1):
    #         print(f'pos is {pos}')
    #         grid[:,(line - pos)] = np.ceil((grid[:, line + pos] + grid[:,(line - pos)])/2)
    #         #print(grid)
    #         pos += 1
    #     grid = grid[:,0:line]
    #     #print(grid)
    #
    # if axis == 'y':
    #     print('\n boop \n')
    #     for i in range(line, size[1]+1):
    #         print(f'pos is {pos}')
    #         grid[(line - pos),:] = np.ceil((grid[line + pos, :] + grid[line - pos, :])/2)
    #         #print(grid)
    #         pos += 1
    #     grid = grid[0:line, :]
    #     #print(grid)


    if axis == 'x':
        print('\n boop \n')
        for pos in range(0, size[0]+1-line):
            print(f'pos is {pos}')
            grid[:,(line - pos)] = np.ceil((grid[:, line + pos] + grid[:,(line - pos)])/2)
            #print(grid)
        grid = grid[:,0:line]
        #print(grid)

    if axis == 'y':
        print('\n boop \n')
        for i in range(0, size[1] + 1 - line):
            print(f'pos is {pos}')
            grid[(line - pos),:] = np.ceil((grid[line + pos, :] + grid[line - pos, :])/2)
            #print(grid)
        grid = grid[0:line, :]
        #print(grid)

    return grid


def solve_problem():
    '''carry out the problem'''

    size, hitlist, folds = read_input('inputs/13-input.txt')
    mygrid = create_grid(size, hitlist)

    count = 0

    for i in folds:
        count += 1
        print(f'\n \n now working on fold number {count} \n \n')
        mygrid = do_fold(mygrid, i, size)


    # mygrid = do_fold(mygrid, folds[0], size)
    # print('\n \n warning! one fold only!\n \n')


    return mygrid, sum(sum(mygrid))

if __name__ == "__main__":
    startTime = time.time()
#    print('Solution to Problem 1 is: ' + read_input('inputs/13-tutorial.txt'))
#    print('Solution to Problem 2 is: ' + str(solve_problem('inputs/5-tutorial.txt', part = 2)))
    print('testing...')
    print(solve_problem()[0])
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
