import pandas as pd

# DataFrame = A tabular data structure with rows and columns (2-D)
#             Think of it like a spreadsheet or SQL table

data = {
    "Name": ["Spongbob", "Patrick", "squidward"],
    "age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])      # pd.DataFrame is a constructor

# print(df)   # this gives the entire data frame

# print(df.loc["Employee 2"]) # this will only print the rows for that particular index
# print(df.iloc[1]) # this will only print the rows for that particular index


# # Add a new column to the DataFrame

df["Job"] = ["Cook", "UnEmployed", "Cashier"]   # added a new column

# print(df)



# Add a new rows to the DataFrame

new_rows = pd.DataFrame([{"Name": "Sandy", "age": 28, "Job":"Engineer"},
                         {"Name": "Eugene", "age": 60, "Job":"Manager"}],
                       index=["Employee 4", "Employee 5"])
df = pd.concat([df,new_rows])

print(df)