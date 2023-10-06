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

# # Number 5

# ### this code is asking use to create a nest desicsion of structures 

# In[11]:


# variables to test the code 
amount1 = 20
amount2 = 90 

# program for a nest decision structure 
#adding if statements 
if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print(amount1, "is greater than", amount2)
            else: amount1 < amount2:
                print(amount1, "is less than", amount2)
                else:
                    if amount1 > 10 
                    print("amount1 is not greater than 10")
                    else:
                    print ("amount2 is less than 100")
                        #adding if else statements 
                
                
                
                
                
        
 
            


# In[12]:


# for the function im going to fix invalid syntax 
# Variables to test the code
amount1 = 20
amount2 = 90

# Program for a nested decision structure
# Adding if statements
if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print(amount1, "is greater than", amount2)
        else:  # Removed "else" and added ":" to start an "if" block
            print(amount1, "is less than", amount2)
    else:  
        print("amount2 is not less than 100")
else:  
    print("amount1 is not greater than 10")
# added correct syntax to line 11 and spaced properly 


# In[13]:


# for the function im going to fix invalid syntax 
# Variables to test the code
amount1 = 500
amount2 = 1000

# Program for a nested decision structure
# Adding if statements
if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print(amount1, "is greater than", amount2)
        else:  # Removed "else" and added ":" to start an "if" block
            print(amount1, "is less than", amount2)
    else:  
        print("amount2 is not less than 100")
else:  
    print("amount1 is not greater than 10")
# added correct syntax to line 11 and spaced properly 


# # program exercise
# ### question 1 

# In[14]:


# they would like use to make a code ranging 1 to 7 and each number displaying a week
# anything other than 1 to 7 should show up as an error message 
# Get input
person_input = input("Enter a number 1 through 7: ")

# Checking the input if the is valid
if person_input():
    # Convert the input to an integer
    number = int(person_input)
# this step is displaying if the number is within the range the program should show the coraspoding answer 

    # Check if the number is within the valid range # greater than or equal to because it is in the range  
    if 1 <= number <= 7:
        # enter an if-elif-else statement for numbers = weeks # == for numbers, = for assignment
        if number == 1:
            day = "Monday"
        elif number == 2:
            day = "Tuesday"
        elif number == 3:
            day = "Wednesday"
        elif number == 4:
            day = "Thursday"
        elif number == 5:
            day = "Friday"
        elif number == 6:
            day = "Saturday"
        else:
            day = "Sunday"
        
        # Display question for the function to activate 
        print(f"The corresponding day of the week is {day}")
    else:
        print("Error: The number is outside the range of 1 through 7.")


# In[15]:


# they would like use to make a code ranging 1 to 7 and each number displaying a week
# anything other than 1 to 7 should show up as an error message 
# Get input
person_input = input("Enter a number 1 through 7: ")

# Checking the input if the is valid
if person_input():
    # Convert the input to an integer
    number = int(person_input)
# this step is displaying if the number is within the range the program should show the coraspoding answer 

    # Check if the number is within the valid range # greater than or equal to because it is in the range  
    if 1 <= number <= 7:
        # enter an if-elif-else statement for numbers = weeks # == for numbers, = for assignment
        if number == 1:
            day = "Monday"
        elif number == 2:
            day = "Tuesday"
        elif number == 3:
            day = "Wednesday"
        elif number == 4:
            day = "Thursday"
        elif number == 5:
            day = "Friday"
        elif number == 6:
            day = "Saturday"
        else:
            day = "Sunday"
        
        # Display question for the function to activate 
        print(f"The corresponding day of the week is {day}")
    else:
        print("Error: The number is outside the range of 1 through 7.")


# ## line 7 im going to add the float function to see if that solves the problem 

# In[ ]:


# they would like use to make a code ranging 1 to 7 and each number displaying a week
# anything other than 1 to 7 should show up as an error message 
# Get input
person_input = input("Enter a number 1 through 7: ")

# Checking the input if the is valid
if person_input():
    # Convert the input to an integer
    number = float(person_input)
# this step is displaying if the number is within the range the program should show the coraspoding answer 

    # Check if the number is within the valid range # greater than or equal to because it is in the range  
    if 1 <= number <= 7:
        # enter an if-elif-else statement for numbers = weeks # == for numbers, = for assignment
        if number == 1:
            day = "Monday"
        elif number == 2:
            day = "Tuesday"
        elif number == 3:
            day = "Wednesday"
        elif number == 4:
            day = "Thursday"
        elif number == 5:
            day = "Friday"
        elif number == 6:
            day = "Saturday"
        else:
            day = "Sunday"
        
        # Display question for the function to activate 
        print(f"The corresponding day of the week is {day}")
    else:
        print("Error: The number is outside the range of 1 through 7.")


# # Question 5 

# In[17]:


# we need to write a program that ask for a mass in Kg then calculates its weight in newtons.  
# If the object weighs more than 500 newtons, display a message indicating that it is too heavy. 
# If the object weighs less than 100 newtons, display a message indicating that it is too light.
# Get the mass of the object from the user
# enter float for math equation and entered input for display for the question 
mass_kg = float(input("Enter the object's mass in kilograms: "))

# this is the equation given to calculate the weight in newtons
weight_newtons = mass_kg * 9.8  # Assuming standard gravity on Earth is 9.8 m/s^2

# this is to check if the object is too heavy or light
if weight_newtons > 500:
    print("The object is too heavy.")
elif weight_newtons < 100:
    print("The object is too light.")
else:
    print(f"The weight of the object is {weight_newtons} newtons.")
    # my perdiction is that the program will ask me to enter mass in Kg then display the weight in newtons 
    # it should also display if the object is to heavy or light in weight 


# In[18]:


# we need to write a program that ask for a mass in Kg then calculates its weight in newtons.  
# If the object weighs more than 500 newtons, display a message indicating that it is too heavy. 
# If the object weighs less than 100 newtons, display a message indicating that it is too light.
# Get the mass of the object from the user
# enter float for math equation and entered input for display for the question 
mass_kg = float(input("Enter the object's mass in kilograms: "))

# this is the equation given to calculate the weight in newtons
weight_newtons = mass_kg * 9.8  # Assuming standard gravity on Earth is 9.8 m/s^2

# this is to check if the object is too heavy or light
if weight_newtons > 500:
    print("The object is too heavy.")
elif weight_newtons < 100:
    print("The object is too light.")
else:
    print(f"The weight of the object is {weight_newtons} newtons.")
    # my perdiction is that the program will ask me to enter mass in Kg then display the weight in newtons 
    # it should also display if the object is to heavy or light in weight 


# #### test was succseful and function ran correctly it display it being to heavy and light 

# In[ ]:




