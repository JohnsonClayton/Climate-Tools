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

  def __str__(self, verbose=False): # This line doesn't even make sense because you can't pass in verbose
    ret = str(self._year)
    if verbose:
      ret += '\n'
      for month in self._months:
        ret += '  ' + str(month) + '\n'
    else:
      ret += ','
      ret += str(self.sumRunOff()) + '\n'
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
    return len(self._months) == 12

  def sumRunOff(self):
    suma = 0
    for month in self._months:
      suma += month.getRunOff()

    return suma


def parse(filename=''):
  """
  parse

  takes in a given file and parses the file

  args: filename ( by default, filename='')

  returns: a list of WaterYear objects

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

  return [ year for year in water_years if year.isGood() ]

def graph(water_years=[]):
  """
  graph

    This function takes a single argument of a list of WaterYear objects and graphs them

  args: list of WaterYear objects (by default, water_years=[] )

  returns: void

  """

  for year in water_years:
    print(year)

def output_to_file(water_years=[]):
  """
  output_to_file
    
    This function takes the a list of water years and outputs them to a file

  args: list of WaterYear objects (by default, water_years=[] )

  returns: void
  """

  with open('runoff_output.csv', 'w') as outf:
    for year in water_years:
      outf.write(str(year))

def parse_and_graph(filename=''):
  """
  parse_and_graph

    This function calls the parsing function. From the values returned from the parsing function, the function will then call the graph function

  args: filename (by default, filename='')

  returns: void

  """
  #graph(parse(filename))
  output_to_file(parse(filename))

if __name__ == '__main__':
  parse_and_graph('runoffdata.csv')
