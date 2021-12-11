#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
import urllib.request
from tqdm import tqdm


# In[86]:


# loop over 20 pages on the unsplash website
for i in tqdm(range(1,20)) :
    r = requests.get(f'https://api.unsplash.com/search/photos?query=cigarette&page={i}&per_page=30&client_id=xxxxxxxxxxxx')
    # get the json file wich contains the following keys :
    # 'total', 'total_pages', 'results'
    data = r.json()
    
    # get links of images
    for img in data['results'] :
        file_name = str(img['id']) + '.jpg'
        url = img['urls']['small']
        
        # save the image in target folder
        data = urllib.request.urlretrieve(url, f'images/{file_name}')
        

