#!/usr/bin/env python

import requests
import sys
import json

with open(sys.argv[1], 'r') as file:
	data = json.load(file)

i = 0
while i < len(data) - 1:
	# skip admin messages
	if not 'http' in data[i]:
		i += 2
		continue

	url = None

	# older tweets do not have 'outlinks'
	if data[i+1] == '':
		url = data[i][data[i].find('http'):]
	else:
		url = data[i+1]

	r = requests.head(url)
	try:
		data[i+1] = r.headers['Location']
	# some bit.ly URLs are broken: http://bit.ly/rrIzwO
	except:
		data[i+1] = None

	print(url, data[i+1])
	i += 2

with open(sys.argv[1] + '-expanded.json', 'w') as file:
	json.dump(data, file, ensure_ascii = False, indent = '\t')