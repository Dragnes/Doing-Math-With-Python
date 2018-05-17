# Doing Math With Python Text


# Chapter 1: pg 1-22

# Working with Fractions
from fractions import Fraction
f = Fraction(3, 4)   #Fraction(numerator, denominator)
Fraction(3, 4)+ 1 + 1.5
Fraction(3, 4) + 1 + Fraction(1, 4)


# Complex Numbers
a = 2 + 3j
type(a)

a = complex(2, 3)
b = 3 + 3j
a+b
a-b
a*b
a**b
a/b

z = 2 + 3j
z.real
z.imag
z.conjugate()

'To find the magnitude of a complex number'
(z.real ** 2 + z.imag ** 2) ** 0.5
abs(z)

a = '1'
int(a) + 1
int('1') + 1
int('1.0') + 1  # returns an error


# Handling Exceptions and Invalid Input
a = 3/4
a = input()
try:
    a = float(input('Enter a number: '))
except ValueError:
    print('You entered an invalid number')

a = input('Input an integer: ')
a = int(input())
a + 1

a = int(input())
'when inputting a float number (1.0 or 4.2) an error will be returned'
4.2.is_integer()
1.0.is_integer()


# Franctions and Complex Numbers as Inputs
a = Fraction(input('Enter a fraction: '))
'input 3/4 as well as 3/0' #3/0 well return an error (ZeroDivisionError)
try:
    a = Fraction(input('Enter a fraction: '))
except ZeroDivisionError:
    print('Invalid fraction')

z = complex(input('Enter a complex number: '))


# Writing Programs that do the Math for you (is number 'a' a facator of 'b')
def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False
print(is_factor(4, 1024))

'examples of range functions, range funtion will be used to write a function that finds factors of an integer'
for i in range(4):
    print(i)
for i in range(1, 4):
    print(i)
for i in range(0, 10, 2):
    print(i)
for i in range(1, 10, 2):
    print(i)  

'''
Find the Factors of an integer.
'''
def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print(i)
if __name__ == '__main__':
    b = input('Your Number Please: ')
    b = float(b)
    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print('Please enter a positive integer')

'''
Another way to find Factors
'''
from functools import reduce
n = int(input('Your Number Please: '))
def factors(n): 
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
print(factors(n))


# Generating Multiplication Tables
'Lets dig into to .format() method which will be used.'
item1 = 'apples'
item2 = 'bananas'
item3 = 'grapes'
print('At the store, I picked up some {0} and {1} and {2}.'.format(item1, item2, item3))

'''
Multiplication table printer
'''
def multi_table(a):
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(a, i, a*i))
if __name__ == '__main__':
    a = input('Enter a number: ')
    multi_table(float(a))

'''
Ever so slight different way for multiplication table printer
'''    
a = int(input('Enter a number: '))  # int or float
def multi_table(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))
print(multi_table(a))

'Practice with format() method'
'{0}'.format(1.25456)
'{0:.2f}'.format(1.25456)
'{0:.2f}'.format(1.25556)
'{0:.2f}'.format(1)


# Converting Units of Measurement
'''
Unit converter: Miles and Kilometers
'''
def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))
def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))
if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()


# Finding the Roots of a Quadratic Equation
'''Solve the following quadratic eqation: x^2 + 2x + 1 = 0'''
a = 1
b = 2
c = 1
D = (b**2 - 4*b*c)**0.5
x_1 = (-b + D)/(2*a)
x_2 = (-b - D)/(2*a)
'''
Quadratic equation root calculator
'''
def roots(a, b, c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    print('x_1: {0}'.format(x_1))
    print('x_2: {0}'.format(x_2))
if __name__ == '__main__':
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    roots(float(a), float(b), float(c))

'Ever so slight simpler code'    
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
def roots(a, b, c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    print('x_1: {0}'.format(x_1))
    print('x_2: {0}'.format(x_2))
print(roots(a, b, c))


# Chapter 1 Programming Challenges pages 22-26

# 1) Even-Odd Vending Machine

number = int(input('Enter an integer: '))        
def even_odd_vending(num):
    if (num % 2) == 0:
        print('Even')
    else:
        print('Odd')
    count = 1
    print(num)
    while count <= 9:
        num += 2
        print(num)
        count += 1
print(even_odd_vending(number))


# 2) Enhanced Multiplication Table Generator

'''
Method 1
'''
a = int(input('Multiplication table of what number?  '))  # int or float
b = int(input('Multiples up to how many times? '))
def multi_table(a,b):
    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))
print(multi_table(a,b))    

