import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Load Dataset
df = pd.read_csv("Dataset.csv")

# Display Dataset Information
print(df.head())
print(df.columns)

# Check Missing Values in Coordinates
print(df[['Latitude', 'Longitude']].isnull().sum())

# Remove Missing Coordinates
df = df.dropna(subset=['Latitude', 'Longitude'])

# =====================================
# Restaurant Distribution Map
# =====================================

restaurant_map = folium.Map(
    location=[df['Latitude'].mean(), df['Longitude'].mean()],
    zoom_start=5
)

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=2,
        fill=True
    ).add_to(restaurant_map)

restaurant_map.save("restaurant_map.html")

print("Map saved successfully")

# =====================================
# Restaurant Concentration by City
# =====================================

city_counts = df['City'].value_counts()

print("\nTop 10 Cities by Restaurant Count:")
print(city_counts.head(10))

plt.figure(figsize=(12, 6))
city_counts.head(10).plot(kind='bar', color='skyblue')

plt.title("Top 10 Cities by Restaurant Count")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("city_distribution.png")
plt.show()

# =====================================
# Average Rating by City
# =====================================

city_rating = df.groupby('City')['Aggregate rating'].mean()

city_rating = city_rating.sort_values(ascending=False)

print("\nTop 10 Cities by Average Rating:")
print(city_rating.head(10))

plt.figure(figsize=(12, 6))
city_rating.head(10).plot(kind='bar', color='green')

plt.title("Top Cities by Average Rating")
plt.ylabel("Average Rating")

plt.tight_layout()

plt.savefig("rating_analysis.png")
plt.show()

# =====================================
# Average Price Range by City
# =====================================

city_price = df.groupby('City')['Price range'].mean()

city_price = city_price.sort_values(ascending=False)

print("\nTop 10 Cities by Average Price Range:")
print(city_price.head(10))

plt.figure(figsize=(12, 6))
city_price.head(10).plot(kind='bar', color='orange')

plt.title("Average Price Range by City")
plt.ylabel("Price Range")

plt.tight_layout()

plt.savefig("price_analysis.png")
plt.show()

# =====================================
# Most Popular Cuisine by City
# =====================================

df['Cuisines'] = df['Cuisines'].fillna('Unknown')

popular_cuisine = (
    df.groupby('City')['Cuisines']
    .agg(lambda x: x.mode()[0])
)

print("\nMost Popular Cuisine by City:")
print(popular_cuisine.head(20))

# =====================================
# Locality Analysis
# =====================================

locality_count = (
    df['Locality']
    .value_counts()
    .head(10)
)

print("\nTop 10 Localities by Restaurant Count:")
print(locality_count)

plt.figure(figsize=(12, 6))

locality_count.plot(
    kind='bar',
    color='purple'
)

plt.title("Top Localities by Restaurant Count")
plt.xlabel("Locality")
plt.ylabel("Number of Restaurants")

plt.tight_layout()

plt.savefig("locality_analysis.png")
plt.show()

# =====================================
# Price Range vs Rating Analysis
# =====================================

plt.figure(figsize=(8, 6))

sns.scatterplot(
    x='Price range',
    y='Aggregate rating',
    data=df
)

plt.title("Price Range vs Restaurant Rating")

plt.tight_layout()

plt.savefig("rating_vs_price.png")
plt.show()

print("\nAnalysis Completed Successfully!")