
import requests


def request_yahoo_quote_regularMarketPreviousClose(product: str, region: str = "US"):
    """
    request_yahoo_quote_regularMarketPreviousClose get 
    :param product: symbol you want to search via yahoo finance
    :param region: could be use to change the region
    :return: regular market previous close ( last close price), none if it did not find anything
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"

    querystring = {"symbol": product, "region": region}

    headers = {
        "x-rapidapi-host": "yh-finance.p.rapidapi.com",
        # please, don't abuse it, it should have been private
        "x-rapidapi-key": "1ff1c60385msh92ed0e32a2fa903p105892jsn24b1705030c5"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring).json()

    try:
        price_to_return = response["price"]["regularMarketPreviousClose"]["raw"]
    except:
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
    #Try float because with the new trend (fraction of a stock), we might want a float.
    try:
        quantity = float(quantity)
    except:
        return None, None

    product = input("Product:")
    return quantity, product


"""
Main function to run the project
"""
while(True):
    quantity, product = ask_basic_info()
    if(quantity is None):
        to_continue = input(
            "Your input was not valid, do you want to try again? ([y]es or [n]o)\n")
    else:
        price = request_yahoo_quote_regularMarketPreviousClose(product)
        if(price is None):
            to_continue = input("An error happen while searching for the information,"
                                "do you want to try again? ([y]es or [n]o)\n")
        else:
            print(price * quantity)
            to_continue = input("\nDo you want to continue with,"
                                "another query ([y]es or [n]o)\n")
    if(not(to_continue.upper() == "Y" or to_continue.upper == "YES")):
        break
