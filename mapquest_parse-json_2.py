import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Rome, Italy"
dest = "Frascati, Italy"
key = "rczb2neOh8r0Cbhj1WWjfMhDwUaqo6X5"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")

