#!/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

def graph(filename='', x_axis_data='', y_axis_data='', title='', xlabel='', ylabel='', normalized=False, save_fig=False):
  """
  graph - Graphs the data from the given file

  args: filename (by default, filename='')
        x_axis_title (by default, x_axis_title='')
        y_axis_title (by default, y_axis_title='')

  returns: void

  """

  df = pd.read_csv(filename, index_col=0)

  # Normalizes the data if requested (this shouldn't change the correlation statistics)
  if normalized:
    df = (df - df.mean()) / (df.max() - df.min())

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

  # Calculates r_squared of the values
  print('R_squared for {} and {}: {}'.format(x_axis_data, y_axis_data, calc_rsquared(filename=filename,xlabel=x_axis_data, ylabel=y_axis_data)))

def calc_rsquared(filename='', xlabel='', ylabel=''):
  data = pd.read_csv(filename, index_col=0)
  slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(data[xlabel], data[ylabel])
  return r_value**2


if __name__ == '__main__':
  graph(filename='rsp1911-1957.csv',
          x_axis_data='Precip', 
          xlabel='Precipitation (inches)', 
          y_axis_data='Discharge', 
          ylabel='River Discharge (cubic feet)',
          title='Relationship Between Precip and River Discharge\nin the Crested Butte Basin from 1911 until 1946',
          normalized=True,
          save_fig=True)

  graph(filename='rsp1958-1988.csv',
          x_axis_data='Precip', 
          xlabel='Precipitation (inches)', 
          y_axis_data='Discharge', 
          ylabel='River Discharge (cubic feet)',
          title='Relationship Between Precip and River Discharge\nin the Crested Butte Basin from 1947 until 1982',
          normalized=True,
          save_fig=True)
  graph(filename='rsp1989-2018.csv',
          x_axis_data='Precip', 
          xlabel='Preciptation (inches)', 
          y_axis_data='Discharge', 
          ylabel='River Discharge (cubic feet)',
          title='Relationship Between Precip and River Discharge\nin the Crested Butte Basin from 1983 until 2018',
          normalized=True,
          save_fig=True)
