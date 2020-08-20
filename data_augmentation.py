#!/usr/bin/env python
# coding: utf-8

# In[110]:


get_ipython().system('pip install googletrans')
import numpy as np
import pandas as pd
from googletrans import Translator


# In[51]:


train = pd.read_csv('./input/train.csv')
test = pd.read_csv('./input/test.csv')


# 

# In[131]:


def is_eng(word):#日本語を除外
    kana_set = {chr(i) for i in range(12353, 12436)}#平仮名があれば日本語
    word_set = set(word)
    if kana_set - word_set == kana_set:
        return True
    else:
        return False


# In[54]:


translator = Translator()


# In[ ]:


train_np = train.to_numpy()

add_data = []
count=0
for i in range(train_np.shape[0]):
  trans_1 = translator.translate(train_np[i][1],src="en",dest='ja')#from eng to jp
  trans_2 = translator.translate(trans_1.text,src="ja",dest='en')#from jp to eng
  if is_eng(trans_2.text)==True:#if the text is eng
    add_data=np.append(add_data,[count+train_np.shape[0],trans_2.text,train_np[i][2]])
    count=count+1
  if i%100==0:  
    print(i)  
add_data=add_data.reshape(-1,3)  

add_data


# In[ ]:


add_df = pd.DataFrame(data=add_data, columns=['id', 'description', 'jobflag'])
add_df


# In[138]:


new_train =  pd.concat([train,add_df],ignore_index=True)
new_train


# In[139]:


new_train.to_csv("/content/drive/My Drive/Colab Notebooks/content/input/new_train_1.csv")

