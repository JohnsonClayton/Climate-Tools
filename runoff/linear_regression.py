#!/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graph(filename='', x_axis_title='', y_axis_title=''):
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
  sns.scatterplot(x=df[x_axis_title], y=df[y_axis_title])
  plt.show()


if __name__ == '__main__':
  graph('runoff_precip_data.csv', 'Snowfall', 'Discharge')
  graph('runoff_precip_data.csv', 'Precip', 'Discharge')
