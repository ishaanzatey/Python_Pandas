import pandas as pd

df = pd.read_csv("/Users/ishan/Documents/BroCode_Padas/04_selection/pokemon.csv", index_col="Name")

pokemon = input("Enter the pokemon name: ")


try:
    print(df.loc[pokemon])
except KeyError:
    print(f"Pokemon {pokemon} not found")
