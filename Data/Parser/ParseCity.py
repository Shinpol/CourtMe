from pathlib import Path

unparsed_file = Path(r"..\DataSets\LACCityUnParsed.txt")
parsed_file = Path(r"..\DataSets\LACCityParsed.txt")

content = ""
try:
    with open(unparsed_file, "r") as file:
        for line in file:
            content = content + line.split()[0] + "\n"
except FileNotFoundError:
    print("The file was not found.")

try:
    with open(parsed_file, "w") as file:
        file.write(content)
        
except FileNotFoundError:
    print("The file was not found.")


