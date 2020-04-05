#!/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

def graph(filename='', x_axis_data='', y_axis_data='', title='', xlabel='', ylabel='', save_fig=False):
  """
  graph - Graphs the data from the given file

  args: filename (by default, filename='')
        x_axis_title (by default, x_axis_title='')
        y_axis_title (by default, y_axis_title='')

  returns: void

  """

  df = pd.read_csv(filename, index_col=0)
  #print(df.head())

  plt.figure()

  # Create a linear regression plot with the given x and y data. Add bands indicating 95% confidence interval (ci)
  reg = sns.regplot(x=df[x_axis_data], y=df[y_axis_data]/12.0, ci=95)

  # Set the title of the graph
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)

  # Display the graph
  plt.show()

  # If user indicated saving, save the figure
  if save_fig:
    ( reg.get_figure() ).savefig('../media/{}_vs_{}.png'.format(xlabel, ylabel))

def calc_rsquared(filename='', xlabel='', ylabel=''):
  data = pd.read_csv(filename, index_col=0)
  slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(data[xlabel], data[ylabel])
  return r_value**2


if __name__ == '__main__':
  print('R_squared for Snowfall and Discharge: {}'.format(calc_rsquared(filename='runoff_precip_data1.csv',xlabel='Snowfall', ylabel='Discharge')))
  graph(filename='runoff_precip_data1.csv', 
          x_axis_data='Snowfall', 
          xlabel='Snowfall (inches)', 
          y_axis_data='Discharge', 
          ylabel='River Discharge (cubic feet)',
          title='Relationship Between Snowfall and River Discharge\nin the Crested Butte Basin',
          save_fig=True)

  print('R_squared for Precipitation and Discharge: {}'.format(calc_rsquared(filename='runoff_precip_data1.csv',xlabel='Precip', ylabel='Discharge')))
  graph(filename='runoff_precip_data1.csv', 
          x_axis_data='Precip', 
          xlabel='Precipitation (inches)', 
          y_axis_data='Discharge', 
          ylabel='River Discharge (cubic feet)',
          title='Relationship Between Precipitation and River Discharge\nin the Crested Butte Basin',
          save_fig=True)
  print('R_squared for Precipitation + Snowfall and Discharge: {}'.format(calc_rsquared(filename='runoff_precip_data1.csv',xlabel='Precip/Snowfall', ylabel='Discharge')))
  graph(filename='runoff_precip_data1.csv', 
          x_axis_data='Precip/Snowfall', 
          xlabel='Precipitation and Snowfall (inches)', 
          y_axis_data='Discharge', 
          ylabel='River Discharge (cubic feet)',
          title='Relationship Between Precipitation and River Discharge\nin the Crested Butte Basin',
          save_fig=True)
