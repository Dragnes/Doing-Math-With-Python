# Doing Math With Python Text


# Chapter 3: pg 61-91

# Finding the Mean

shortlist = [1,2,3]
sum(shortlist)

len(shortlist)

'''
Calculating the mean
'''
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    return(s/N)
if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean = calculate_mean(donations)
    N = len(donations)
    print('Mean donation over the last {0} days is {1}'.format(N, mean))

samplelist = [4,1,3,2]
samplelist.sort()
samplelist

# Finding the Median

'''
Calculating the median
'''
def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()
    # find the median
    if N % 2 == 0:
        m1 = N/2
        m2 = (N/2) + 1
        # convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    return(median)
if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = calculate_median(donations)
    N = len(donations)
    print('Median donation over the last {0} day is {1}'.format(N, median))

    
# Finding the Mode and Creating a Frequency Table
    
# Finding the Most Common Elements

simplelist = [4, 2, 1, 3, 4]
from collections import Counter
c = Counter(simplelist)
c.most_common()
c.most_common(1)
c.most_common(2)

mode = c.most_common(1)
mode
mode[0]
mode[0][0]

# Finding the Mode

'''
Calculating the Mode
'''
from collections import Counter
def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return(mode[0][0])
if __name__ == '__main__':
    scores = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]
    mode = calculate_mode(scores)
    print('The mode of the list of numbers is: {0}'.format(mode))

'''
Calculating the mode when the list of numbers may have multiple modes
'''
from collections import Counter
def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return(modes)
if __name__ == '__main__':
    scores = [5,5,5,4,4,4,9,1,3]
    modes = calculate_mode(scores)
    print('The mode(s) of the list of numbers are: ')
    for mode in modes:
        print(mode)

# Creating a Frequency Table

'''
Frequency table for a list of numbers
'''
from collections import Counter
def frequency_table(numbers):
    table = Counter(numbers)
    print('Number\tFrequency')
    for number in table.most_common():
        print('{0}\t{1}'.format(number[0], number [1]))
if __name__ == '__main__':
    scores = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]
    frequency_table(scores)

'''
Frequency table for a list of numbers
Enhanced to display the table sorted by the numbers
'''
from collections import Counter
def frequency_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()
    print('Number\tFrequency')
    for number in numbers_freq:
        print('{0}\t{1}'.format(number[0], number[1]))
if __name__ == '__main__':
    scores = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]
    frequency_table(scores)


# Measuring the Dispersion

# Finding the range of a set of Numbers

'''
Finding the range
'''
def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    # Find the range
    r = highest - lowest
    return(lowest, highest, r)
if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))
    
# Finding the Variance and Standard Diviation

'''
Find the variance and standard deviation of a list of numbers
'''
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return(mean)
def find_differences(numbers):
    # Find the meanj
    mean = calculate_mean(numbers)
    # Find the differences from the sum
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return(diff)
def calculate_variance(numbers):
    # Find the list of differences
    diff = find_differences(numbers)
    # Find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # Find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return(variance)
if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))
    std = variance**0.5
    print('The standard deviation of the list of numbers is {0}'.format(std))

 
# Calculating the Correlation Between Two Data Sets

# Calculating the Correlation Coefficient

simple_list1 = [1,2,3]
simple_list2 = [4,5,6]
for x, y in zip(simple_list1, simple_list2):
    print(x, y)

'''
Calculat the correlation coefficient
'''
def find_corr_x_y(x, y):
    n = len(x)
    # Find the sum of the products
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi*yi)
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    x_square = []
    for xi in x:
        x_square.append(xi**2)
    # Find the sum
    x_square_sum = sum(x_square)
    y_square = []
    for yi in y:
        y_square.append(yi**2)
    # Find the sum
    y_square_sum = sum(y_square)
    # use formula from text to calculate correlation
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator
    return(correlation)

# High School Grades and Performance on College Adimission Tests (examples)

def find_corr_x_y(x, y):
    n = len(x)
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi*yi)
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    x_square = []
    for xi in x:
        x_square.append(xi**2)
    x_square_sum = sum(x_square)
    y_square = []
    for yi in y:
        y_square.append(yi**2)
    y_square_sum = sum(y_square)
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator
    return(correlation)

import matplotlib.pyplot as plt
if __name__ == '__main__':
    x = [90,92,95,96,87,87,90,95,98,96]
    y = [85,87,86,97,96,88,89,98,98,87]
    correlation = find_corr_x_y(x,y)
    print('The Correlation Coefficient of High School Grades and Performance on College Adimission Tests is {0}'.format(correlation))
    plt.scatter(x, y, marker = 'x')
    plt.ylabel('College admission Test Scores')
    plt.xlabel('High School Grades')

if __name__ == '__main__':
    x = [83,85,84,96,94,86,87,97,97,85]
    y = [85,87,86,97,96,88,89,98,98,87]
    correlation = find_corr_x_y(x,y)
    print('The Correlation Coefficient of High School Grades and Performance on College Adimission Tests is {0}'.format(correlation))
    plt.scatter(x, y, marker = 'x')
    plt.ylabel('College admission Test Scores')
    plt.xlabel('High School Grades')

# Reading Data from Files

# Reading Data from a Text File

# Find the sum of the numbers stored in a file (same as in the text)
def sum_data(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s += float(line)
    print('Sum of the numbers: {0}'.format(s))
if __name__ == '__main__':
    sum_data('Ch3_mydata.txt')   # Created my own text file and saved it where the program is located
# Below I try to stay consistent with flow of text
def sum_data(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s += float(line)
    return (s)
if __name__ == '__main__':
    data = sum_data('Ch3_mydata.txt')
    print('Sum of the numbers: {0}'.format(data))

'''
Calculating the mean of numbers stored in a file
'''
def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return(numbers)
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return(mean)
if __name__ == '__main__':
    data = read_data('Ch3_mydata.txt')
    mean = calculate_mean(data)
    print('Mean: {0}'.format(mean))

# Reading Data from a CSV (comma-separated values) file

import csv
import matplotlib.pyplot as plt

def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.show()
def read_csv(filename):
    numbers = []
    squared = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            numbers.append(int(row[0]))
            squared.append(int(row[1]))
        return(numbers, squared)
if __name__ == '__main__':
    numbers, squared = read_csv('Ch3_numbers_csv.csv')
    scatter_plot(numbers, squared)

# Download csv data from to determine correlation between 'summer' and 'swimming lessons' search on google.
def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        
        summer = []
        highest_correlated = []
        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))
    return(summer, highest_correlated)

if __name__ == '__main__':
    summer, highest_correlated = read_csv('correlate-summer.csv')
    corr = find_corr_x_y(summer, highest_correlated)
    print('Highest Correlation: {0}'.format(corr))
    scatter_plot(summer, highest_correlated)
