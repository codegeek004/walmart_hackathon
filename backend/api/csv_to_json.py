import csv
import json
def csv_to_json(csv_file_path, json_file_path):
    json_list = []
    with open(csv_file_path, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            json_list.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(json_list, indent=4)
        jsonf.write(jsonString)


csv_file_path = 'data.csv'
json_file_path = 'data.json'

csv_to_json(csv_file_path, json_file_path)


