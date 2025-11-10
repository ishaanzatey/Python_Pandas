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

# === 5️⃣ Function to clean and extract service names ===
def extract_unique_services(text):
    if pd.isna(text):
        return ""
    # Normalize text: remove hidden characters and newlines
    text = str(text)
    text = re.sub(r'(_x000D_|\r|\n)+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    # Extract service names
    matches = re.findall(r'service[_\s:-]*([A-Za-z0-9_-]+)', text, flags=re.IGNORECASE)

    # Post-cleaning: remove leftover "_x000D" and similar fragments
    clean_matches = []
    for m in matches:
        cleaned = re.sub(r'_x000D', '', m, flags=re.IGNORECASE).strip('_- ')
        if cleaned:
            clean_matches.append(cleaned)

    # Return unique, sorted names
    unique_services = sorted(set(clean_matches), key=str.lower)
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
print(final_df.head(10).to_string(index=False))