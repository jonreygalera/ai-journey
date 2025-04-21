# 🤖 KNN Mastery (K-Nearest Neighbors)

### 📌 What is KNN?

A simple but powerful supervised machine learning algorithm that can be used for:

- ✅ Classification (e.g., Is this a cat or dog?)
- ✅ Regression (e.g., Predicting house price)

It predicts the label of a new data point by looking at the 'k' nearest data points in the training set and voting for the majority label.

------------


### 🧠 How KNN Thinks (Visual + Intuitive)
Imagine you're in a school cafeteria 🍔🥤 and you just transferred.

You don’t know anyone…
So to decide who you might be similar to, you look at the 3️⃣ people (K=3) closest to you.
They’re all talking about anime, so you think:
👉 "I must be an anime fan too!"

That’s how KNN works.

------------

### 📐 Formula (KNN has no training formula — it's lazy!)

But for distance, it uses this:
🧮 Euclidean Distance (most common):
```cpp
🧮 Euclidean Distance (most common):
D = √((x1 - x2)² + (y1 - y2)² + ... + (n1 - n2)²)
```
It just measures how close data points are.

------------

### ⚙️ How KNN Works Step-by-Step:

1. Save all the training data (no learning yet). 
2. When asked to make a prediction:
   - Measure distance between the test point and all training points.
   - Pick the K closest points (neighbors).
   - For classification: vote 🗳️
   - For regression: average 🧮


------------

### 🔍 Visual Intuition (Emoji Style)

```
📦 ← test point (what we want to predict)
🐱 🐶 🐱 🐶 🐱 ← labeled neighbors

If K=3:
→ Check 3 closest neighbors
→ Majority vote: 🐱🐱🐶 → 🐱 wins → prediction = 🐱

```


------------
### 🧪 Sample Dataset (CSV-Ready)
| Height | Weight | Type    |
|--------|--------|---------|
| 160    | 55     | Burger  |
| 170    | 70     | Pizza   |
| 180    | 85     | Pizza   |
| 150    | 45     | Burger  |
| 165    | 65     | Pizza   |
| 155    | 50     | Burger  |
| 175    | 80     | Pizza   |
| 158    | 52     | Burger  |
| 172    | 77     | Pizza   |
| 153    | 49     | Burger  |


------------

### 🧑‍💻 Simple KNN Python Code (Pandas + Scikit-learn)

```python
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

# Load Data
df = pd.read_csv("food_data.csv")  # replace with your CSV path

# Separate Features and Label
X = df[["Height", "Weight"]].values
y = df["Type"].values

# Encode Labels
le = LabelEncoder()
y = le.fit_transform(y)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predictions
predictions = knn.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions, target_names=le.classes_))

```

### 🧠 KNN Cheat Sheet

# 🧠 KNN Cheat Sheet

| **Concept**        | **Meaning**                                                            |
|--------------------|------------------------------------------------------------------------|
| `Lazy Learner`     | No training; only memorizes data                                        |
| `Distance Metric`  | Mostly Euclidean, can be Manhattan or others                           |
| `K Value`          | Number of neighbors to vote or average                                  |
| `Too Small K`      | Overfits (memorizes too much)                                           |
| `Too Big K`        | Underfits (too general)                                                |
| `Feature Scaling`  | Important, otherwise features like weight dominate                      |
| `Time Complexity`  | Slow on large data (O(n)) per prediction                               |


------------

#### ✅ Strengths (Pros)

-     Simple and intuitive

-     No training needed

-     Works well with small datasets

#### ❌ Weaknesses (Cons)

-     Slow with large datasets

-     Needs scaling (sensitive to feature range)

-     Bad with irrelevant features


------------

