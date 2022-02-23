import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    path = 'epa-sea-level.csv'
    df = pd.read_csv(path)
    df = df.fillna(0)

    # Create scatter plot
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    # Create first line of best fit
    new_index = [i for i in range(133, 170, 1)]
    new_years = [i for i in range(2014, 2051, 1)]
    new_df = pd.DataFrame(data = new_years, index = new_index, columns = ['Year'])
    x = pd.concat([df, new_df], ignore_index = True, axis = 0)
    x = x.fillna(0)

    m, b, r, p, se = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])

    plt.plot(x['Year'], m*x['Year'] + b, 'b')

    # Create second line of best fit
    m1, b1, r2, p2, se2 = linregress(x = df['Year'][120:], y = df['CSIRO Adjusted Sea Level'][120:])

    plt.plot(x['Year'][120:], m1*x['Year'][120:] + b1, 'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend(['level rise if the rate of rise continues as it has since the year 1880', 
        'level rise if the rate of rise continues as it has since the year 2000'])
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()