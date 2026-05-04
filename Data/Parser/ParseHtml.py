import re


def parse(html):
    names = re.findall(r"(?<=>[0-9]..)(.*)(?=<\/a)", html)
    addresses = re.findall(r'(?<=https:\/\/maps\.google\.com\?daddr=)(.*)(?=".class)', html)
    address_links = []
    for x in addresses:
        address_links.append("https://maps.google.com/maps?q=" + x)

    return {
        "name": names, 
        "address": addresses,
        "address_link": address_links
    }

