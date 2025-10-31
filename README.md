# Seasonality Analysis for Sub-Industry Spend Data

This Python script analyzes seasonal spending patterns across multiple years for each sub-industry. It normalizes spending values within each year, calculates average seasonal performance across years, and categorizes months as **High**, **Medium**, or **Low** seasonality periods.

## Description
The script processes advertising or sales spend data to highlight when each sub-industry tends to perform best throughout the year.  
It does this by:
1. Normalizing spend values by year and sub-industry.
2. Calculating the average normalized score (Seasonal Score) for each month.
3. Converting scores into percentages.
4. Assigning a **Seasonal Indicator** (High, Medium, or Low) based on performance levels.
5. Saving the final dataset to an Excel file for reporting or visualization.

## Input
- **spend_data.xlsx** → Must contain the following columns:
  - `year`
  - `month`
  - `sub-industry`
  - `Sum of Value` (total spend)

## Output
- **seasonality_output.xlsx** → Includes:
  - Normalized_Year (%)
  - Seasonal_Score (%)
  - Seasonal_Indicator (High / Medium / Low)

## How to Use
1. Place your input Excel file in the same folder as the script and name it: *spend_data.xlsx*
2.  Run the script
3.   The output Excel file `seasonality_output.xlsx` will be generated in the same folder.

## Example Use Case
This analysis helps identify which months historically show higher spending or engagement for each sub-industry — useful for **campaign planning, demand forecasting, or budget allocation.**

