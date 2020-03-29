
# import packages

import json
import urllib
import requests

# website container json scructure data to scrape download links

website = 'https://api.fda.gov/download.json'

# dump the json data

with urllib.request.urlopen(website) as url:
    data = json.loads(url.read().decode())

# get the animal and veterinary data

list_of_records = data['results']['animalandveterinary']['event']['partitions']

# create empty list to store the downlaod links

list_of_files = []

# add links to file

for x in range(len(list_of_records)):
    list_of_files.append(list_of_records[x]['file'])

# write list of links to text file for bash script to download

with open('open_fda_file_list.txt', 'w') as filehandle:
    for listitem in list_of_files:
        filehandle.write('%s\n' % listitem)

