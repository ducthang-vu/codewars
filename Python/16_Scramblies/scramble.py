# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to
# match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered
# Input strings s1 and s2 are null terminated.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2):
    return True if all(s2.count(char) <= s1.count(char) for char in set(s2)) else False

# SOLUTION
# def scramble(s1,s2):
#     for c in set(s2):
#         if s1.count(c) < s2.count(c):
#             return False
#     return True


# More difficult in case the problem does not specify wich string have to be rearrange with the other (see notes):

def scramble_2(s1, s2):
    return True if all(s1.count(char) <= s2.count(char) for char in set(s1)) or all(s2.count(char) <= s1.count(char)
                                                                                    for char in set(s2)) else False


