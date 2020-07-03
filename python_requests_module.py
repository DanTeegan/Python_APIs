# What is an API
# Application programming interface
# Why - used to connect to other programs
# In Python we have a module called requests to interact with web APIs

# How can we install a python package in pycharm

# Write "pip install requests" in the pycharm terminal

import requests

# Check HTTP/HTTPS 200 = Success - 400 - 404 page not found.
response_bbc = requests.get("https://www.bbc.co.uk/") # Here we have created a variable.

print(response_bbc)