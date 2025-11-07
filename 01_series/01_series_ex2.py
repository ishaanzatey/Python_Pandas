import pandas as pd

calories = {"Day1": 1750,
            "Day2": 2100,
            "Day3": 1700}

series = pd.Series(calories)       # as this is a diectonary it will take the keys as the labels
# print(series)

# print(series.loc["Day1"])
# series.loc["Day3"] += 500

diet_followed = {f"I have followed diet on the day {series[series < 2000]}"}

print(diet_followed)

diet_not_followed = (f"I overate on the {series[series >= 2000]}")

print(diet_not_followed)