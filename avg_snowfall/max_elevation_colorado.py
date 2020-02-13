# Python script made to take input from pipe and find the site with the highest elevation in CO, USA

import json
import sys

data = ""

for line in sys.stdin:
  data += line

jdata = json.loads(data)

for attr in jdata:
  print(attr)

co_sites = []
count = 0
for i in range(0, len(jdata['results'])):
  try:
    #print(jdata['results'][i]['elevation'])
    if jdata['results'][i]['name'][-5:] == "CO US":
      # Checks to see if the elevation attribute exists (other techniques weren't working...
      jdata['results'][i]['elevation'] = jdata['results'][i]['elevation']
      jdata['results'][i]['mindate'] = jdata['results'][i]['mindate']
      jdata['results'][i]['maxdate'] = jdata['results'][i]['maxdate']
      co_sites.append(jdata['results'][i])
  except KeyError:
    count += 1

print("Malcontents: {}".format(count))

co_sites.sort(key=lambda x: x['mindate'])
co_sites.sort(key=lambda x: x['elevation'], reverse=True)

for site in co_sites:
  print("Site: {}\n\tElevation: {}\n\tMin Date: {}\n\tMax Date: {}".format(site['name'], site['elevation'], site['mindate'], site['maxdate']))
