stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
std_pos = stdform.find('x10^')
mantissa = stdform[:std_pos]
# print(mantissa)
exponent = stdform[std_pos+4:]
# print(exponent)
result = mantissa + 'E' + exponent
print(f'This number in E notation is {result}.')