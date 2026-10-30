import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# load the dataset
iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"]=iris.target_names[iris.target]

# display the dataset
print(df.head())

# 1. line plot
plt.figure(figsize=(8, 5))
plt.plot(df.index[:30],df["sepal length (cm)"][:30], marker="o")
plt.title("Line Plot - Sepal Length")
plt.xlabel("Data Index")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.show()

# 2. Bar Plot
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="species", y="sepal length (cm)")
plt.title("Bar Plot - Average Sepal Length")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length (cm)")
plt.show()

# 3. Scatter PLot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="sepal length (cm)",y="petal length (cm)",
    hue="species" )
plt.title("Scatter Plot - Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()

# 4. Heatmap
plt.figure(figsize=(8, 5))
correlation=df.select_dtypes(include="number").corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap - Feature Correlation")
plt.show()
