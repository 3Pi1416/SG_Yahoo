#Par Carrier Hugo 
import json
from flask import Flask, request
from pathlib import Path


class Logic:
    #Class to work with logic information
    #Could add put, post, delete in the futur. 
    def get(self,logic_to_get = None):
        """
        get , get infomation from a json file 
        :param logic_to_get:  logic to get, if none will get all the logic in the file
        :return: logic in the form of json, return empty if file not found
        """
        # could be an acces to a data base in real life
        base_path = str(Path(__file__).parent.resolve())
        full_path = base_path + '/logic.json'
        file = open(full_path, 'r')
        # get data from open file or return error
        try:
            all_data = json.load(file)
            file.close
            if( logic_to_get is None):
                return all_data
            else :
                return all_data[logic_to_get]
        except:
            file.close
            return {}

logic = Logic()
app = Flask(__name__)

#front page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Un beau problème</h1>
<p>Un Seul Api existe : Logic</p>'''


@app.route('/logic', methods=['GET'])
def get_logic():
    logic_to_get = request.args.get('logic')
    return logic.get(logic_to_get)


app.run(None,port = 8000)
