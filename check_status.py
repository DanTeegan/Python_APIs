import requests

post_codes_req = requests.get ("https://api.postcodes.io/postcodes/N135PG")

class Live_web_status_code:

    def check_status_code(self):
        if post_codes_req.status_code:
            return "Sucess"
        elif post_codes_req.status_code:
            return "sorry not available"
status = Live_web_status_code() # Creating a class object/instantiating
print(status.check_status_code()) # Calling the method of check_status_code within the class



# print(post_codes_req.status_code)
print(post_codes_req.content)
# print(type(post_codes_req.content))
# print(post_codes_req.headers)
# print(type(post_codes_req.headers))
# print(post_codes_req.status_code)