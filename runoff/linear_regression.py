#!/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
  reg = sns.regplot(x=df[x_axis_data], y=df[y_axis_data], ci=95)

  # Set the title of the graph
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)

  # Display the graph
  plt.show()

  # If user indicated saving, save the figure
  if save_fig:
    ( reg.get_figure() ).savefig('../media/{}_vs_{}.png'.format(xlabel, ylabel))


if __name__ == '__main__':
  graph(filename='runoff_precip_data.csv', 
          x_axis_data='Snowfall', 
          xlabel='Snowfall (inches)', 
          y_axis_data='Discharge', 
          ylabel='River Discharge (cubic feet per second)',
          title='Relationship Between Snowfall and River Discharge\nin the Crested Butte Basin',
          save_fig=True)

  graph(filename='runoff_precip_data.csv', 
          x_axis_data='Precip', 
          xlabel='Precipitation (inches)', 
          y_axis_data='Discharge', 
          ylabel='River Discharge (cubic feet per second)',
          title='Relationship Between Precipitation and River Discharge\nin the Crested Butte Basin',
          save_fig=True)
