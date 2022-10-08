#!/usr/bin/env python
# coding: utf-8

# In[27]:


import json
import requests


# In[28]:


url = "https://api.github.com/repos/MNYudina/Seminars/stargazers"
response = requests.get(url)


# In[29]:


print(json.dumps(response.json()[0], indent=1))
print()


# In[30]:


for (k,v) in response.headers.items():
 print(k, "=>", v)


# In[ ]:




