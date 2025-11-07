import pandas as pd

# df = pd.read_csv("/Users/ishan/Documents/BroCode_Padas/03_import_csv_&_json/pokemon.csv")
df = pd.read_json("/Users/ishan/Documents/BroCode_Padas/03_import_csv_&_json/pokemon.json")

print(df)   # this will only give the first 5 rows and the last 5 rows

print(df.to_string())   # this will give all the rows

