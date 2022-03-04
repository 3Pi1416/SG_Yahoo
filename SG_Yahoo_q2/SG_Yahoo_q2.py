import json
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from pathlib import Path


class Logic():
    def get():
        # could be an acces to a data base in real life
        base_path = str(Path(__file__).parent.resolve())
        full_path = base_path + "/logic.json"
        file = open(full_path, "r")
        # get data from open file or return error
        try:
            all_data = json.load(file)
            file.close
            return all_data
        except:
            file.close
            return "no logic found"


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Un beau probleme</h1>
<p>Un Seul Api existe : Logic</p>'''


@app.route('/logic', methods=['GET'])
def get_logic():
    return Logic.get()

app.run()
