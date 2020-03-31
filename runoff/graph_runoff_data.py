#!/bin/python3

import csv
import matplotlib.pyplot as plt


# Class implementation for water years used in other (of my) code

class Month:
  def __init__(self, num, runoff):
    self._num = num
    self._runoff = runoff
  
  def __str__(self):
    return str(self._num) + ' ' + str(self._runoff)

  def getRunOff(self):
    return self._runoff

class WaterYear:
  def __init__(self, year, month, runoff):
    self._year = year
    self._months = []
    self._months.append(Month(month, runoff))
    self._bad_data = False

  def __str__(self):
    ret = str(self._year) + '\n'
    for month in self._months:
      ret += '  ' + str(month) + '\n'
    return ret

  def getYear(self):
    return self._year

  def getMonths(self):
    return self._months

  def addMonth(self, month, runoff):
    self._months.append(Month(month, runoff))

  def setBadData(self):
    self._bad_data = True

  def isGood(self):
    return not self._bad_data


def parse_and_print(filename=''):
  """
  parse_and_print

  takes in a given file, parses the file, and creates a graph using the input data

  args: filename ( by default, filename='')

  returns: void

  """
  if filename != '':
    # Parse input file
    first = True
    added = False
    year = 0
    month = 0
    
    water_years = []

    with open(filename, 'r') as csvFile:
      reader = csv.reader(csvFile, delimiter='\t')
      for line in reader:
        #print(line) 
  

        # agency_cd    agency code
        # site_no USGS site number
        # parameter_cd
        # ts_id
        # year_nu Calendar year for value
        # month_nu     Month for value
        # mean_va monthly-mean value.
        if not first and len(line) >= 6 and line[0] == 'USGS':
          # Get year and month for the instance
          year = int(line[4])
          month = int(line[5])
          try: 
            runoff = float(line[6])
          except Exception:
            runoff = 0

            #print('year: {}\nmonth: {}'.format(year, month))
        
          # Find what water year it is
          if month > 10:
            # It belongs to the water year for year + 1
            year += 1
          # Find if water year exists
          added = False
          for water_year in water_years:
            if year == water_year.getYear():
              water_year.addMonth(month, runoff)
              added = True
          if not added:
             water_years.append(WaterYear(year, month, runoff))
        else:
          first = False

  else:
    # Nothing to do
    print('Nothing to do...')

  for year in water_years:
    print(year)

if __name__ == '__main__':
  parse_and_print('runoffdata.csv')
