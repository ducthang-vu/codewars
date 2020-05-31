# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
# "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is
# irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and
# punctuation.


def is_pangram(s):
    lower_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    upper_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    for letter in lower_letters:
        if any([letter in s, upper_letters[lower_letters.index(letter)] in s]):
            continue
        else:
            return False
    return True


# SOLUTION:
# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())