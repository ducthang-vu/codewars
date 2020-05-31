from is_interesting import all_digit_equal, all_digit_0_but_first, increasing_digits, \
    decreasing_digits, is_palindrome, is_interesting_array, is_interesting_one_number, is_interesting


print('\n\t\tCheck if number formed by only one digit')
print(all_digit_equal(5))
print(all_digit_equal(555))
print(all_digit_equal(625))
print(all_digit_equal(98))
print(all_digit_equal(99))

print('\n\t\tCheck if number is x000')
print(f'should be True: {all_digit_0_but_first(500)}')
print(f'should be False: {all_digit_0_but_first(760)}')
print(f'should be True: {all_digit_0_but_first(8000)}')
print(f'should be True: {all_digit_0_but_first(98)}')
print(f'should be True: {all_digit_0_but_first(99)}')


print('\n\t\tCheck if number is 12345..')
print(f'should be False: {increasing_digits(500)}')
print(f'should be True: {increasing_digits(123)}')
print(f'should be False: {increasing_digits(1232345)}')
print(f'should be True: {increasing_digits(567890)}')
print(f'should be False: {increasing_digits(45678901)}')

print('\n\t\tCheck if number is 54321..')
print(f'should be False: {decreasing_digits(500)}')
print(f'should be True: {decreasing_digits(321)}')
print(f'should be False: {decreasing_digits(654354321)}')
print(f'should be True: {decreasing_digits(543210)}')
print(f'should be False: {decreasing_digits(54321098)}')


print('\n\t\tCheck if number is palindrone..')
print(f'should be False: {is_palindrome(500)}')
print(f'should be True: {is_palindrome(12321)}')
print(f'should be False: {is_palindrome(123455432)}')
print(f'should be True: {is_palindrome(12344321)}')
print(f'should be False: {is_palindrome(5676567876)}')

print('\n\t\tCheck if number is in array')
print(f'should be False: {is_interesting_array(500, [250, 5000, 50])}')
print(f'should be True: {is_interesting_array(12321, [50, 25, 12321, 90])}')
print(f'should be False: {is_interesting_array(432, [4321, 2345, 43.2])}')
print(f'should be True: {is_interesting_array(12344321, [15, 57, 12344321])}')
print(f'should be False: {is_interesting_array(5676567876, [])}')


print('\n\t\tCheck if number ok for the problem')
print(f'should be 0: {is_interesting_one_number(97, [250, 5000, 50])}')
print(f'should be 0: {is_interesting_one_number(4312, [4321, 2345, 43.2])}')
print(f'should be 2: {is_interesting_one_number(12344321, [15, 57])}')
print(f'should be 2: {is_interesting_one_number(7890, [])}')
print(f'should be 2: {is_interesting_one_number(12344321, [15, 57, 12344321])}')
print(f'should be 2: {is_interesting_one_number(5000, [])}')
print(f'should be 2: {is_interesting_one_number(573, [50, 25, 573, 90])}')
print(f'should be 0: {is_interesting_one_number(100, [250, 5000, 50])}')
print(f'should be 0: {is_interesting_one_number(100, [100, 5000, 50])}')


print('\n\t\tTesting solution')
print(is_interesting(98, []))