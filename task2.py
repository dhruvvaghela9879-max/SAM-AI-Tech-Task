import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("E:\Python\project\Zomatodata.csv")

# Check first 5 rows
print(df.head())

# Count cuisine combinations
cuisine_count = df["Cuisine"].value_counts()

print("\nTop 10 Cuisine Combinations:")
print(cuisine_count.head(10))

# Plot top 10 combinations
cuisine_count.head(10).plot(kind="bar", figsize=(10,5))
plt.title("Top 10 Cuisine Combinations")
plt.xlabel("Cuisine Combination")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Average rating of each cuisine combination
avg_rating = df.groupby("Cuisine")["Avg_Rating_Cuisine"].mean()

print("\nTop Rated Cuisine Combinations:")
print(avg_rating.sort_values(ascending=False).head(10))

# Plot top rated combinations
avg_rating.sort_values(ascending=False).head(10).plot(kind="bar", figsize=(10,5))
plt.title("Top Rated Cuisine Combinations")
plt.xlabel("Cuisine Combination")
plt.ylabel("Avg_Rating_Cuisine")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()