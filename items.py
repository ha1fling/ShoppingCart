import json
import os


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'items.json')) as json_file:
    data = json.load(json_file)