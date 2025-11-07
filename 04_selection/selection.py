import pandas as pd

df = pd.read_csv("/Users/ishan/Documents/BroCode_Padas/04_selection/pokemon.csv", index_col="Name")

####################################################################
# SELECTION by column

# print(df.head())
# print(df["Table 1"].head())
# print(df.columns)

# print(df["Name"])
# print(df["Name"].to_string())   # we can select the single column like this
# print(df[["Name", "Height", "Weight"]].to_string()) # selecting multiple columns

####################################################################


# SELECTION by row

# print(df.loc[0])   # selecting the 1st row data
# print(df.loc["Charizard", ["Height", "Weight"]])    # if you only want the 2 columns data for 1 label

# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])    # if you only want the 2 columns data from a range starting range and ending range label

print(df.iloc[0:11:2])  # getting the data as per the index base



# 0:11:2 is the rows and 0:3 is for columns
print(df.iloc[0:11:2, 0:3]) # getting the silced data for only 3 columns which is from 0 to 3 column
# print(df)