"""
Learning:
1. How to use Numbers in python 
2. Integers
3. Floating point

"""

myNumber = 13
print(myNumber)

# You can do some basic math such as add, subtract, divide and multiple

added = 2 + 2
print('I added two plus two and got: ', added)

subtracted = 2 - 2
print('I subtracted two minus two and got: ', subtracted)

multiplied = 2 * 2
print('I multiplied two times two and got: ', multiplied)

divided = 2 / 2
print('I divided two divided by two and got: ', divided)

#  Noticed that the value returned in added, subtracted and multiplied case was an integer
# When we divided 2/2, we go 1.0, or a floating point number 
# Floats are numbers that can have a decimal at any location

# What happens when I apply some math that includes an integer and a floating point number?

result = 2 + 2.0
print('My Result: ', result)

# Python respects order of operations

multiplyFirst = 5 + 10 * 2
print('What is my result: ', multiplyFirst)

addParentheses = (5 + 10) * 2
print('What happens with parentheses? ', addParentheses)