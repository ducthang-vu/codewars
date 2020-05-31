# Write the function that parses the mileage number input,and returns a 2 if the number is "interesting" (see below),
# a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.
#
# "Interesting" Numbers
# Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
#
# Any digit followed by all zeros: 100, 90000
# Every digit is the same number: 1111
# The digits are sequential, incementing†: 1234
# The digits are sequential, decrementing‡: 4321
# The digits are a palindrome: 1221 or 73837
# The digits match one of the values in the awesome_phrases array
# † For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
# ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
#
# So, you should expect these inputs and outputs:
#
# # "boring" numbers
# is_interesting(3, [1337, 256])    # 0
# is_interesting(3236, [1337, 256]) # 0
#
# # progress as we near an "interesting" number
# is_interesting(11207, []) # 0
# is_interesting(11208, []) # 0
# is_interesting(11209, []) # 1
# is_interesting(11210, []) # 1
# is_interesting(11211, []) # 2
#
# # nearing a provided "awesome phrase"
# is_interesting(1335, [1337, 256]) # 1
# is_interesting(1336, [1337, 256]) # 1
# is_interesting(1337, [1337, 256]) # 2
# Error Checking
# A number is only interesting if it is greater than 99!
# Input will always be an integer greater than 0, and less than 1,000,000,000.
# The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks
# numbers spell funny words...)
# You should only ever output 0, 1, or 2.

def all_digit_equal(number):
    # Every digit is the same number: 1111
    return True if len(set(list(str(number)))) == 1 else False


def all_digit_0_but_first(number):
    # Any digit followed by all zeros: 100, 90000
    return True if set(list(str(number)[1:])) == {'0'} else False


def increasing_digits(number):
    # The digits are sequential, incementing: 1234; 0 is 10
    new_array = [10 if int(n) == 0 else int(n) for n in list(str(number))]
    return False if any(value != new_array[key - 1] + 1 for key, value in enumerate(new_array[1:], start=1)) else True


def decreasing_digits(number):
    # The digits are sequential, decrementing: 4321; 0 should come after 1
    new_array = [int(n) for n in list(str(number))]
    return False if any(value != new_array[key - 1] - 1 for key, value in enumerate(new_array[1:], start=1)) else True


def is_palindrome(number):
    # The digits are a palindrome: 1221 or 73837
    return True if list(str(number))[:int(len(list(str(number))) / 2)] == \
                   (list(str(number)))[::-1][:int(len(list(str(number))) / 2)] else False


def is_interesting_array(number, array):
    # The digits match one of the values in the awesome_phrases array
    return True if number in array else False


def is_interesting_simple(number, awesome_phrases):
    return True if all_digit_equal(number) or all_digit_0_but_first(number) or increasing_digits(number) or \
                   decreasing_digits(number) or is_palindrome(number) or \
                   is_interesting_array(number, awesome_phrases) else False


def is_interesting(number, awesome_phrases):
    # A number is only interesting if it is greater than 99!
    if number < 98:
        return 0
    elif 98 <= number <= 99:
        return 1
    else:
        if is_interesting_simple(number, awesome_phrases):
            return 2
        else:
            if any(is_interesting_simple(n, awesome_phrases) for n in [number + 1, number + 2]):
                return 1
            else:
                return 0


# Optimize version:

def is_interesting_opt_compacted(number, awesome_phrases):
    return 2 if is_interesting_simple(number, awesome_phrases) and number >= 100 \
        else 1 if any(is_interesting_simple(n, awesome_phrases) for n in [number + 1, number + 2]) and number >= 98 \
        else 0