import pandas as pd
import matplotlib.pyplot as plt

# 1. Read CSV
df = pd.read_csv("car_info.csv")
print("Shape of the dataframe:", df.shape)

# 2. Japanese cars with V6 engines
japanese_v6 = df[(df['origin'] == 'japan') & (df['cylinders'] == 6)]
print("Japanese v6 cars:", list(japanese_v6['car']))

# 3. Cars with missing horsepower
missing_hp = df[df['horsepower'].isna()]
print("Cars with missing horsepower data:", list(missing_hp['car']))

# 4. Cars with mpg >= 20
print("Number of cars having mpg >= 20:", df[df['mpg'] >= 20].shape[0])

# 5. Car with highest mpg
max_mpg_car = df[df['mpg'] == df['mpg'].max()]['car']
print("Most fuel-efficient car:", list(max_mpg_car))

# 6. Weight stats
print("minimum weight:", df['weight'].min(),
      "maximum weight:", df['weight'].max(),
      "average weight:", round(df['weight'].mean(), 2))

# 7. Drop rows with any missing values
df_clean = df.dropna()
print("Shape after removing the missing values:", df_clean.shape)

# 8. Pie chart – car origin distribution
plt.figure(figsize=(6, 6))
df['origin'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Cars Manufactured by Country")
plt.ylabel("")
plt.show()

# 9. Two vertical scatter subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Subplot 1: mpg vs weight
ax1.scatter(df['weight'], df['mpg'])
ax1.set_xlabel("Weight")
ax1.set_ylabel("MPG")
ax1.set_title("MPG vs Weight")
ax1.legend(["mpg vs weight"])

# Subplot 2: mpg vs displacement
ax2.scatter(df['displacement'], df['mpg'])
ax2.set_xlabel("Displacement")
ax2.set_ylabel("MPG")
ax2.set_title("MPG vs Displacement")
ax2.legend(["mpg vs displacement"])

plt.tight_layout()
plt.show()
