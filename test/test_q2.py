#Par Carrier Hugo 
#tester l'api
import requests

url = "http://127.0.0.1:8000/logic_information"
assert requests.request("GET", url, headers={}, params={}).json() == {'notionalRetrival': {'formula': 'Quantity * last close price', 'source': 'Yahoo Finance'}}

url = "http://127.0.0.1:8000/logic_information?logic=notionalRetrival"
assert requests.request("GET", url, headers={}, params={}).json() == {'formula': 'Quantity * last close price', 'source': 'Yahoo Finance'}