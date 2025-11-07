import pandas as pd

# Data cleaning = The process of fixing /removing
#                 incomplete, incorrect, or irrevalent data.
#                 ~75% of work done with pandas in data cleaning 


df = pd.read_csv("/Users/ishan/Documents/BroCode_Padas/07_data_cleaning/pokemon.csv")


# # 1. Drop irrevalent column

# df = df.drop(columns=["Legendary" , "No"])

# print(df)


# Handle missing data

# df = df.dropna(subset=["Type2"])    # willl remove any rows which has null value or the values not availble

# df = df.fillna({"Type2": "None"})    # this will replace the Nan(Not a number to the none)

# print(df.to_string())


# # 3. Fix inconsistent values

# df["Type1"] = df["Type1"].replace({"Grass":"GRASS",
#                                    "Fire":"FIRE",
#                                    "Water":"WATER"})    # we can replace the words from the table

# print(df.to_string())



# # 4. Standardize data

# df["Name"]= df["Name"].str.lower()    # this will convert all the words to lower case

# print(df.to_string())



# 5. Fix the datatypes

# df["Legendary"] = df["Legendary"].astype(bool)    # this will convert the data type to boolean

# print(df.to_string())



# 6. Remove duplicate entrys

df = df.drop_duplicates()

print(df.to_string())