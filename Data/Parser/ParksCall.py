import requests 
from pathlib import Path
import pandas as pd 
import time
import random 

import ParseHtml

##req = "https://locator.lacounty.gov/lac/Search?" &

def create_request(d):
    req = "https://locator.lacounty.gov/lac/Search?" 
    for key in d: 
        req = req + key + "=" + d[key] + "&"
    req = req[0:len(req) - 1]
    return req


def call_request(d):
    d_req = create_request(d)
    d_res = requests.get(d_req)
    return d_res



