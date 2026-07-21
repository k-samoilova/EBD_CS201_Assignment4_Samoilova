import csv

with open("global_sales.csv", "r", encoding="utf-8") as file:
    list_of_dictionaries = csv.reader(file)

import json

with open("regional_tariffs.json", "r", encoding="utf-8") as file:
    dictionary = json.load(file)

