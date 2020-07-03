# What is an API
# Application programming interface
# Why - used to connect to other programs
# In Python we have a module called requests to interact with web APIs

# How can we install a python package in pycharm

# Write "pip install requests" in the pycharm terminal

# import requests

# Check HTTP/HTTPS 200 = Success - 400 - 404 page not found.
response_bbc = requests.get("https://www.bbc.co.uk/") # Here we have created a variable.

print(response_bbc.status_code) # status.code presents the data in more of a readable format

print(response_bbc.headers) # headers displays information that is in the header

print(type(response_bbc.headers)) # Using the type method

print(response_bbc.keys) # To find the keys within the dictionary

print(response_bbc.content) # .content will display the content

# Iteration 1
# Receive a response code and check if 200 - print success
# elif code 400 - page not found
# else code 404 Ops sorry something went wrong.

# Iteration 2
# Create a function called check_response_code including all of the above
# Returns the message with status code

# Iteration 3
# OOP with 4 pillars

# Control flow of checking the status_code of a website (www.bbc.co.uk)
# Iteration 1
if response_bbc.status_code == 200:
    print("Success your in!")
elif response_bbc.status_code == 400:
    print("Page not found")
elif response_bbc.status_code == 404:
    print("oops sorry something went wrong")
else:
    print("Could not identify the status code, Please try another website")

# Creating a function called check_response_code to check the status_code
# Iteration 2
def check_response_code():
    if response_bbc.status_code == 200:
        print("Success your in!")
    elif response_bbc.status_code == 400:
        print("Page not found")
    elif response_bbc.status_code == 404:
        print("oops sorry something went wrong")
    else:
        print("Could not identify the status code, Please try another website")

# Iteration 3
from python_request_module import check_response_code
print(check_response_code())