#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string

from sklearn.base import TransformerMixin

import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer


# In[2]:


nltk.download('stopwords')
nltk.download('wordnet')


# In[3]:


wordnet_lemmatizer = WordNetLemmatizer()

def clean_text(text: str) -> str:
    #removes upper cases
    text = text.lower()
    
    # removes punctuation
    for char in string.punctuation:
        text = text.replace(char, "")
        
    #lemmatize the words & join back into string text
    text = " ".join([wordnet_lemmatizer.lemmatize(word) for word in word_tokenize(text)])
    return text


class DenseTransformer(TransformerMixin):
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X, y=None, **fit_params):
        return X.todense()
    
    def __str__(self):
        return "DenseTransformer()"
    
    def __repr__(self):
        return self.__str__()


# In[ ]:




