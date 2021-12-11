#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import shutil


# In[29]:


# take 20% of images for validation purposes
txt_len = len([name for name in os.listdir('./labels')])
prg = int(txt_len * 0.2)

# separate the data 
df_val = os.listdir('./labels')[:prg]
df_train = os.listdir('./labels')[prg:]


# In[30]:


# turn the data into the appropriate formate in the train and validation folders for both images and labels
def prepare_data(data, data_type='train'):
 
    for fich in data:
        name = fich.split('.')[0]
        try :
        
            shutil.copyfile(
                f"labels/{name}.txt",
                f"labels/{data_type}/{name}.txt"
            )

            shutil.copyfile(
                f"images/{name}.jpg",
                f"images/{data_type}/{name}.jpg"
            )
        except :
            continue


prepare_data(df_train, data_type='train')
prepare_data(df_val, data_type='validation')

