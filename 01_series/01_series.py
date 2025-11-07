import pandas as pd

# series  = A pandas 1_dimensional labeled array that can hold any data type
#           Think of it like a single column in a spreadsheet(1-Dimensional)

data = [100 ,102 ,104, 200, 202]

# data = ["a", "b", "c"]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])    # ps.Series is a constructor

# series.loc["c"] = 200       # this will change the value at the index where the label of c is indexed

# print(series.iloc[0])       # we can print by using the ixdex

# print(series.loc["c"])  # this will return the value of the label at that index

# print(series[series >= 200])     # this will print the labesl which have the value more than 200

# print(series[series < 200])     # this will print the labesl which have the value less than 200

