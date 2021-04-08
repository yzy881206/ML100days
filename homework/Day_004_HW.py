#!/usr/bin/env python
# coding: utf-8

# ## 練習時間
# 資料的操作有很多，接下來的馬拉松中我們會介紹常被使用到的操作，參加者不妨先自行想像一下，第一次看到資料，我們一般會想知道什麼訊息？
# 
# #### Ex: 如何知道資料的 row 數以及 column 數、有什麼欄位、多少欄位、如何截取部分的資料等等
# 
# 有了對資料的好奇之後，我們又怎麼通過程式碼來達成我們的目的呢？
# 
# #### 可參考該[基礎教材](https://bookdata.readthedocs.io/en/latest/base/01_pandas.html#DataFrame-%E5%85%A5%E9%97%A8)或自行 google

# # [作業目標]
# - 熟悉更多的 Python 資料操作

# # [作業重點]
# - 列出資料的大小 (In[4], Hint : shape)
# - 列出所有欄位 (In[5], 有多種寫法)
# - 擷取部分資料 (In[6], Hint : loc 或 iloc)

# In[1]:


import os
import numpy as np
import pandas as pd


# In[5]:


# 設定 data_path
dir_data = 'D:/ML100d/courses/EDA_讀取資料與分析流程_HW/'


# In[6]:


f_app = os.path.join(dir_data, 'application_train.csv')
print('Path of read in data: %s' % (f_app))
app_train = pd.read_csv(f_app)


# ### 如果沒有想法，可以先嘗試找出剛剛例子中提到的問題的答案
# #### 資料的 row 數以及 column 數

# In[29]:


print("列數:",app_train.shape[0])
print("行數:",app_train.shape[1])


# #### 列出所有欄位

# In[15]:


app_train.columns


# #### 截取部分資料

# In[38]:


app_train.iloc[4:7,0:5]


# #### 還有各種數之不盡的資料操作，重點還是取決於實務中遇到的狀況和你想問的問題，在馬拉松中我們也會陸續提到更多例子

# In[ ]:




