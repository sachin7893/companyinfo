#!/usr/bin/python

import json
import requests
import sys
import ConfigParser


config = ConfigParser.ConfigParser()
config.read("config.txt")
API_KEY = config.get('client', 'api_key')
response = requests.get('https://api.macaddress.io/v1?apiKey='+API_KEY+'&output=json&search='+sys.argv[1])
data = response.json()
print data['vendorDetails']['companyName']