# 📍K-Nearest Neighbors (KNN)

## ✅ What is KNN used for?
- Classification
- Regression

<hr/>

## 📐 Formula (Simple Version)
> KNN doesn’t have a training formula, but this is the key idea:

```python
distance = √(x1​−x2​)^2 + (y1​−y2​)^2
```
Then:
- Find the **K** closest data points
- Pick the most common label among them

<hr/>

## 🧠 Visual Intuition (Emoji Style)
<p>Imagine you're a 🍕 food critic in a food court.
You see a new dish 😋 and want to guess what it is…
You look around 🧐 and find the K most similar dishes nearby (based on ingredients).
</p>
<p>Example</p>

```text
You = ❓
Nearby dishes:
🥓 (Bacon Burger)
🍗 (Chicken Sandwich)
🍗
🥓
🍔

Most common = 🍗 → So you guess it's Chicken Sandwich
```
<hr/>

## 🧠 ASCII Logic
```text
Step 1: Measure distance from unknown point to all other points
Step 2: Sort distances (smallest to largest)
Step 3: Pick top K neighbors
Step 4: Count labels of those K neighbors
Step 5: Most common label = prediction
```
<hr/>

## 💡 Key Insights

- 📏 Distance matters (Euclidean is most common)
- 🎯 K = 1 is sensitive (overfits), K = too large = underfits
- 🧠 No “learning” step — lazy algorithm
- 🧼 Normalize features or it gets confused (height in cm vs weight in kg)

## 🧠 KNN MASTER CHEATSHEET (Keep this forever)
| Concept               | Meaning                                                            |
|-----------------------|--------------------------------------------------------------------|
| K                     | Number of neighbors to consider                                     |
| Distance formula      | Euclidean: √((x1 - x2)² + (y1 - y2)²)                             |
| Prediction            | Majority vote of K neighbors                                       |
| Classification use    | Yes ✅                                                              |
| Regression use        | Yes (average of K values) 🧮                                        |
| Normalize features    | Important! Prevent bias if features have different scales 📏        |
| Sensitive to noise    | Yes (K=1 is especially noisy)                                       |
| Training time         | Fast (no training really) ⚡                                        |
| Prediction time       | Slow for large datasets (compares to all) 🐌                        |

## K=5 vs K=3
- **K=5**: Considers 5 nearest neighbors to make a prediction.
- **K=3**: Considers only the 3 closest neighbors to make a prediction.

**Effect on prediction:**
- For smaller K, the model is more sensitive to individual data points.
- If there’s a small group of neighbors with a strong, different label, it can sway the prediction.

**Result of K=3:**
- It may overfit to a few close points.
- It might be more erratic in predicting than K=5, but it’s more specific.

📊 **Key Insights:**
- **K=3** is more sensitive, so predictions may change a lot if there are small variations in the data.
- **K=5** makes the model more "calm" and generally more stable because it averages out over 5 neighbors.
- Lower **K** means more specific but possibly noisier predictions.