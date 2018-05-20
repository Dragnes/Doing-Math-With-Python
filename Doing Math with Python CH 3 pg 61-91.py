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
