import requests 


##req = "https://locator.lacounty.gov/lac/Search?" &

community_centers = {
    "find": "Community+Centers+(Park+Amenities)",
    "near": "La+Puente",
    "tag": "43909",
    "page": "1",
    "pageSize": "50"
}

parks_tennis = {
    "find": "Parks+and+Gardens",
    "near": "La+Puente",
    "tag": "43909", #34
    "page": "1",
    "pageSize": "50"
}

parks_pb = {
    "find": "Parks+and+Gardens",
    "near": "La+Puente",
    "tag": "34",
    "page": "1",
    "pageSize": "50"
}

def create_request(d):
    req = "https://locator.lacounty.gov/lac/Search?" 
    for key in d: 
        req = req + key + "=" + d[key] + "&"
    req = req[0:len(req) - 1]
    print(req)


create_request(community_centers)

#response = requests.get()