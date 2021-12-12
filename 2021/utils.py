import numpy as np
import pandas as pd

def input_to_list(filename):
    '''takes text file input and converts it to a list of strings, with each
    line as its own element (created for 1-dec)'''

    with open(filename) as f:
        return [line.strip('\n') for line in f]


def stringlist_to_dataframe(stringlist):
    '''takes a list of strings. for each string, produces a sublist of strings
    when this the string is split on spaces, and in turn converts this into a
    pandas dataframe - a table, in some sense. Numerical strings are converted
    to floats'''

    df = pd.DataFrame(data=np.array([i.split() for i in stringlist]))

    return df.apply(pd.to_numeric, errors = 'ignore')


def character_array(stringlist):
    '''takes a list of strings. for each string, produces a sublist of characters,
    and in turn converts this into a numpy array. they're still strings'''

    return np.array([list(j[0]) for j in ([i.split() for i in stringlist])])
