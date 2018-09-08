#!/usr/bin/python
# Comprehension example

# Set the range of numbers to between 0 and 49
numbers = range(0,50)

# Print the range of numbers
print numbers

# Set a variable to pring only even numbers in the range. 
# The i % 2 gives the remainder after the integer division (when dealing with only integers such as in this case, otherwise a common type) of i/2. The % is called the modulo operator. Of course when the remainder is 0, the number is even.
even_numbers = [i for i in range (0,50) if i % 2 == 0 and i >=2 ]

# Print the even numbers
print even_numbers

# Get the square of all the even numbers
squares = [i*i for i in numbers if i % 2 == 0 and i >=2]

# Print the square of all the even numbers
print squares

# Import the random module
import random

# Create a range of random numbers
random_numbers = [ random.randint(1,100) for x in range(50) ]
print random_numbers

# Create a list of unique random numbers from the range above
unique_random_numbers = list(set(random_numbers))
print unique_random_numbers


