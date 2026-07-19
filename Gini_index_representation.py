# "How equally is income distributed across different countries, and which countries require policy interventions?"



import pandas as pd
import plotly.express as px

# ==========================================================
# 1. Load Dataset
# ==========================================================

print("Loading dataset...")

df = pd.read_csv(r"D:\Python_Code_Practice\gini_data.csv")

# ==========================================================
# 2. Identify Gini Column Automatically
# ==========================================================

gini_col = [col for col in df.columns if "Gini" in col][0]

# Rename columns
df = df.rename(columns={
    "Entity": "Country",
    
})

# ==========================================================
# 3. Clean Data
# ==========================================================

# Remove missing values
df = df.dropna(subset=["Gini_Index"])

# Keep latest available year for each country
df_latest = (
    df.sort_values("Year")
      .groupby("Country")
      .last()
      .reset_index()
)

print(df_latest.head())

# # ==========================================================
# # 4. World Choropleth Map
# # ==========================================================

# fig = px.choropleth(
#     df_latest,
#     locations="Code",                  # ISO-3 Country Code
#     color="Gini_Index",
#     hover_name="Country",
#     hover_data={
#         "Year": True,
#         "Gini_Index": ':.2f'
#     },
#     color_continuous_scale="YlOrRd",
#     projection="natural earth",
#     title="🌍 Global Gini Index by Country (Latest Available Year)"
# )

# fig.update_layout(
#     width=1400,
#     height=750,
#     title_x=0.5,
#     geo=dict(
#         showframe=False,
#         showcoastlines=True,
#         showcountries=True,
#         countrycolor="black",
#         showland=True,
#         landcolor="lightgray",
#         bgcolor="white"
#     ),
#     coloraxis_colorbar=dict(
#         title="Gini Index"
#     )
# )

# fig.show()

def classify(gini):
    if gini < 0.30:
        return "Low Inequality"
    elif gini < 0.40:
        return "Moderate Inequality"
    elif gini < 0.50:
        return "High Inequality"
    else:
        return "Very High Inequality"

df_latest["Category"] = df_latest["Gini_Index"].apply(classify)
fig = px.choropleth(
    df_latest,
    locations="Code",
    color="Category",
    hover_name="Country",
    hover_data=["Year", "Gini_Index"],
    projection="natural earth",
    title="Global Income Inequality Categories",

    category_orders={
        "Category": [
            "Low Inequality",
            "Moderate Inequality",
            "High Inequality",
            "Very High Inequality"
        ]
    }
)

fig.show()

fig.show()
# top20 = df_latest.sort_values(
#     "Gini_Index",
#     ascending=False
# ).head(20)

# fig = px.bar(
#     top20,
#     x="Country",
#     y="Gini_Index",
#     color="Gini_Index",
#     color_continuous_scale="Reds",
#     title="Top 20 Countries with Highest Income Inequality"
# )

# fig.show()


# bottom20 = df_latest.sort_values(
#     "Gini_Index"
# ).head(20)

# fig = px.bar(
#     bottom20,
#     x="Country",
#     y="Gini_Index",
#     color="Gini_Index",
#     color_continuous_scale="Greens",
#     title="Top 20 Countries with Lowest Income Inequality"
# )

# fig.show()

# fig = px.histogram(
#     df_latest,
#     x="Gini_Index",
#     nbins=25,
#     title="Distribution of Global Gini Index"
# )

# fig.show()


# fig = px.box(
#     df_latest,
#     y="Gini_Index",
#     points="all",
#     title="Global Gini Index Distribution"
# )

# fig.show()


# fig = px.scatter(
#     df_latest,
#     x="Year",
#     y="Gini_Index",
#     color="Gini_Index",
#     hover_name="Country",
#     title="Latest Gini Index by Year"
# )

# fig.show()