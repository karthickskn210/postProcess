#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
df = pd.read_csv('dataSet.csv')
df.head()


# In[34]:


df = df.drop(['Unkown','USER_NAME','SQL_TEXT_TYPE','DATABASE_NAME','SESSION_ID','PLAN_ID','TOTAL_SECONDS','SNIPPETS','THROUGH_PUT_ROWS','THROUGH_PUT_SIZE','newline'],axis=1)
df.head()


# In[169]:


class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value
        
    def checkKey(self, key): 
      
        if key in self.keys(): 
            return True 
        else: 
            return False
        
    # Increment value
    def increment(self,key):
        
        if key in self.keys():
            
            self[key] += 1
    


# In[173]:


"""
dic = dict()
key = 'Cluster1'
dict1.setdefault(key,{})
"""
Dict = my_dictionary()

for i in range(5,6):
    print(i)
    values = []
    rep_list = []
    nrep_list = []
    for data in df.index:
        if df.loc[data,'Clusters']==i:
            
            Ext = df['SQL_TEXT_HASH'][data]
            values.append(Ext)
    #print('all')
    #print(values)
    
    for j in range(len(values)): 
        if values[j] not in values[j + 1:]: 
            rep_list.append(values[j])
                        
    for k in range(len(values)): 
        if values[k] in values[k + 1:]: 
            nrep_list.append(values[k])
    #print('non rep')
    #print(rep_list)
    #print('rep')
    #print(nrep_list)
    
    for j in range(len(rep_list)):
        key = str(rep_list[j])
        value = 1
        Dict.add(key,value)
    #print(Dict)
    
    for k in range(len(nrep_list)):
        key = str(nrep_list[k])
        present = Dict.checkKey(key)
        #print(present)
        if present == True:
            #print(key)
            Dict.increment(key) #increment(self,key
    print(Dict)
    #values.update({key : 1})
    #values = l(values)
            


# In[ ]:




