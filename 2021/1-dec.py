import numpy as np

def input_to_list(filename):
    '''takes text file input and converts it to a list of strings, with each
    line as its own element'''

    with open(filename) as f:
        return [line.strip('\n') for line in f]

def inputs_to_triple_sums(mylist):
    '''returns the 3-value forward sum of input list'''

    avg_list = [int(mylist[i]) + int(mylist[i+1]) + int(mylist[i+2]) for i in
    range(0, len(mylist)-2)]
    #avg_list[0] = int(mylist[0])
    #avg_list[1] = (int(mylist[0])+int(mylist[1]))/2

    return avg_list

def input_to_changes(depthlist):
    '''returns the list of changes
    from the input list. 1st value dropped, as no comparison viable

    i.e. [1, 2, 5, 3] -> [1, 3, -2]'''

    return [int(depthlist[i])-int(depthlist[i-1]) for i in range(1, len(depthlist))]

def count_increases(changelist):
    '''outputs the number of positive values in the input list'''

    return sum([x > 0 for x in changelist])

def problem1(filename):
    '''reads in a textfile and produces the answer to problem 1 as a string'''

    return str(count_increases(input_to_changes(input_to_list(filename))))

def problem2(filename):
    '''reads in a textfile and produces the answer to problem 2 as a string'''

    return str(count_increases(input_to_changes(inputs_to_triple_sums(input_to_list(filename)))))

if __name__ == "__main__":
    print('number of increases is ' + problem1('input_1.txt'))
    print('number of increases using 3-value trailing averages is ' + problem2('input_1.txt'))
