from utils import *
import numpy as np
import pandas as pd

def solve_problem(filename, part=2):
    '''creates a pandas dataframe with all the necessary info at each step
    leaves working columns explicit for readability'''

    df = stringlist_to_dataframe(input_to_list(filename)) #turn text file to df

    df['aim_adjustment'] = np.zeros(len(df))
    df['horiz_adjustment'] = np.zeros(len(df))

    #I'm not iterating here, promise

    df.loc[df[0] == 'down', 'aim_adjustment'] = df[df[0] == 'down'][1]
    df.loc[df[0] == 'up', 'aim_adjustment'] = -df[df[0] == 'up'][1]
    df.loc[df[0] == 'forward', 'horiz_adjustment'] = df[df[0] == 'forward'][1]

    df['aim'] = df['aim_adjustment'].cumsum()
    df['depth_adjustment'] = df['aim']*df['horiz_adjustment']

    final_aimed_depth = df['depth_adjustment'].sum() #depth for part 2
    final_naive_depth = df['aim_adjustment'].sum() #depth for part 1
    final_horizontal = df['horiz_adjustment'].sum()

    if part == 1:
        return final_naive_depth * final_horizontal
    elif part == 2:
        return final_aimed_depth * final_horizontal


if __name__ == "__main__":
    print('Solution to Problem 1 is: ' + str(solve_problem('inputs/2-input.txt', part = 1)))
    print('Solution to Problem 2 is: ' + str(solve_problem('inputs/2-input.txt', part = 2)))
