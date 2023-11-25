#!/usr/bin/env python
# coding: utf-8

# # Python Functions and Conditions Assignment

# ## Problem 1

# In[1]:


def is_even():
    x = int(input("enter a number: "))
    if x % 2 == 0:
        return True
    else:
        return False
    


# In[2]:


is_even()


# ## Problem 2

# In[ ]:


def calculate_grade(score):
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
    


# In[5]:


calculate_grade(69)


# ## Problem 3

# In[6]:


def calculate_area():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    area = length * width
    print("area of rectangle is ", area)
    


# In[7]:


calculate_area()


# In[ ]:





# ## Problem 4

# In[8]:


def is_triangle(a, b, c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        return True
    else:
        return False
    


# In[9]:


is_triangle(2, 20, 20)


# In[ ]:





# ## Problem 5

# In[10]:


def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
    


# In[11]:


max_of_three(6,5,5)


# In[ ]:





# ## Bonus

# In[12]:


def reverse_string():
    word = input("enter a word: ")
    reverse_word = word[::-1]
    print(reverse_word)
    
   


# In[ ]:


reverse_string()


# In[ ]:





# In[ ]:





# In[ ]:




