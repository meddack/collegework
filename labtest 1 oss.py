#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
aqi_reading=np.array(np.random.normal(1,1,1440))
print(aqi_reading)


# In[15]:


noise=np.array(np.random.rand(5,5,1440))
print(noise)


# In[18]:


new= aqi_reading+noise
print(new)


# In[23]:


import scipy.signal 

smooth data = scipy.signal(new)


# In[33]:


k=0
i=0

def avg_aqi(k,new):
    
    for i in new:
        k=new[i]+k
            


print(avg_aqi(k,new))
            
    


# In[48]:


import matplotlib.pyplot as plt

plt.bar(noise,new)

plt.xlabel("x axis")
plt.ylabel("y-axis")
plt.show()


# In[ ]:





# In[ ]:




