import pandas as pd

# Read input Excel
df = pd.read_excel("spend_data.xlsx")

# --- Step 1: Normalize within each Year & SubIndustry ---
df["Normalized_Year"] = df.groupby(["year", "sub-industry"])["Sum of Value"].transform(
    lambda x: x / x.max() if x.max() != 0 else 0
)

# --- Step 2: Compute Seasonal Score (avg across years for each SubIndustry & Month) ---
seasonal_scores = (
    df.groupby(["sub-industry", "month"])["Normalized_Year"]
    .mean()
    .reset_index()
    .rename(columns={"Normalized_Year": "Seasonal_Score"})
)

# Merge back to main DataFrame
df = df.merge(seasonal_scores, on=["sub-industry", "month"], how="left")

# --- Step 3: Convert to percentages ---
df["Normalized_Year"] = (df["Normalized_Year"] * 100).round(2)
df["Seasonal_Score"] = (df["Seasonal_Score"] * 100).round(2)

# --- Step 4: Add Seasonal Indicator ---
def categorize(score):
    if score > 60:
        return "High"
    elif score >= 30:
        return "Medium"
    else:
        return "Low"

df["Seasonal_Indicator"] = df["Seasonal_Score"].apply(categorize)

# --- Step 5: Save output to Excel ---
df.to_excel("seasonality_output.xlsx", index=False)

print("Seasonality analysis complete. Output saved as 'seasonality_output.xlsx'")
