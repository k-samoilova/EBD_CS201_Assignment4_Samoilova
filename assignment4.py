import csv
import json

with open("global_sales.csv", "r", encoding="utf-8") as file:
    list_of_dictionaries = list(csv.DictReader(file))


with open("regional_tariffs.json", "r", encoding="utf-8") as file:
    dictionary = json.load(file)

for x in list_of_dictionaries:
    if x["quantity"] == "N/A":
        x["quantity"] = 0
    if x["revenue"] == "N/A":
        x["revenue"] = 0
    x["quantity"] = int(x["quantity"])
    x["revenue"] = float(x["revenue"])

for a in dictionary:
    if dictionary[a] == "N/A":
        dictionary[a] = 0
    else:
        dictionary[a] = float(dictionary[a])

for x in list_of_dictionaries:
    x["net_profit"] = round(x["revenue"] - (x["revenue"] * dictionary[x["region"]]/100),2)

with open("cleaned_sales_updated.csv", "w", encoding="utf-8", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=list_of_dictionaries[0].keys())
    writer.writeheader()
    writer.writerows(list_of_dictionaries)
