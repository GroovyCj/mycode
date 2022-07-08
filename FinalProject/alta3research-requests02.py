#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/metal"





new_metal={
        "name" : "Liquid Snake",
        "realname" : "Eli",
        "friend" : "none",
        "first appearance" : "Metal Gear Solid"}





new_metal = json.dumps(new_metal)





resp = requests.post(URL, json=new_metal)


pprint(resp.json())
