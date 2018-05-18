# Doing Math With Python Text


# Chapter 3: pg 61-91

# Finding the Mean

shortlist = [1,2,3]
sum(shortlist)

len(shortlist)

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
