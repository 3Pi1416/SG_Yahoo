# Par Carrier Hugo
import requests
from flask import Flask, request, jsonify,abort
from LogicInformation import LogicInformation


def request_yahoo_quote_regular_market_previous_close(product: str, region: str = "US"):
    """
    request_yahoo_quote_regularMarketPreviousClose get
    :param product: symbol you want to search via yahoo finance
    :param region: could be use to change the region
    :return: regular market previous close ( last close price), none if it did not find anything
    """
    # api might have chance, market/get-summary was on v2 and did not take symbol as an input.
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"

    query_string = {"symbol": product, "region": region}

    headers = {
        "x-rapidapi-host": "yh-finance.p.rapidapi.com",
        # please, don't abuse it, it should have been private
        "x-rapidapi-key": "1ff1c60385msh92ed0e32a2fa903p105892jsn24b1705030c5"
    }
    price_to_return = None
    try:
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        # to be sure that the request work and we dont have an empty shell with the skeleton but no values
        if(response.status_code == 200):
            price_to_return = response.json()["price"]["regularMarketPreviousClose"]["raw"]
    except:  # depeding on how the client want it, many exception cases can existe with requests.exceptions
        price_to_return = None

    return price_to_return


def ask_basic_info():
    """
    ask_basic_info ask the quantity and product (symbol) to calculate the notional of the position.
    It verify if the input for quantity is a number
    :return quantity: quantity as float. If the input was not a number, return none.
    :return product: product (symbol). None if quantity was not a number.
    """
    quantity = input("Quantity:")
    # Try float because with the new trend (fraction of a stock), we might want a float.
    try:
        quantity = float(quantity)
    except:
        return None, None

    product = input("Product:")
    return quantity, product

logic_information = LogicInformation()
app = Flask(__name__)

@app.errorhandler(400)
def bad_input(e):
    return jsonify(error=str(e)), 400

# front page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Un beau problème</h1>
<p>API 1 : logic_information: donne l'information sur les calcul</p>
<p>API 2 : notional: donne le notionel, prend comme entrées : "quanity" et "product" </p>'''

#api to get how information is caculated
@app.route('/logic_information', methods=['GET'])
def get_logic_information():
    logic_to_get = request.args.get('logic')
    return logic_information.get(logic_to_get)

#api to get the notional with a quantity and product
@app.route('/notional', methods=['GET'])
def get_logic():
    quantity = request.args.get('quantity')
    product = request.args.get('product')
    if(product is None or quantity is None):
        abort(400, "quantity or product are missing")
    try:
        quantity = float(quantity)
    except:
        abort(400, "quantity must be a number")

    price = request_yahoo_quote_regular_market_previous_close(product)
    if (price is None):
        abort(400, "yahoo data retrieval failed")
        
    return jsonify(notional=price*quantity)

app.run(None, port=8000)


"""
To run in local terminal
"""

# """
# Main function to run the project
# """
# while(True):
#     quantity, product = ask_basic_info()
#     if(quantity is None):
#         to_continue = input(
#             "Your input was not valid, do you want to try again? ([y]es or [n]o)\n")
#     else:
#         price = request_yahoo_quote_regularMarketPreviousClose(product)
#         if(price is None):
#             to_continue = input("An error happen while searching for the information,"
#                                 "do you want to try again? ([y]es or [n]o)\n")
#         else:
#             print(price * quantity)
#             to_continue = input("\nDo you want to continue with,"
#                                 "another query ([y]es or [n]o)\n")

#     if(not(to_continue.upper() == "Y" or to_continue.upper == "YES")):
#         exit(0)
