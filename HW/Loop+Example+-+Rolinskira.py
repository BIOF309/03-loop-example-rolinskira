
# coding: utf-8

# In[1]:

#real life example of a loop 
packing = ['kindle ereader', 'headphones', 'toothbrush', 'toothpaste', 'face wash', 'hairbrush', 'sweatshirt', 'tennis shoes', 'boarding pass']


# In[2]:

print("The total number of items on your packing list is:")
len(packing)


# In[3]:

packing[3] 


# In[4]:

for done in packing:
    while len(packing) > 0:
        print("You still have more to pack!")
        print("This is how many items you have left to pack:")
        print(len(packing))
        print("These are the items you have left to pack:")
        print(packing)
        print('............')
        del(packing[0])
    else:
        print("You're all packed and ready to go... have a great trip!")


# In[ ]:




# In[ ]:




# In[ ]:



