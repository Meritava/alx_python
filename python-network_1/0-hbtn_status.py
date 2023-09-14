""" 
This modules uses the request moduleno to get
and fetch requests from alu-intranet
"""
import requests
# a variable that stores the url to be fetch
req = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(req.text))
print("\t- content:", req.text)