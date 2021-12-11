def input_to_list(filename, test=False):
    '''takes text file input and converts it to a list of strings, with each
    line as its own element'''

    if test:
        return [199, 200, 208, 210, 200, 207, 240, 269, 260, 2]
    else:
        with open(filename) as f:
            return [line.strip('\n') for line in f]

def depths_to_changes(depthlist):
    '''returns the list of changes
    from the previous depth entry. Initial value is 0'''

    depthlist[0] = 0
    return [int(depthlist[i])-int(depthlist[i-1]) for i in range(1, len(depthlist))]

def count_increases(changelist):
    '''outputs the number of increases in the depthlist. This is equivalent to
    returning the number of positive values in the changelist'''

    return sum([x > 0 for x in changelist])

def problem1(filename):
    '''reads in a textfile and produces the answer to problem1 as a string'''

    return str(count_increases(depths_to_changes(input_to_list(filename))))

if __name__ == "__main__":
    print('number of increases is ' + problem1('input_1.txt'))
