#/bin/bash

echo "Downloading 0-1000"
curl -H "token:$(cat token)" "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/?limit=1000" >> stations0.json 
echo "Downloading 1000-2000"
curl -H "token:$(cat token)" "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/?limit=1000&offset=1000" >> stations1.json 
echo "Downloading 2000-3000"
curl -H "token:$(cat token)" "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/?limit=1000&offset=2000" >> stations2.json 
echo "Downloading 3000-4000"
curl -H "token:$(cat token)" "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/?limit=1000&offset=3000" >> stations3.json 
echo "Downloading 4000-5000"
curl -H "token:$(cat token)" "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/?limit=1000&offset=4000" >> stations4.json 
echo "Downloading 5000-6000"
curl -H "token:$(cat token)" "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/?limit=1000&offset=5000" >> stations5.json 
echo "Downloading 6000-7000"
curl -H "token:$(cat token)" "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/?limit=1000&offset=6000" >> stations6.json
#cat stations.json | python3 max_elevation_colorado.py # -m json.tool #>> stations.json
