import requests 
from pathlib import Path
import pandas as pd 
import time
import random 


##req = "https://locator.lacounty.gov/lac/Search?" &

community_centers = {
    "find": "Community+Centers+(Park+Amenities)",
    "near": "",
    "tag": "43909",
    "page": "1",
    "pageSize": "20"
}

parks_tennis = {
    "find": "Parks+and+Gardens",
    "near": "",
    "tag": "43909", #34
    "page": "1",
    "pageSize": "20"
}

parks_pb = {
    "find": "Parks+and+Gardens",
    "near": "",
    "tag": "34",
    "page": "1",
    "pageSize": "20"
}

def create_request(d):
    req = "https://locator.lacounty.gov/lac/Search?" 
    for key in d: 
        req = req + key + "=" + d[key] + "&"
    req = req[0:len(req) - 1]
    return req


response = ""

city_file = Path(r"..\DataSets\LACCityParsed.txt")
cities = []
try:
    with open(city_file, "r") as file:
        for line in file:
            cities.append(line.strip())
except FileNotFoundError:
    print("The file was not found.")

community_centers_content = ""
parks_tennis_content = ""
parks_pb_content = ""

community_centers_file = Path(r"..\DataSets\LACCommunityCenters.txt")
parks_tennis_file = Path(r"..\DataSets\LACParksTennis.txt")
parks_pb_file = Path(r"..\DataSets\LACParksPB.txt")

cities = ["La+Puente", "Arcadia"]

for x in cities: 

    print(x)

    community_centers["near"] = x
    parks_tennis["near"] = x
    parks_pb["near"] = x

    community_centers_req = create_request(community_centers)
    community_centers_res = requests.get(community_centers_req)
    #community_centers_content = community_centers_content + community_centers_req.text
    try:
        with open(community_centers_file, "a") as file:
            file.write(community_centers_res.text)
            
    except FileNotFoundError:
        print("The file was not found.")
    
    print("appended community centers")

    time.sleep(random.randint(1, 15))

    parks_tennis_req = create_request(parks_tennis)
    parks_tennis_res = requests.get(parks_tennis_req)
    #parks_tennis_content = parks_tennis_content + parks_tennis_req.text
    try:
        with open(parks_tennis_file, "a") as file:
            file.write(parks_tennis_res.text)
            
    except FileNotFoundError:
        print("The file was not found.")

    print("appended parks tennis")

    time.sleep(random.randint(1, 15))

    parks_pb_req = create_request(parks_pb)
    parks_pb_res = requests.get(parks_pb_req)
    #parks_pb_content = parks_pb_content + parks_pb_req.text
    try:
        with open(parks_pb_file, "a") as file:
            file.write(parks_pb_res.text)
            
    except FileNotFoundError:
        print("The file was not found.")

    print("appended parks pickleball")

    time.sleep(random.randint(1, 15))

print("file has finished running")
