from utils import *
import pandas as pd


def column_bit(array, col=0, popularity='most'):
    '''find the most/least frequent bit in a given column'''

    most_likely = 1
    least_likely = 1 - most_likely

    values, counts = np.unique(array[:, col], return_counts=True)
    ind = np.argmax(counts)

    if popularity == 'most':
        return ind
    elif popularity == 'least':
        return 1 - ind


def epsilon_rate(array, mode = 'epsilon'):
    '''calculates the sequence of the most frequent bits for a given array,
    and turns this into a decimal epsilon rate. Calculates gamma_rate too'''

    most_freq_bits = [str(column_bit(array, col=i)) for i in range(0, np.shape(array)[1])]
    eps_rate = int("".join(most_freq_bits), 2)

    if mode == 'epsilon':
        return eps_rate

    elif mode == 'gamma':
        return 2**np.shape(array)[1] - eps_rate - 1


def oxygen_rating(myarray, mode = 'oxygen'):
    '''returns the oxygen generator rating when given an array of inputs'''

    df = pd.DataFrame(data=myarray)

    for i in range(0, np.shape(myarray)[1]):
        if mode == 'oxygen':
            colmode = df[i].mode().tolist()[-1]

        elif mode == 'carbon_dioxide':

            if len(df[i].mode()) > 1:
                colmode = '0'

            else:
                colmode = df[i].value_counts().idxmin()

        df = df[df[i] == colmode]

    bitlist = [df[i].mode()[0] for i in range(0, np.shape(myarray)[1])]
    oxy = int(''.join(bitlist), 2)

    return oxy


def solve_problem(myarray, part=1):
    '''solves problem 1: find the product of epsilon and gamma rates'''

    c = character_array(input_to_list(myarray))

    if part == 1:
        return epsilon_rate(c) * epsilon_rate(c, mode = 'gamma')

    elif part == 2:
        return oxygen_rating(c, mode = 'carbon_dioxide') * oxygen_rating(c)


if __name__ == "__main__":
    print('Solution to Problem 1 is: ' + str(solve_problem('inputs/3-input.txt', part = 1)))
    print('Solution to Problem 2 is: ' + str(solve_problem('inputs/3-input.txt', part = 2)))
