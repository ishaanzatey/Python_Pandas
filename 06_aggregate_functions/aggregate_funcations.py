import pandas as pd

# Aggregate funcations = Reduce a set of values into a single summary value
#                        Used to summarize and analyze data
#                        Often used with groupby() dunction


df = pd.read_csv("/Users/ishan/Documents/BroCode_Padas/06_aggregate_functions/pokemon.csv")



#####################################################################

# Aggregate funcations = Reduce a set of values into a single summary value
#                        Used to summarize and analyze data
#                        Often used with groupby() dunction

df = pd.read_csv("/Users/ishan/Documents/BroCode_Padas/06_aggregate_functions/pokemon.csv")


##########################################################################

# this will apply to the whole data frame

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())



##########################################################################

# this will apply to the single column

# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())


##########################################################################

# groupby() Function

# print(df)
group = df.groupby("Type1")

# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())