# Doing Math With Python Text


# Chapter 2: pg 27-54

# Working with Lists and Tuples

simplelist = [1, 2, 3]
simplelist[0]
simplelist[1]
simplelist[2]
simplelist[-1]

stringlist = ['a string', 'b string', 'c string']
stringlist[0]
stringlist[1]
stringlist[-1]

emptylist = []
emptylist.append(1)
emptylist.append(2)
emptylist

simpletuple = (1, 2, 3)
simpletuple[0]
simpletuple[1]
simpletuple[2]
simpletuple[-1]
simpletuple[-1] == simpletuple[2]


# Iterating over a List or Tuple
l = [1, 2, 3]
for item in l:
    print(item)
t = (1, 2, 3)
for item in t:
    print(item)

'enumerate index'
l = [1, 2, 3]
for (index, item) in enumerate(l):
    print(index, item)
t = (1, 2, 3)
for (index, item) in enumerate(t):
    print(index, item)


# Creating Graphs with Matplotlib

import matplotlib.pyplot as plt
from pylab import plot, show
x_numbers = [1,2,3]
y_numbers = [2,4,6]
plot(x_numbers, y_numbers)
plot(x_numbers, y_numbers, marker = 'o')
plot(x_numbers, y_numbers, '*')           # only coordinates without line

