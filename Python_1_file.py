import pandas as pd
import matplotlib.pyplot as plt

    # =====================================================================
# 2. READ CSV AND VERIFY THE DATA
# =====================================================================
print("Step 2: Loading data into Pandas...")
df = pd.read_csv(r"D:\Python_Code_Practice\gini_data.csv")


# Display the first few rows
print("\n--- FIRST 5 ROWS OF THE DATASET ---")
print(df.head())
print("-----------------------------------\n")

# =====================================================================
# 3. CLEAN, FILTER, AND PLOT THE DATA
# =====================================================================
print("Step 3: Preparing data for visualization...")

# Identify the Gini column dynamically (since the name might be long)
gini_col = [col for col in df.columns if "Gini" in col][0]

# Rename columns to match your preferred naming
df = df.rename(columns={"Entity": "Country", gini_col: "Gini_Index"})

# Remove rows with missing Gini values
df_clean = df.dropna(subset=["Gini_Index"])

# Note: Since Gini coefficient data for 2024 is highly incomplete or empty,
# we will grab the LATEST available year for each country in the dataset.
df_latest = df_clean.sort_values("Year").groupby("Country").last().reset_index()

# If you only want to plot a subset (e.g., top 40 countries for readability)
df_plot = df_latest.sort_values(by="Gini_Index").tail(40)

print(
    f"Plotting the latest available Gini index data for {len(df_plot)} countries..."
)

# Plotting the data
plt.figure(figsize=(15, 8))
plt.bar(
    df_plot["Country"],
    df_plot["Gini_Index"],
    color="crimson",
    edgecolor="black",
)

plt.title(
    "Global Gini Index Breakdown (Latest Available Year)",
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Countries", fontsize=12)
plt.ylabel("Gini Index (0 to 100 or 0 to 1)", fontsize=12)
plt.xticks(rotation=90, fontsize=8)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

# Show the plot
plt.show()


import plotly.express as px

# ==========================================================
# Interactive Plotly Bar Chart
# ==========================================================

fig = px.bar(
    df_plot,
    x="Country",
    y="Gini_Index",
    color="Gini_Index",
    color_continuous_scale="Reds",
    text="Gini_Index",
    title="Country-wise Gini Index (Latest Available Year)"
)

fig.update_layout(
    xaxis_title="Country",
    yaxis_title="Gini Index",
    xaxis_tickangle=-90,
    width=1400,
    height=700,
    template="plotly_white"
)

fig.update_traces(textposition="outside")

fig.show()

import plotly.express as px

fig = px.choropleth(
    df_latest,
    locations="Code",          # ISO-3 country codes
    color="Gini_Index",
    hover_name="Country",
    hover_data=["Year", "Gini_Index"],
    color_continuous_scale="Reds",
    projection="natural earth",
    title="Global Gini Index (Latest Available Year)"
)

fig.update_layout(
    width=1200,
    height=700,
    margin=dict(l=0, r=0, t=50, b=0)
)

fig.show()