import ParksCall 
import ParseHtml
import Get
import pandas as pd 
from pathlib import Path
import os

##req = "https://locator.lacounty.gov/lac/Search?" &

"""
community_centers = {
    "find": "Community+Centers+(Park+Amenities)",
    "near": "",
    "tag": "43909",
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
"""

parks_tennis = {
    "find": "Parks+and+Gardens",
    "near": "",
    "tag": "43967", 
    "page": "1",
    "pageSize": "30"
}

example_data = {
    "name": [], 
    "address": [],
    "address_link": [], 
    "tennis_courts": [],
    "pb_courts": [], 
    "city": []
}

csv_file = Path(r"..\DataSets\LACCourts.csv")

def main():
    #cities =  Get.get_cities()
    cities = ["La+Puente"]
    
    df = pd.DataFrame(example_data)
    df.to_csv(csv_file, index=False, header=["name","address","address_link", "tennis_courts", "pb_courts", "city"])
    
    for city in cities:
        #community_centers["near"] = city
        #parks_pb["near"] = city 

        #community_centers_res = ParksCall.call_request(community_centers)
        #parks_pb_res = ParksCall.call_request(parks_pb)

        #community_centers_html = ParseHtml.parse(community_centers_res.text)
        #community_centers_html["type"] = ["community_center"] * 20

        #parks_pb_html = ParseHtml.parse(parks_pb_res.text)
        #parks_pb_html["type"] = ["pickleball"] * 20

        parks_tennis["near"] = city 
        parks_tennis_res = ParksCall.call_request(parks_tennis)
        parks_tennis_html = ParseHtml.parse(parks_tennis_res.text)
                
        total = 30
    
        parks_tennis_html["name"] = parks_tennis_html["name"][0:total]
        parks_tennis_html["address"] = parks_tennis_html["address"][0:total]
        parks_tennis_html["address_link"] = parks_tennis_html["address_link"][0:total]
                
        df = pd.DataFrame(parks_tennis_html)
        df.to_csv(csv_file, mode='a', index=False, header=False)
        

main()
##ParseHtml.howdy()

