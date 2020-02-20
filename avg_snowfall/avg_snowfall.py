# Clayton Johnson
#  GEOL496 - Climate Change
#  
#  This program will import data from a local csv collected from NOAA.
#  The data is the global precipitation summary of the months from 1909 until 2018. 
#  
#  We are currently ignoring water years with incomplete data.
import csv

class WaterYear:
  def __init__(self, _year, _month, _precip, _snowfall):
    self.year = _year
    self.months = []
    self.months.append({_month:[_precip, _snowfall]})

  def getYear(self):
    return self.year

  def getMonths(self):
    return self.months

  def addMonth(self, _month, _precip, _snowfall):
    self.months.append({_month:[_precip, _snowfall]})

def get_water_years():
  first = True
  added = False
  year = 0
  month = 0
  
  water_years = []
  
  with open('../../data/crested_butte.csv') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    for line in reader:
      # line[0] => Site code (US...)
      # line[1] => Site name (CRESTED...)
      # line[2] => Date (Ex: Year-Month)
      # line[3] => Number days with snow depth > 1 inch
      # line[4] => Number days with snow depth > 1 inch (not sure why there's two)
      # line[5] => Extreme max snow depth
      # line[6] => Extreme max snow fall
      # line[7] => Extreme max precipitation
      # line[8] => Precipitation
      # line[9] => Snowfall
  
      if not first and len(line) >= 10:
        # Get year and month for the instance
        year = int(line[2].split('-')[0])
        month = int(line[2].split('-')[1])
        precip = line[8]
        snowfall = line[9]
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
        
water_years = get_water_years()
  
for water_year in water_years:
  print('Year: {}'.format(water_year.getYear()))
  print('\tTotal Months: {}'.format(len(water_year.getMonths())))
