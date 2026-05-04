from pathlib import Path

city_file = Path(r"..\DataSets\LACCityParsed.txt")
def get_cities():
    cities = []
    try:
        with open(city_file, "r") as file:
            for line in file:
                content = line.split()[0]
                cities.append(content)
            return cities
    except FileNotFoundError:
        print("The file was not found.")