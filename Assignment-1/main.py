import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris_data = load_iris()
df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df_iris['class'] = iris_data.target
df_iris['class_name'] = df_iris['class'].apply(lambda x: iris_data.target_names[x])

# a. Total no. of data-points
total_points = len(df_iris)
print(f"Total no. of data-points: {total_points}")

# b. No. of classes
unique_classes = df_iris['class_name'].nunique()
print(f"No. of classes: {unique_classes}")

# c. Data Distribution
distribution = df_iris['class_name'].value_counts()
print("Data Distribution:")
for cname, cnt in distribution.items():
    print(f"{cname} : {cnt}")

# d. No. of features (excluding 'class' and 'class_name')
feature_count = df_iris.shape[1] - 2
print(f"No. of features: {feature_count}")

# e. Min_max of the features
print("Min_max of the features:")
stats_min_max = df_iris[iris_data.feature_names].agg(['min', 'max'])
for feat in iris_data.feature_names:
    print(f"{feat} : {stats_min_max.loc['min', feat]} : {stats_min_max.loc['max', feat]}")

# f. Mean & variance of the features
print("Mean & variance of the features:")
stats_mean_var = df_iris[iris_data.feature_names].agg(['mean', 'var'])
for feat in iris_data.feature_names:
    print(f"{feat} : {stats_mean_var.loc['mean', feat]} : {stats_mean_var.loc['var', feat]}")

# g. Classwise min_max of each feature
print("Classwise min_max of each feature:")
grouped_min_max = df_iris.groupby('class')[iris_data.feature_names].agg(['min', 'max'])
for class_idx in range(unique_classes):
    class_name = iris_data.target_names[class_idx]
    print(f"{class_name}:")
    for feat in iris_data.feature_names:
        print(f"{feat} : {grouped_min_max.loc[class_idx, (feat, 'min')]} : {grouped_min_max.loc[class_idx, (feat, 'max')]}")

# h. Classwise mean & variance of each feature
print("Classwise mean & variance of each feature:")
grouped_mean_var = df_iris.groupby('class')[iris_data.feature_names].agg(['mean', 'var'])
for class_idx in range(unique_classes):
    class_name = iris_data.target_names[class_idx]
    print(f"{class_name}:")
    for feat in iris_data.feature_names:
        print(f"{feat} : {grouped_mean_var.loc[class_idx, (feat, 'mean')]} : {grouped_mean_var.loc[class_idx, (feat, 'var')]}")

# i. Plot the values of each features using different colours for different classes
fig, axes = plt.subplots(2, 2, figsize=(10, 6))
axes = axes.ravel()
colors = plt.colormaps['tab10']

for i, feat in enumerate(iris_data.feature_names):
    for c_idx, cname in enumerate(iris_data.target_names):
        subset = df_iris[df_iris['class_name'] == cname]
        axes[i].scatter(subset[feat], subset['class'], c=[colors(c_idx)], label=cname)
    axes[i].set_title(feat)
    axes[i].set_xlabel("Feature values")
    axes[i].set_ylabel("Class")
    axes[i].legend()

plt.tight_layout()
plt.show()

# j. Randomly split this dataset into two seperate datasets containing 80% and 20% data points, and print their descriptions
train_set, test_set = train_test_split(df_iris, test_size=0.2, random_state=42)
print("Train dataset description:")
print(train_set.describe())
print("Test dataset description:")
print(test_set.describe())