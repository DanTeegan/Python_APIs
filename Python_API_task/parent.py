# Here we import the requests
import requests
# Here we are getting the requests from the website BBC
response_bbc = requests.get("https://www.bbc.co.uk/")
# Here we are creating a function check_response_code
def check_response_code():
    # Here we are using control flow to check the desired print statment
    if response_bbc.status_code == 200:
        print("Success your in!")
    elif response_bbc.status_code == 400:
        print("Page not found")
    elif response_bbc.status_code == 404:
        print("oops sorry something went wrong")
    else:
        print("Could not identify the status code, Please try another website")
