#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 03:45:37 2017

@author: jameswalker
"""
x = int(input('Enter an interger: '))
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')
    

# Compound Booleans
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
z = float(input("Enter a number for z: "))
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("therefore, x / y is", x/y)
    if y != 0:
        print("therefore, x / y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("thanks!")