# Graphing the Average Annual Temperature in NYC
'Method 1 from the text'
nyc_temp = [53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
years = range(2000, 2013)
plot(years, nyc_temp, marker = 'x')
'Method 2'
import matplotlib.pyplot as plt
nyc_temp = [53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
years = range(2000, 2013)
plt.plot(years, nyc_temp marker = 'o')


# Comparing the Monthly Temperature Trends of NYC

'Method 1 from the text'
nyc_temp_2000 = [31.3,37.3,47.2,51.0,63.5,71.3,72.3,72.7,66.0,57.0,45.3,31.1]
nyc_temp_2006 = [40.9,35.7,43.1,55.7,63.1,71.0,77.9,75.8,66.6,56.2,51.9,43.6]
nyc_temp_2012 = [37.3,40.9,50.9,54.8,65.1,71.0,78.8,76.7,68.8,58.0,43.9,41.5]
months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
'Method 2'
nyc_temp_2000 = [31.3,37.3,47.2,51.0,63.5,71.3,72.3,72.7,66.0,57.0,45.3,31.1]
nyc_temp_2006 = [40.9,35.7,43.1,55.7,63.1,71.0,77.9,75.8,66.6,56.2,51.9,43.6]
nyc_temp_2012 = [37.3,40.9,50.9,54.8,65.1,71.0,78.8,76.7,68.8,58.0,43.9,41.5]
months = range(1, 13)
plt.plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)

'Lets add Legend'
'Method 1 from the text'
from pylab import legend
nyc_temp_2000 = [31.3,37.3,47.2,51.0,63.5,71.3,72.3,72.7,66.0,57.0,45.3,31.1]
nyc_temp_2006 = [40.9,35.7,43.1,55.7,63.1,71.0,77.9,75.8,66.6,56.2,51.9,43.6]
nyc_temp_2012 = [37.3,40.9,50.9,54.8,65.1,71.0,78.8,76.7,68.8,58.0,43.9,41.5]
months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
legend([2000, 2006, 2012])
'Method 2'
nyc_temp_2000 = [31.3,37.3,47.2,51.0,63.5,71.3,72.3,72.7,66.0,57.0,45.3,31.1]
nyc_temp_2006 = [40.9,35.7,43.1,55.7,63.1,71.0,77.9,75.8,66.6,56.2,51.9,43.6]
nyc_temp_2012 = [37.3,40.9,50.9,54.8,65.1,71.0,78.8,76.7,68.8,58.0,43.9,41.5]
months = range(1, 13)
plt.plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
plt.legend([2000, 2006, 2012])

# Customizing Graphs

'Lets add Title and Lables'
'Method 1 from the text'
from pylab import plot, show, title, xlabel , ylabel, legend
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
title('Average monthly temperature in NYC')
xlabel('Month')
ylabel('Temperature')
legend([2000, 2006, 2012])
'Method 2'
import matplotlib.pyplot as plt
plt.plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
plt.title('Average monthly temperature in NYC')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.legend([2000, 2006, 2012])
plt.axes()

'Customizing the Axes'
'Method 1 from the text'
from pylab import axis
nyc_temp = [53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
plot(nyc_temp, marker = 'o')
axis()
axis(ymin = 0, xmin = 0, ymax = 60)
'Method 2'
import matplotlib.pyplot as plt
nyc_temp = [53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
plt.plot(nyc_temp, marker = 'o')
plt.axis()
plt.axis(ymin = 0, xmin = 0, ymax = 60)

'Plotting Using pyplot (which has been Method 2)'
'''
Simple plot using pyplot
'''
import matplotlib.pyplot as plt
def create_graph():
    x_numbers = [1,2,3]
    y_numbers = [2,4,6]
    plt.plot(x_numbers, y_numbers)
    plt.show()
if __name__ == '__main__':
    create_graph()
    
# Saving the Plots
from pylab import savefig
x = [1,2,3]
y = [2,4,6]
pylab.plot(x, y)
pylab.savefig('mygraph1.pdf')    # to save the figure


# Plotting with Formulas
# Newton's Law of Universal G
'''
The relationship between gravitational force and distance betwee two bodies
'''
import matplotlib
import matplotlib.pyplot as plt
    # Draw the graph
def draw_graph(x, y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel('Distance in Meters')
    plt.ylabel('Gravitational Force in Newtons')
    plt.title('Gravitational Force and Distance')
    plt.show()
def generate_F_r():
    # Values of r (100, 150, 200, 300.... up to 1000)
    r = range(100, 1001, 50)
    F = []
    G = 6.74*(10**-11)
    m1 = 0.5
    m2 = 1.5
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)
    draw_graph(r, F)
if __name__ == '__main__':
    generate_F_r()

# Projectile Motion
'''
Generate equally spaced floating points so we an have range of decimal numbers.
'''
start = 0.5
final = 1.0
increment = 0.1
def fragne(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
    return(numbers)
print(fragne(start, final, increment))

'''
Draw the trajectory of a body in projectile motion
'''
from matplotlib.pyplot import savefig
import matplotlib.pyplot as plt
import math
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')
def fragne(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
    return(numbers)  
def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    # time of flight
    t_flight = 2*u*math.sin(theta)/g
    # find time intervals
    intervals = fragne(0, t_flight, 0.001)
    # list of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_graph(x, y)
if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You entered an invalid input')
    else:
        draw_trajectory(u, theta)
        plt.show()
        #plt.savefig('projectile_motion1.svg')
        
# Comparing the Trajectory of Different Initial Velocities
        
if __name__ == '__main__':
    #List of three different initial velocities
    u_list = [20,40,60]
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)
    plt.legend(['20', '40', '60'])
    plt.show()
    #plt.savefig('different_initial_velocities.png')



# Chapter 2 Programming Challenges pages 55-60

# 1) How Does the Temperature Vary During the Day?

'''Method 1 from the text'''    
import matplotlib.pyplot as plt
def New_Delhi_weather():
    time = ['3am', '6am', '9am', '12pm', '3pm', '6pm', '9pm', '12am']
    temp = [80, 78, 77, 89, 92, 92, 88, 84]
    interval = range(1, len(time) + 1)
    plt.plot(interval, temp, '-x')
    plt.title('New Delhi Weather')
    plt.xticks(interval, time)
    plt.xlabel('Time of Day')
    plt.ylabel('Temperature')
    plt.show()
if __name__ == '__main__':
    New_Delhi_weather()

def Toledo_weather():
    time = ['3am', '6am', '9am', '12pm', '3pm', '6pm', '9pm', '12am']
    temp = [27, 24, 25, 29, 34, 38, 36, 30]
    interval = range(1, len(time) + 1)
    plt.plot(interval, temp, '-x')
    plt.title('Toledo Weather')
    plt.xticks(interval, time)
    plt.xlabel('Time of Day')
    plt.ylabel('Temperature')
    plt.show()
if __name__ == '__main__':
    Toledo_weather()
   
'''Method 2'''
import matplotlib.pyplot as plt
time = ['3am', '6am', '9am', '12pm', '3pm', '6pm', '9pm', '12am']
temp = [80, 78, 77, 89, 92, 92, 88, 84]
interval = range(1, len(time) + 1)
plt.plot(interval, temp, '-x')
plt.xticks(interval, time)
plt.title('New Delhi Weather')
plt.xlabel('Time of Day')
plt.ylabel('Temperature')
plt.show()

    # Comparing the weather of New Delhi and Toledo
import matplotlib.pyplot as plt
time = ['3am', '6am', '9am', '12pm', '3pm', '6pm', '9pm', '12am']
temp_New_Delhi = [80, 78, 77, 89, 92, 92, 88, 84]
temp_Toledo = [27, 24, 25, 29, 34, 38, 36, 30]
interval = range(1, len(time) + 1)
plt.plot(interval, temp_New_Delhi, '-x', temp_Toledo, '-x')
plt.xticks(interval, time)
plt.title('New Delhi vs Toledo Weather')
plt.xlabel('Time of Day')
plt.ylabel('Temperature')
plt.show()


# 2) Exploring a Quadrati Function Visually
'''
Quadratic function calculator
'''
#x_values = [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
x_values = range(-100, 101)
for x in x_values:
    y_values = []
    y = x**2 + 2*x + 1
    y_values.append(y)
    print('x = {0}, y = {1}'.format(x, y))
    plt.scatter(x, y, color = 'black')
    plt.title('X and Y plot for Quadratic Eq.')
    
    
# 3) Enhanced Projectile Trajectory Comparison Program

import matplotlib.pyplot as plt
import math
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')
def fragne(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
    return(numbers)  
def draw_trajectory(u, theta, t_flight):
    theta = math.radians(theta)
    g = 9.8
    # time of flight
    t_flight = 2*u*math.sin(theta)/g
    # find time intervals
    intervals = fragne(0, t_flight, 0.001)
    # list of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_graph(x, y)
if __name__ == '__main__':
    num_trajectories = int(input('How many trajectories? '))
    velocities = []
    angles = []
    g = 9.8
    for i in range(1, num_trajectories + 1):
        v = input('Enter the initial velocity for trajectory {0} (m/s): '.format(i))
        theta = input('Enter the angle of projection for trajectory {0} (degrees): '.format(i))
        velocities.append(float(v))
        angles.append(math.radians(float(theta)))
    for i in range(num_trajectories):
        t_flight = 2*velocities[i]*math.sin(angles[i])/g
        S_x = velocities[i]*math.cos(angles[i])*t_flight
        S_y = velocities[i]*math.sin(angles[i])*(t_flight/2) - (1/2)*g*(t_flight/2)**2
        print('Initial velocity: {0} Angle of Projection: {1}'
              .format(velocities[i], math.degrees(angles[i])))
        print('T: {0} S_x: {1} S_y: {2}'.format(t_flight, S_x, S_y))
        print()
        draw_trajectory(velocities[i], angles[i], t_flight)
        legends = []
    for i in range(0, num_trajectories):
        legends.append('{0} - {1}'.format(velocities[i], math.degrees(angles[i])))
    plt.legend(legends)
    plt.show()  


# 4) Visualizing Your Expenses

'''Examples of drawing a horizontal bar chart'''

import matplotlib.pyplot as plt
y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
plt.bar(x, y, color="blue")

import matplotlib.pyplot as plt
def create_bar_chart(data, labels):
    # Number of bars
    num_bars = len(data)
    # This list is the point on the y-axis where each
    # Bar is centered. Here it will be [1,2,3,...]
    positions = range(1, num_bars + 1)
    plt.barh(positions, data, align = 'center')
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of steps walked')
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()
if __name__ == '__main__':
    # Number of steps walked during the past week
    steps = [6534, 7000, 8900, 10789, 3467, 11045, 5090]
    # Corresponding days
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_bar_chart(steps, labels)
    
'''
Now to the problem 4
'''
import matplotlib.pyplot as plt
def create_bar_chart(data, labels):
    num_bars = len(data)
    positions = range(1, num_bars + 1)
    plt.barh(positions, data, align = 'center')
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Categories')
    plt.title('Weekly expenditures')
    plt.grid()
    plt.show()
if __name__ == '__main__':
    num_categories = int(input('Enter the number of Categories: '))
    expenditures = []
    labels = []
    for i in range(num_categories):
        category = input('Enter Category: ')
        expenditure = float(input('Enter Expenditure: '))
        labels.append(category)
        expenditures.append(expenditure)
    create_bar_chart(expenditures, labels)
    

# 5) Exploring the Relationship Between the Fibonacci Sequence and the Golden Ratio
    
import matplotlib.pyplot as plt

def fibonacci(n):
    if n == 1:
        return[1]
    if n == 2:
        return[1,1]
    # for n > 2
    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a+b
        series.append(c)
        a = b
        b = c
    return(series)

def plot_ratios(series):
    ratios = []
    for i in range(len(series)-1):
        ratios.append(series[i+1]/series[i])
    plt.plot(ratios)
    plt.title('Ratio between Fibonacci Numbers & Golden Ratio')
    plt.ylabel('Ratio')
    plt.xlabel('Numbers')
    plt.show()
if __name__ == '__main__':
    num = 50
    series = fibonacci(num)
    plot_ratios(series)
