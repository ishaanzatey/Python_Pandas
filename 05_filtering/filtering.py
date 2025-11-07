import pandas as pd

df = pd.read_csv("/Users/ishan/Documents/BroCode_Padas/04_selection/pokemon.csv", index_col="Name")

tall_pokemon = df[df["Height"] > 2]
heavy_pokemon = df[df["Weight"] > 200]
legend_pokemon = df[(df["Legendary"]==1)]
water_pokemon = df[(df["Type1"] == "Water") |
                   (df["Type2"]=="Water")]

fire_flying_pokemon = df[(df["Type1"]=="Fire") &
                         (df["Type2"]=="Flying")]


print(tall_pokemon)
print(heavy_pokemon)
print(legend_pokemon)
print(water_pokemon)
print(fire_flying_pokemon)