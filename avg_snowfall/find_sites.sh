#!/bin/bash

curl -H "token:$(cat token)" "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/"
