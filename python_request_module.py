

import requests
response_bbc = requests.get("https://www.bbc.co.uk/")

def check_response_code():
    if response_bbc.status_code == 200:
        print("Success your in!")
    elif response_bbc.status_code == 400:
        print("Page not found")
    elif response_bbc.status_code == 404:
        print("oops sorry something went wrong")
    else:
        print("Could not identify the status code, Please try another website")