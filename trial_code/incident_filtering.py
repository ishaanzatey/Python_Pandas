import pandas as pd
import os
import re


df= pd.read_excel("/Users/ishan/Documents/BroCode_Padas/trial_code/incident_data.xlsx", header=1)

extracted_req_data = df[["Short Description", "Comments and Worknotes", "Mnemonic"]]

print(extracted_req_data.columns)


# === Step 3: Clean unwanted characters ===
extracted_req_data["Comments and Worknotes"] = extracted_req_data["Comments and Worknotes"].astype(str)
extracted_req_data["Comments and Worknotes"] = extracted_req_data["Comments and Worknotes"].replace({'_x000D_': '', r'\n': ' ', r'\r': ' '}, regex=True)

print(extracted_req_data["Comments and Worknotes"])
# extraced_req_data = extraced_req_data[["", "", ""]].copy()

# extraced_req_data = extraced_req_data.replace({'_x000D':''},regex=True)

# print(extraced_req_data)

