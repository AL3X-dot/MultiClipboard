import json

from flask import jsonify

FILE_PATH = './data/data.json'



with open(FILE_PATH,'r+') as f:
    data = json.load(f)
    print(data)
    json.dump({'key':'value'},f)
    f.truncate()