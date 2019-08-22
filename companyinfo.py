#!/usr/bin/python

import json
import requests
import sys
import configparser

macaddr=str(input("Please enter MAC Address: "))
config = configparser.ConfigParser()
config.read("config.txt")
API_KEY = config.get('client', 'api_key')
response = requests.get('https://api.macaddress.io/v1?apiKey='+API_KEY+'&output=json&search='+macaddr)
data = response.json()
print (data['vendorDetails']['companyName'])
