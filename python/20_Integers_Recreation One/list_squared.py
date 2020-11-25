# Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum
# of the squared divisors is 2500 which is 50 * 50, a square!
#
# Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is
# itself a square. 42 is such a number.
#
# The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two
# elements, first the number whose squared divisors is a square and then the sum of the squared divisors.
#
# #Examples:
# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]


def find_divs(a):
    # given a, finds all divisors of a
    half_divs = [b for b in range(1, int(a ** 0.5) + 1) if (a/b).is_integer()]
    return set(half_divs + [int(a/b) for b in half_divs])


def list_squared(m, n):
    solution = []
    for a in range(m, n + 1):
        tot = sum([b**2 for b in find_divs(a)])
        if (tot**0.5).is_integer():
            solution.append([a, tot])
    return solution


# Not needed

def sum_of_squared_divs(a):
    # given integer a, finds divisors and return sum of the all of them squared
    return sum([b**2 for b in range(1, a + 1) if (a / b).is_integer()])