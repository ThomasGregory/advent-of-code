from utils import *

def column_bit(array, col=0, popularity='most'):
    '''find the most/least frequent bit in a given column'''

    most_likely = 1
    least_likely = 1 - most_likely

    values, counts = np.unique(array[:, col], return_counts=True)
    print(values)
    print(counts)
    ind = np.argmax(counts)

    if popularity == 'most':
        return ind
    elif popularity == 'least':
        return 1 - ind

def epsilon_rate(array, mode = 'epsilon'):
    '''calculates the sequence of the most frequent bits for a given array,
    and turns this into a decimal epsilon rate. Calculates gamma_rate too'''
    print(np.shape(array)[1])
    most_freq_bits = [str(column_bit(array, col=i)) for i in range(0, np.shape(array)[1])]
    binary_eps = int("".join(most_freq_bits))
    print(binary_eps)


    if mode == 'epsilon':
        return eps_rate

    elif mode == 'gamma':
        return 2**len(array) - eps_rate




c = character_array(input_to_list('inputs/3-tutorial.txt'))
print(epsilon_rate(c))
