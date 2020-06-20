import json


def format(_json):
    return json.dumps(_json, indent=4, sort_keys=False)
