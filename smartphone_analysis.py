import matplotlib.pyplot as plt
import pandas as pd

# 1. Load the data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Smartphones sold": [150, None, 220, 310],
}
df = pd.DataFrame(data)

# 2. Clean the data (Fill missing NaN value with 200)
df["Smartphones sold"] = df["Smartphones sold"].fillna(200)

# 3. Filter the data (Create a separate spreadsheet for months over 200)
booming_months = df[df["Smartphones sold"] > 200]

print("--- Booming Months Only (Terminal Printout) ---")
print(booming_months)
print("-----------------------------------------------")

# 4. Draw, title, and show the chart (Using the original 'df' to show all months)
df.plot(kind="line", x="Month", y="Smartphones sold")
plt.title("Monthly Smartphone sales")
plt.show()