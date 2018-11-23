import csv
import json
import random

with open('slots.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

profiles = {}
index = 1

while index < len(data):
    slot = "Slot " + str(index)
    profiles[slot] = {
        "billing": {
            "address":"",
            "apt":"",
            "city":"",
            "country":None,
            "firstName":"",
            "lastName":"",
            "phoneNumber":"",
            "state":None,
            "zipCode":""
        },
        "billingMatch": True,
        "card": {
            "cvv": data[index][13],
            "holder": data[index][9],
            "month": data[index][11],
            "number": data[index][10],
            "year": data[index][12]
        },
        "email": data[index][3],
        "profileName": slot,
        "shipping": {
            "address": data[index][4],
            "apt": data[index][5],
            "city": data[index][6],
            "firstName": data[index][1],
            "lastName": data[index][2],
            "phoneNumber": data[index][14],
            "state": data[index][7],
            "zipCode": data[index][8]
        }
    }
    index += 1

with open('dasheProfiles.json', 'w') as outfile:
    json.dump(profiles, outfile)
