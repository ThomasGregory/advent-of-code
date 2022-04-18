from utils import *
import numpy as np
import pandas as pd

def read_input(input):
    '''reads the input file, and outputs:
        - the maximum size required on the matrix
        - a list of co-ordinates (hits)
        - a list of folds'''

    raise NotImplementedError

    return n, hits, folds

def create_grid(n, hits):
    '''generates a matrix of 1s (hits) and 0s representing the locations of the dots'''

    raise NotImplementedError

    return grid

def do_fold(grid, fold):
    '''takes a grid and applies a fold'''

    raise NotImplementedError

    return grid

def solve_problem():
    '''carry out the problem'''

    raise NotImplementedError

    return solution
