import csv
import json

csvfile = open('/Users/ishan/Documents/BroCode_Padas/03_import_csv_&_json/pokemon.csv', 'r')
jsonfile = open('/Users/ishan/Documents/BroCode_Padas/03_import_csv_&_json/pokemon.json', 'w')

reader = csv.DictReader(csvfile)
data = list(reader)
json.dump(data, jsonfile, indent=2)

csvfile.close()
jsonfile.close()
