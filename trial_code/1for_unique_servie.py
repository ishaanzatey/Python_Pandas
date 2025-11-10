import pandas as pd
import re
import os

# === [1] Read the Excel file dynamically ===
input_file = "/Users/ishan/Documents/BroCode_Padas/trial_code/incident_data.xlsx"
output_file = "/Users/ishan/Documents/BroCode_Padas/trial_code/cleaned_service_names.xlsx"

# Read everything — even blank or hidden rows
df = pd.read_excel(
    input_file,
    keep_default_na=False,   # prevents dropping rows with blanks
    na_filter=False          # ensures empty cells are read as empty strings
    ,header=1
)

print(f"✅ Total rows read from Excel: {len(df)}")
print(f"✅ Columns detected: {list(df.columns)}\n")

# === [2] Clean the data (remove hidden chars like _x000D_) ===
df = df.replace({'_x000D_': '', '\r': '', '\n': ''}, regex=True)

# Try to detect the correct column name case-insensitively
possible_columns = [c for c in df.columns if 'work' in c.lower()]
if not possible_columns:
    raise KeyError("❌ Could not find 'Worknotes' column in the Excel file.")
worknotes_col = possible_columns[0]

# === [3] Define function to extract all service names ===
def extract_all_services(text):
    if not isinstance(text, str):
        return []
    # find matches like: service name, service: name, Service_name2, etc.
    pattern = r'\bservice[:\s_-]*([a-zA-Z0-9_-]+)?'
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    # filter out empty results, remove duplicates, and strip spaces
    unique_matches = sorted(set([m.strip() for m in matches if m.strip()]))
    return unique_matches

# === [4] Apply extraction to all rows ===
df["unique_services"] = df[worknotes_col].apply(extract_all_services)

# === [5] Save to new Excel file ===
df.to_excel(output_file, index=False)

# === [6] Print preview ===
print(f"✅ Extraction complete! Processed {len(df)} rows.")
print(f"➡️ Cleaned data saved to: {output_file}\n")

print("📘 Preview of extracted service names:")
print(df[[worknotes_col, "unique_services"]].head(10).to_string(index=False))
