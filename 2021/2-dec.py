from utils import *
import numpy as np
import pandas as pd

# def sum_categories(dataframe, category):
#     '''takes a 2-column pandas dataframe and sums the column 2 values of the given
#     column 1 category'''
#
#     return dataframe[dataframe[0] == category][1].sum()


# def problem1(filename, startpoint=[0,0]):
#     '''takes in the filename of the input .txt, and outputs the solution to
#     problem 1 as an integer'''
#
#     s = stringlist_to_dataframe(input_to_list(filename))
#     horizontal_endpoint = startpoint[0] + sum_categories(s, 'forward')
#     vertical_endpoint = startpoint[1] + sum_categories(s, 'down') - sum_categories(s, 'up')
#
#     return horizontal_endpoint * vertical_endpoint


def solve_problem(filename, part=2):
    '''creates a column showing the effect of any given row on the aim. expects
    non-zero categories to be up or down'''

    df = stringlist_to_dataframe(input_to_list(filename))
    df['aim_adjustment'] = np.zeros(len(df))
    df['horiz_adjustment'] = np.zeros(len(df))

    #I'm not iterating here, promise

    df.loc[df[0] == 'down', 'aim_adjustment'] = df[df[0] == 'down'][1]
    df.loc[df[0] == 'up', 'aim_adjustment'] = -df[df[0] == 'up'][1]
    df.loc[df[0] == 'forward', 'horiz_adjustment'] = df[df[0] == 'forward'][1]

    df['aim'] = df['aim_adjustment'].cumsum()
    df['depth_adjustment'] = df['aim']*df['horiz_adjustment']

    final_aimed_depth = df['depth_adjustment'].sum()
    final_naive_depth = df['aim_adjustment'].sum()
    final_horizontal = df['horiz_adjustment'].sum()

    if part == 1:
        return final_naive_depth * final_horizontal
    elif part == 2:
        return final_aimed_depth * final_horizontal


# def problem2(filename):
#     '''takes in the filename of the input .txt and returns the solution
#     to problem 2. it's a big loop because we need information from
#     the previous row, but iterrows is slow so a dataframe may no longer be
#     the best solution'''
#
#     df = aim_column(stringlist_to_dataframe(input_to_list(filename)))
#
#     # df[df[0] = 'forward'] * df[df['aim']] =
#
#     print(aim_column(df))
#
#
#     return 117





if __name__ == "__main__":
    print('Solution to Problem 1 is: ' + str(solve_problem('inputs/2-tutorial.txt', part = 1)))
    print('Solution to Problem 2 is: ' + str(solve_problem('inputs/2-tutorial.txt')))
