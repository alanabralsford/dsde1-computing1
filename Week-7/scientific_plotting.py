'''
scientific_plotting.py

Using numpy and matplotlib to create plots and 
graphs useful for scientific reports.
'''

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


def create_line_data(num_values):
    '''Generates points for a line plot.'''
    # generate linear data
    data = np.linspace(0, 100, num_values)
    # add a little noise to make more interesting
    data += random.random(num_values)
    return data

def line_graph():
    x = create_line_data(50)
    plt.plot(x, x)
    plt.xlabel('Amount of Doggos')
    plt.ylabel('Pure Joy')
    plt.title("Secret to Happiness")
    plt.show()
#line_graph()

def create_scatter_data(num_values):
    '''Returns a dictionary with two arrays all length num_values:
           x - series of x-axis values
           y - series of datapoints of random values 
           '''
    data = {'x': np.arange(num_values),
            'a': np.random.randint(0, 50, num_values)}
    data['a'] += data['x']
    return data
def scatter_graph():
    data = create_scatter_data(50)
    plt.scatter(data['x'], data['a'])
    plt.xlabel('Amount of Doggos')
    plt.ylabel('Pure Joy')
    plt.title("Secret to Happiness")
    plt.show()
#scatter_graph()

def histogram():
    data = create_scatter_data(100)
    plt.hist(data['a'], bins = 10)
    plt.xlabel('Amount of Doggos')
    plt.ylabel('Pure Joy')
    plt.title("Secret to Happiness")
    plt.show()
histogram()
def main():
    '''The function that will be called first.'''

    # number of data points
    #num_values = 100
    #y_data = create_line_data(num_values)
    #scatter_data = create_scatter_data(num_values)



if __name__ == '__main__':
    main()