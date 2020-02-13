#!/bin/bash

for year in {1977..2017}
do
  echo $year
  wget "https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USC00053489&startDate=$year-01-11&endDate=$year-01-11&dataTypes=TMAX,TMIN" -w 1 
done

# This is an example of a technique to filter out all of the data from February 3rd collected at the GRAND JUNCTION WALKER FIELD site
cat *.csv | grep "02-03\"" | grep "GRAND JUNCTION WALKER FIELD" >> feb_3.csv
