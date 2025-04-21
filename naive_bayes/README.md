# 🧠 Naive Bayes

### 📌 What is Naive Bayes?

Imagine you’re a burger detective. You’ve eaten hundreds of burgers 🍔 and can guess what kind of burger it is (Spicy, Sweet, Cheesy) just by knowing what’s in it—like sauce, toppings, etc.

Naive Bayes helps you guess the label (like burger type) based on ingredients (features). It uses math + probabilities to make the best guess.


------------

### 📚 Used for:

- 📂 Classification

- 🧠 Spam detection

- 🤖 Sentiment analysis

- 🩺 Disease prediction

- 📊 Document categorization


------------

### 🧮 Formula (in plain English)
***Bayes’ Theorem:***
P(Class∣Data)=P(Data∣Class) * P(Class)P(Data)/P(Data)
*** But we ignore P(Data)P(Data) (same for all), so we use: ***
Score(Class)=P(Class)*P(Data1|Class)×P(Data2|Class)*…

------------


### 🔑 Naive Bayes Variables Cheat Sheet

| **Symbol / Term**          | **Meaning**                                                             |
|----------------------------|--------------------------------------------------------------------------|
| P(Class I Data)         | Probability the class is true, given the observed data (posterior)       |
| P(Data I Class)          | Probability of the data, assuming the class is true (likelihood)         |
| P(Class)                 | Prior probability of the class (how likely it is before seeing data)     |
| P(Data)                  | Probability of the data itself (evidence — often ignored in comparison)  |


------------

### 🎯 Visual Intuition (Emoji style)

Let’s say you see this:

🍔 → [🔥, 🧀, 🌶️]
You're trying to decide if it’s:

-     Spicy 🔥

-     Cheesy 🧀

-     Sweet 🍯

Naive Bayes counts how often each ingredient shows up for each class and uses that to guess the most likely class.


------------

### ⚙️ ASCII Logic Breakdown
```sql
+---------------------------+
|     Ingredient Count      |
+---------------------------+
| Class: Spicy              |
|  - 🔥: 30                 |
|  - 🧀: 5                  |
+---------------------------+
| Class: Cheesy             |
|  - 🔥: 3                  |
|  - 🧀: 40                 |
+---------------------------+

Now we predict:

Score(Spicy)  = P(Spicy) * P(🔥|Spicy) * P(🧀|Spicy)  
Score(Cheesy) = P(Cheesy) * P(🔥|Cheesy) * P(🧀|Cheesy)

→ Choose the class with the **highest score**
```


------------

#### ✅ Pros

  -   Very fast, even on large data

-     Works well with high-dimensional data

-     Easy to implement

#### ❌ Cons

-     Assumes features are independent (which is not always true)

-     Can perform poorly if features are correlated

### 📊 Metrics You Can Use

    Precision

    Recall

    F1-Score

    Accuracy
