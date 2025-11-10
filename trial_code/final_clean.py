import pandas as pd
import re

# === 1️⃣ File paths ===
input_path = "/Users/ishan/Documents/BroCode_Padas/trial_code/incident_data.xlsx"
output_path = "/Users/ishan/Documents/BroCode_Padas/trial_code/cleaned_service_names.xlsx"

# === 2️⃣ Load Excel ===
df = pd.read_excel(input_path)
print(f"✅ Total rows read from Excel: {len(df)}")
print(f"✅ Columns detected: {list(df.columns)}\n")

# === 3️⃣ Normalize column names ===
df.columns = df.columns.str.strip().str.lower()

# === 4️⃣ Identify columns dynamically ===
short_desc_col = next((col for col in df.columns if "short" in col), None)
worknotes_col = next((col for col in df.columns if "work" in col or "comment" in col), None)
mnemonic_col = next((col for col in df.columns if "mnemonic" in col), None)

if not short_desc_col or not worknotes_col or not mnemonic_col:
    raise KeyError("❌ Could not find required columns: Short Description / Worknotes / Mnemonic")

# === 5️⃣ Function to clean and extract unique service names ===
def extract_unique_services(text):
    if pd.isna(text):
        return ""
    text = str(text)

    # Clean encoded newlines and unwanted text
    text = re.sub(r'_x000[DdAabB]_?', ' ', text)   # removes _x000D, _x000A, etc.
    text = re.sub(r'[\r\n\t]+', ' ', text)         # removes line breaks/tabs
    text = re.sub(r'\s+', ' ', text).strip()       # normalize spaces

    # Extract only valid "service_name" patterns (case-insensitive)
    matches = re.findall(r'\bservice_name[0-9a-zA-Z_-]*\b', text, flags=re.IGNORECASE)

    # Clean and deduplicate
    clean_matches = [m.strip().lower() for m in matches if m]
    unique_services = sorted(set(clean_matches))

    return ", ".join(unique_services)

# === 6️⃣ Apply extraction ===
df["unique_services"] = df[worknotes_col].apply(extract_unique_services)

# === 7️⃣ Keep only required columns ===
final_df = df[[short_desc_col, "unique_services", mnemonic_col]]

# === 8️⃣ Save output ===
final_df.to_excel(output_path, index=False)
print(f"✅ Extraction complete! Processed {len(df)} rows.")
print(f"➡️ Cleaned data saved to: {output_path}\n")

# === 9️⃣ Show preview ===
print("📘 Preview of cleaned data:")
print(final_df.to_string(index=False))