'''
Method 2 = more aligned with the text
'''
def multi_table(a, b):
    for i in range(1,b+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))
if __name__ == '__main__':
    a = int(input('Multiplication table of what number? '))
    b = int(input('Multiples up to how many times? '))
    multi_table(a, b)


# 3) Enhanced Unit Converters

'''
Method 1
''' 
print('1. Kilometers to Miles')
print('2. Miles to Kilometers')
print('3. Kilograms to Pounds')
print('4. Pounds to Kilograms')
print('5. Celsius to Fahrenheit')
print('6. Fahrenheit to Celsius')
choice = input('Which conversion would you like to do?: ')
if choice == '1':
    kilometers = float(input('Enter distance in kilometers: '))
    miles = kilometers / 1.609
    print('Distance in miles: {0}'.format(miles))
elif choice == '2':
    miles = float(input('Enter distance in miles: '))
    kilometers = miles * 1.609
    print('Distance in kilometers: {0}'.format(kilometers))
elif choice == '3':
    kilograms = float(input('Enter weight in kilograms: '))
    pounds = kilograms * 2.205
    print('Weight in pounds: {0}'.format(pounds))
elif choice == '4':
    pounds = float(input('Enter weight in pounds: '))
    kilograms = pounds / 2.205
    print('Weight in kilograms: {0}'.format(kilograms))
elif choice == '5':
    celsius = float(input('Enter the temperature in celsius: '))
    fahrenheit = (9/5)*celsius + 32
    print('Temperature in fahrenheit: {0}'.format(fahrenheit))
else:
    fahrenheit = float(input('Enter the temperature in fahrenheit: '))
    celsius = (fahrenheit - 32)*(5/9)
    print('Temperature in celsius: {0}'.format(celsius))

'''
Method 2 = more aligned with the text
'''
def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')  
def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))
def miles_km():
    miles = float(input('Enter distane in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))
def kg_pounds():
    kg = float(input('Enter weight in kilograms: '))
    pounds = kg * 2.205
    print('Weight in pounds: {0}'.format(pounds))
def pounds_kg():
    pounds = float(input('Enter weight in pounds: '))
    kg = pounds / 2.205
    print('Weight in kilograms: {0}'.format(kg))
def celsius_fahrenheit():
    celsius = float(input('Enter temperature in celsius: '))
    fahrenheit = (9/5)*celsius + 32
    print('Temperature in fahrenheit: {0}'.format(fahrenheit))
def fahrenheit_celsius():
    fahrenheit = float(input('Enter temperature in fahrenheit: '))
    celsius = (fahrenheit - 32)*(5/9)
    print('Temperature in celsius: {0}'.format(celsius))
if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    if choice == '3':
        kg_pounds()
    if choice == '4':
        pounds_kg()
    if choice == '5':
        celsius_fahrenheit()
    if choice == '6':
        fahrenheit_celsius()
        

# 4) Fraction Calculator

'''
Method 1
''' 
from fractions import Fraction

op = input('Operation to preform - Add, Subtract, Divide, Multiply: ')
a = Fraction(input('Enter the first fraction: '))
b = Fraction(input('Enter the second fraction: '))
if op.lower() == 'add':
    add = a+b
    print('Result of Addition of {0} and {1}: {2}'.format(a, b, add))
if op.lower() == 'subtract':
    subtract = a-b
    print('Result of Subtraction of {0} and {1}: {2}'.format(a, b, subtract))
if op.lower() == 'divide':
    divide = a/b
    print('Result of Division of {0} and {1}: {2}'.format(a, b, divide))
if op.lower() == 'multiply':
    multiply = a*b
    print('Result of Multiplication of {0} and {1}: {2}'.format(a, b, multiply))
    
'''
Method 2: more aligned with the text
'''
from fractions import Fraction

def add(a, b):
    print('Result of adding {0} and {1} is {2}'.format(a, b, a+b))
def subtract(a, b):
    print('Result of subtracting {0} and {1} is {2}'.format(a, b, a-b))
def divide(a, b):
    print('Result of dividing {0} by {1} is {2}'.format(a, b, a/b))
def multiply(a, b):
    print('Result of multiplying {0} and {1} is {2}'.format(a, b, a*b))

if __name__ == '__main__':
    try:
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))

        if op.lower() == 'add':
            add(a, b)
        if op.lower() == 'subtract':
            subtract(a, b)
        if op.lower() == 'divide':
            divide(a, b)   
        if op.lower() == 'multiply':
            multiply(a, b)
    except ValueError:
        print('Invalid fraction entered')
