#using upper function:-
#Say that we want to have this astronaut's name in all caps to print on their space suit. Instead of having to make a new variable, 
#we can use the .upper() function to print the name in capital letters. 
#To call a function, type the variable followed by a period, the name of the function, and then parenthesis.
#Calling this upper function won't change the astronaut variable, since we want to preserve their name with the correct capitalization. 
#You must set a new variable or current variable equal to the function that you'have called.
#Example:-

astronaut = "Stanley G Love"
upperCase = astronaut.upper()
print(upperCase)

#vice-versa in lower function:- it brings all the alphabets in lowercase.

#LIST FUNCTION:-
#Lists are ways to store a lot of data in Python and are similar to variables.
#  They are a collection of values stored in the form of a list.
#  Lists are useful in Python because often you'll need more than one piece of data.
#Lists play a huge role in data science, because the goal of data science is to take large amounts of related data and analyze it. 
# That's why the popular data science Python packages, such as Pandas and NumPy, have additional data structures like dataframes and arrays, 
# which are essentially lists with additional features.
#How to make a list:-
#Defining lists in Python is similar to creating variables. However, lists can hold multiple values. 
#Start by making a name for your list and then set it equal to a value. For example:

#List Functions
#There are many pre-made functions included in Python, which we can use to modify a list.
#For example, we can add items to a list by calling the.append() function followed by the data that we want to add in parentheses. 
#we can add items to a list by calling the.append() function:-  rockTypes.append("soil")
#                                                               rockTypes
#Doing this adds an item to the end of a list. Let's add a rock type to our original list.
#We can also delete items from the end of a list by calling the .pop() function. 
#We'll now delete"soil"from the rock types list:- rockTypes.pop()
#                                                 rockTypes

#Finally, we can look at and change the value from anywhere within the list. To see what a value is at a certain point in the list, 
# use square brackets after the list name to look at that specific value. Everything in Python is zero-indexed, 
# meaning that counting begins at 0, not 1. So if we look at the value in the first position in a list, we would use: listName[0].
#In our rock type example, use the following code to look at the value in the second position in the list:-(rockTypes[1])
