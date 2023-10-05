#!/usr/bin/env python
# coding: utf-8

# # Algorithm workbench 

# # number 4 

# In[1]:


# question 4 code shows an If-Else statement that is incorrect with inproper aligment we must fix the function 
if score >= A_score: 
print('Your grade is A.') 
else: 
if score >= B_score: 
print('Your grade is B.') 
else: 
if score >= C_score: 
print('Your grade is C.') 
else: 
if score >= D_score: 
print('Your grade is D.') 
else: 
print('Your grade is F.') 


# In[2]:


# for this If-esle statement I am going to give proper aligment to see if the code works 
 if score >= A_score: 
print('Your grade is A.') 
else: 

    if score >= B_score: 
print('Your grade is B.') 
    else: 

         if score >= C_score: 
print('Your grade is C.') 
         else: 

              if score >= D_score: 
print('Your grade is D.') 
              else: 

                   print('Your grade is F.')
# error said indent was incorrect am going to keep trying diffrent indents till the fuction is successfull 


# In[3]:


if score >= A_score:
print('Your grade is A.') 
else: 

    if score >= B_score: 
print('Your grade is B.') 
else: 

    if score >= C_score: 
print('Your grade is C.') 
else: 

    if score >= D_score: 
print('Your grade is D.') 
else: 

    print('Your grade is F.') 
    # pressing enter to indent code is unsucessful, 
    # going to try spacing without space inbetween each line 


# In[4]:


if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
# aligment and indentation are successful   
# need to lable scores 


# In[7]:


# area to define score 
A_score = 90
B_score = 80
C_score = 70 
D_score = 60

if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')


# In[9]:


#added a score for equation to work 
score = 85

# area to define score 
A_score = 90
B_score = 80
C_score = 70 
D_score = 60

# If, else clase 
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')


# ### lots of trail and error but finally got the equation to work 
# ### forgot to added a score and identify function for the if, else clause to work. 
# ### got fixated on the code proved and forgot that i needed to added assements to the scores to test the code

# In[ ]:




