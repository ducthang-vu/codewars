# Range Extraction

# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

# A format for expressing an ordered list of integers is to use a comma separated list of either
#   - individual integers
#   - or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
#     The range includes all integers in the interval including both endpoints. It is not considered a range unless it
#     spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted
# string in the range format.


def solution(args):
    result = []
    temp = {
        'range': [args[0]],
        'asc': None,
    }

    def add_to_result():
        if len(temp['range']) >= 3:
            to_add = [temp['range'][0]] if temp['range'][0] == temp['range'][-1] else [temp['range'][0],
                                                                                       temp['range'][-1]]
            result.append('-'.join(map(str, to_add)))
        else:
            result.append(','.join(map(str, temp['range'])))
        temp['range'] = [item]
        temp['asc'] = None

    for item in args[1:]:
        try:
            last = temp['range'][-1]
            if temp['asc'] is None:
                if item == last + 1:
                    temp['asc'] = True
                    temp['range'].append(item)
                elif item == last - 1:
                    temp['asc'] = False
                    temp['range'].append(item)
                else:
                    add_to_result()
            elif temp['asc']:
                if item == last + 1:
                    temp['asc'] = True
                    temp['range'].append(item)
                else:
                    add_to_result()
            else:
                if item == last - 1:
                    temp['asc'] = False
                    temp['range'].append(item)
                else:
                    add_to_result()
        except IndexError:
            temp['range'].append(item)

    add_to_result()
    return ','.join(result)


# solution:
# from itertools import groupby
#
# def solution(args):
#    grps = ([v[1] for v in g] for _,g in groupby(enumerate(args), lambda p: p[1]-p[0]))
#    return ','.join('{}{}{}'.format(g[0],'-'if len(g)>2 else',',g[-1])
#        if len(g)>1 else str(g[0]) for g in grps)
