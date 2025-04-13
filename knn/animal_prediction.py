#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


# In[2]:


df = pd.read_csv("../datasets/animals.csv")


# In[3]:


X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values


# In[4]:


print(X)


# In[5]:


print(y)


# In[6]:


le = LabelEncoder()
y = le.fit_transform(y)


# In[7]:


print(y)


# In[16]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.01, random_state=1)


# In[18]:


print(X_train)


# In[19]:


print(X_test)


# In[20]:


print(y_train)


# In[21]:


print(y_test)


# In[25]:


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)


# In[26]:


prediction = knn.predict(X_test)


# In[27]:


print(prediction)


# In[ ]:




