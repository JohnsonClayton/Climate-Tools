# Clayton Johnson
#  GEOL496 - Climate Change
#  
#  This program will import data from a local csv collected from NOAA.
#  The data is the global precipitation summary of the months from 1909 until 2018. 
#  
#  We are currently ignoring water years with incomplete data.

import csv
import numpy as np
import matplotlib.pyplot as plt

class Month:
  def __init__(self, _num, _precip, _snowfall):
    self.num = _num
    self.precip = _precip
    self.snowfall = _snowfall

  def getPrecip(self):
    return self.precip

  def getSnowfall(self):
    return self.snowfall

class WaterYear:
  def __init__(self, _year, _month, _precip, _snowfall):
    self.year = _year
    self.months = []
    self.months.append(Month(_month, _precip, _snowfall))
    self.bad_data = False

  def getYear(self):
    return self.year

  def getMonths(self):
    return self.months

  def addMonth(self, _month, _precip, _snowfall):
    self.months.append(Month(_month, _precip, _snowfall))

  def setBadData(self):
    self.bad_data = True

  def isGood(self):
    return not self.bad_data

  def sumPrecip(self):
    precip_sum = 0
    for month in self.months:
      precip_sum += month.getPrecip()
    return precip_sum

  def sumSnowfall(self):
    snowfall_sum = 0
    for month in self.months:
      snowfall_sum += month.getSnowfall()
    return snowfall_sum

def get_water_years():
  first = True
  added = False
  year = 0
  month = 0
  
  water_years = []
  
  with open('../../data/crested_butte.csv') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    for line in reader:
      """line[0] => Site code (US...)
      line[1] => Site name (CRESTED...)
      line[2] => Date (Ex: Year-Month)
      line[3] => Number days with snow depth > 1 inch
      line[4] => Number days with snow depth > 1 inch (not sure why there's two)
      line[5] => Extreme max snow depth
      line[6] => Extreme max snow fall
      line[7] => Extreme max precipitation
      line[8] => Precipitation
      line[9] => Snowfall"""
  
      if not first and len(line) >= 10:
        # Get year and month for the instance
        year = int(line[2].split('-')[0])
        month = int(line[2].split('-')[1])
        try: 
          precip = float(line[8])
        except Exception:
          precip = 0

        try: 
          snowfall = float(line[9])
        except Exception:
          snowfall = 0
        #print('year: {}\nmonth: {}'.format(year, month))
        
        # Find what water year it is
        if month > 10:
          # It belongs to the water year for year + 1
          year += 1
        # Find if water year exists
        added = False
        for water_year in water_years:
          if year == water_year.getYear():
            water_year.addMonth(month, precip, snowfall)
            added = True
        if not added:
           water_years.append(WaterYear(year, month, precip, snowfall))
      else:
        first = False
  return water_years

def clean_data(wyears):
  for wyear in wyears:
    if len(wyear.getMonths()) < 12:
      wyear.setBadData()
  return wyears

def graph_data(wyears):
  # Preparing data to be graphed
  precip_data = []
  snowfall_data = []
  years = []

  trend_precip_data = []
  trend_snowfall_data = []
  trend_years = []

  for wyear in wyears:
    years.append(wyear.getYear())
    if wyear.isGood():
      precip_data.append(wyear.sumPrecip())
      snowfall_data.append(wyear.sumSnowfall())

      trend_precip_data.append(wyear.sumPrecip())
      trend_snowfall_data.append(wyear.sumSnowfall())
      trend_years.append(wyear.getYear())
    else:
      precip_data.append(np.nan)
      snowfall_data.append(np.nan)

  # Graphing Snowfall
  fig, ax1 = plt.subplots()
  
  color = 'tab:blue'
  ax1.set_xlabel('Water Years')
  ax1.set_ylabel('Snowfall (mm)', color=color)
  ax1.plot(years, snowfall_data, color=color)
  ax1.tick_params(axis='y', labelcolor=color)

  # Graphing Snowfall trendline
  z = np.polyfit(trend_years, trend_snowfall_data, 1)
  p = np.poly1d(z)
  trend_data_points = []
  for tyear in trend_years:
    trend_data_points.append(p(tyear))
  print('snowfall trend is {}'.format(p))
  plt.plot(trend_years, trend_data_points, 'b--')

  # Graphing Precipitation
  ax2 = ax1.twinx() # Creates the second axis that shares the domain

  color = 'tab:green'
  ax2.set_ylabel('Precipitation (mm)', color=color)
  ax2.plot(years, precip_data, color=color)
  ax2.tick_params(axis='y', labelcolor=color)

  # Graphing Precipitation trendline
  z = np.polyfit(trend_years, trend_precip_data, 1)
  p = np.poly1d(z)
  print('precip trend is {}'.format(p))
  trend_data_points = []
  for tyear in trend_years:
    trend_data_points.append(p(tyear))
  plt.plot(trend_years, trend_data_points, 'g--')

  plt.title('Snowfall and Precipitation in Crested Butte from 1909 to 2018', fontsize=17)
  fig.tight_layout()
  plt.show()

def print_summary(wyears):
  for water_year in water_years:
    print('Year: {}'.format(water_year.getYear()))
    if water_year.isGood():
      print('\tTotal Precipitation: {}'.format(water_year.sumPrecip()))
      print('\tTotal Snowfall: {}'.format(water_year.sumSnowfall()))
    else:
      print('\tBad Data')
  
          
water_years = clean_data(get_water_years())
graph_data(water_years)

