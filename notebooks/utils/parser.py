import IPython.display
import json
from bson import json_util
from dotwiz import DotWiz
from datetime import datetime

# Define a few helper functions
def pretty(j):
    return IPython.display.JSON(json.loads(json_util.dumps(j)))

def tree(d):
    return DotWiz(d)

def to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp/1000.0)

def add_index(array):
    return [{**array_fields, **{'index': array_index + 1}} for array_index, array_fields in enumerate(array)]

