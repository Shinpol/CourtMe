from pathlib import Path

cities = ["La+Puente", "Arcadia"]


data = {
    "city": [],
    "name": [],
    "address": [], 
    "address_link": []
}

##df = pd.DataFrame(data)
count = 1
city = 0
unparsed_file = Path(r"..\DataSets\LACCommunityCenters.txt")

name = "<h4 class=\"shadow\"><a href=\"/lac/Location"
address = "<a href=\"https://maps.google.com?daddr="

try:
    with open(unparsed_file, "r") as file:
        for line in file:
            content = line.trim()
            if len(content) < len(name):
                continue 
            if content[0:len(name)] == name:
                num = str(count) + ". "
                begin = content.find(num) + len(num)
                end = content.find("</a>")
                data["city"].append(cities[city])
                data["name"].append(content[begin:end])
                count = count + 1 
            if len(content) < len(address):
                continue 
            if content[0:len(address)] == address:
                begin = len(address) +  1
                end = content.find("\" class=\"btn")
                add = content[begin, end]
                data["address"].append(add)
                data["address_link"].append("https://maps.google.com?daddr=" + add )
            
            if count > 20: 
                count = 1
                city = city + 1 
            if city >= len(cities):
                break 
except FileNotFoundError:
    print("The file was not found.")

print(data)


            




except FileNotFoundError:
    print("The file was not found.")


