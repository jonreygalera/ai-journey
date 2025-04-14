# 📚 Naive Bayes Mastery

## 🤖 What is Naive Bayes?
- A classification algorithm based on Bayes’ Theorem from probability.
- It’s "naive" because it assumes all features are independent of each other (even though that’s rarely true).
- Still works great in real life: fast, easy, and powerful!

<hr/>

## 🧠 What it’s used for:
- Classification
- Spam detection (email filters)
- Sentiment analysis (happy/sad text)
- Medical diagnosis (flu or not?)
- Predicting user preferences (like what burger you want 🍔)

</hr>

## 🧮 The Formula

**In Naive Bayes format::**

```mathematica
P(Class | Features) = [P(Feature1 | Class) * P(Feature2 | Class) * ... * P(Class)]
```

**Breakdown of the Formula Variables:**

- **P(Class | Features):**  
  The **posterior probability** — the probability of a class (label) given the observed features (data).
  
- **P(Feature1 | Class):**  
  The **likelihood** — the probability of observing Feature1 given a certain class.
  
- **P(Class):**  
  The **prior probability** — the likelihood of the class before knowing any features.
  
- **P(Features):**  
  The **evidence** — the total probability of all features combined.

**Important note in Naive Bayes:**  
We ignore the denominator (**P(Features)**) because it’s the same for every class. We focus on comparing the **numerators** only.

</hr>

## Intuitive Example: The Burger Master

<p>
Let's use a burger example to understand Naive Bayes.
Imagine you’re at a burger joint 🍔. Customers come in with different toppings, and you need to guess which type of burger they want.
</p>

You have three types:

- Veggie Burger 🥦
- Cheese Lover 🧀
- Meat Lover 🥩

**Toppings and Class Labels**

| Tomato 🍅 | Cheese 🧀 | Bacon 🥓 | Lettuce 🥬 | Burger Type  |
|-----------|-----------|----------|------------|--------------|
| 1         | 1         | 0        | 1          | Veggie       |
| 0         | 1         | 1        | 0          | Meat Lover   |
| 1         | 1         | 0        | 1          | Cheese Lover |
| 0         | 0         | 1        | 0          | Meat Lover   |
| 1         | 0         | 0        | 1          | Veggie       |
| ...       | ...       | ...      | ...        | ...          |

**Features:**

- **Tomato (🍅):** 1 = Yes, 0 = No
- **Cheese (🧀):** 1 = Yes, 0 = No
- **Bacon (🥓):** 1 = Yes, 0 = No
- **Lettuce (🥬):** 1 = Yes, 0 = No

**Goal:**
You want to predict the **Burger Type** based on these toppings (features).

### Naive Bayes in Action

**Formula for Veggie Burger:**

```rst
P(Veggie | Tomato, Cheese, Bacon, Lettuce) = P(Tomato | Veggie) * P(Cheese | Veggie) * P(Bacon | Veggie) * P(Lettuce | Veggie) * P(Veggie)
```

**Formula for Meat Lover Burger:**
```rst
P(Meat Lover | Tomato, Cheese, Bacon, Lettuce) = P(Tomato | Meat Lover) * P(Cheese | Meat Lover) * P(Bacon | Meat Lover) * P(Lettuce | Meat Lover) * P(Meat Lover)
```

**Formula for Cheese Lover Burger:**
```rst
P(Cheese Lover | Tomato, Cheese, Bacon, Lettuce) = P(Tomato | Cheese Lover) * P(Cheese | Cheese Lover) * P(Bacon | Cheese Lover) * P(Lettuce | Cheese Lover) * P(Cheese Lover)
```