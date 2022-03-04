
import requests

url = "http://127.0.0.1:5000/logic"

print( requests.request("GET", url, headers={}, params={}).json())