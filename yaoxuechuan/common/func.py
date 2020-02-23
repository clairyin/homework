import json
from common.base import BaseObj

def print_json(x):
    print(json.dumps(x, indent=4, ensure_ascii=False))

def to_dict(obj):
    try:
        return obj.__dict__
    except  Exception as e:
        return obj

def dict_to_json(obj):
    return json.dumps(obj,default=to_dict)

def to_json(j):
    try:
        return BaseObj(**j)
    except Exception as e:
        return j

def json_to_dict(j):
    return json.loads(json.dumps(j),object_hook=to_json)
