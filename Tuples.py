#Tuple:- sequenced and immutable.
'''
t=eval(input("Enter a Tuple:"))
print(type(t))
for i in range (len(t)):
    print(t[i])
'''
'''
t=eval(input("Enter a Tuple:"))
print(type(t))
t1=t[::-1]
print(t1)
'''
'''
=eval(input("Enter a Tuple:"))
print(type(t))
t1=t[::-1]
t2=()
print(t1)
for i in range (len(t)):
    t2=t+t1
print(t2)
'''
'''
#WAP to return the length of the shortest string in th etuple of the string.
t=eval(input("Enter a Tuple:"))
x= t[0]
for i in t:
    if len(i)<len(x) :
        x=i
print("Smallest string in tuple = ",x)
'''
'''
#WAP to count  the number of pairs such that both are even.
t= ((2,5),(4,2),(9,8),(12,8))
c= 0
for i in range (len(t)):
    if t[i][0]% 2 == 0 and t[i][1]% 2 == 0:
        c+= 1
print("The number of even pairs are:",c)
'''
'''
#WAP to unpack a tuple in several variables.
t=eval(input("Enter a Tuple:"))
x,x1,x2=t
print(x+x1+x2)
'''
'''
#WAP to reverse a tuple.
t=eval(input("Enter a Tuple:"))
print(t[::-1])
'''
'''
#WAP to calculate the total number of characters, alphabets, digits and spaces in a string.
x=input("Enter a String : ")
c=d=a = 0
for i in range(len(x)):
    if(x[i].isalpha()):
        a+=1
    elif(x[i].isdigit()):
        d+= 1
    else:
        c+=1
print("Total Number of Alphabets in this String :  ", a)
print("Total Number of Digits in this String :  ", d)
print("Total Number of Characters in this String :  ",c)
'''
'''
#WAP that accepts n numbers in a lsit and counts the even numbers present in the list.
x=eval(input("Enter a list:"))
even=odd=0
for i in x:
    if i% 2== 0:
     even+= 1
    else:
      odd+= 1
print("Even numbers: ",even)
print("Odd numbers:",odd)
'''
'''
#WAP that takes any message as input and prints it without vowels.
x=input("Enter a String:")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
y= ""
for i in range(0,len(x)):
    if x[i] not in vowels:
        y=y+x[i]
print("New String:")
x=y
print(x)
'''
'''
#WAP to print Python in new line each word.
x="python"  
y= ""  
for i in x:  
    y+=i  
    print(y)   
'''
'''
#WAP to find the mean from a list of numbers.(NOT WORKING)
x=eval(input("Enter a list:"))
y=0
for i in x:
    y+=1
mean=y/len(x)
print("The Mean of Numbers is:",mean)
'''
#WAP to count the number of character in a string, to capitaise,check wheather given string is letter or number,change lower case to uppercase and change one character to another.

'''
#WAP that prints 1,2,4,8,16,32,64,128.
x=8
y=1
while(x):
    print(y, end =" ")
    y*=2
    x-=1
'''
'''
#WAP to find the sum of all the elements of a list N.
x=eval(input("Enter a List:"))
y=int(input("Enter Number Upto:" ))
for i in range(y):
    z= int(input("Enter number:"))
    x.append(z)
print("Sum of elements is:", sum(x))
'''
'''
#WAP to compare two strings without using built in functions.
x=input("Enter a String:")
y=input("Enter another String:")
if x==y:
    print("Equal Strings")
else:
    print("Unequal Strings")
''' 
'''
#WAP to move all duplicate values in a list to the end of the list.
l=eval(input("Enter a list :"))
x=[]
y=1
while y<len(l):
      for i in l:
            if l.count(i)!= 1:
                  l.remove(i)
                  x.append(i)
      y+= 1
l.sort()
print("New list : ",l+x)
'''
'''
#WAP that rotates the elements of a list so that the element at the first index moves to the second index, the element in the second index moves to the third index etc and the element in the last index moves to the first index.
l=eval(input("Enter a list:"))
print("Old List")
print(l)
l=l[-1:]+l[:-1]
print("New List")
print(l)
'''
'''
#WAP to merge two sorted list and return a sorted list.
a=eval(input("Enter a List:"))
b=eval(input("Enter a List:"))
for i in range(1,a):
    a=a.sort()
for i in range(1,b):
    b=b.sort()  
new=a+b
new.sort()
print("Sorted list is:",new)
'''
'''
#WAP to delete all the odd no.s and negatuve no.s from a list.
x=eval(input("Enter a list:"))
x.sort()
for i in x:
    if i%2!=0:
        y=x.remove(i)      
    for i in range(x.index(i)+1),x.index(i):
        del x[i] 
print(x)
'''
'''
#WAP that takes a string with multiple words and then capitalise the first letter of each word and forms a new string out of it.
x=input("Enter a string:")
y=x.split()
for i in y:
    z=i.capitalize()
    print(z,end="")
'''
'''
#WAP to sort a list using insertion sort.
l=[1,9,2,8,3,7,4,6,5]
for i in range(1,len(l)):
    temp=l[i]
    pos=i 
    while pos>0 and l[pos-1]>temp:
        l[pos]=l[pos-1]
        pos=pos-1
    l[pos]=temp
print(l)
'''
'''
x=eval(input("Enter a Tuple:"))
print(x[-1])
'''
'''
x=eval(input("Enter a Tuple:"))
print(x[3])
print(x[-4])
'''
'''
x=eval(input("Enter Tuple 1:"))
y=eval(input("Enter Tuple 2:"))
print(x==y)
'''
'''
x=eval(input("Enter a List:"))
print(x)
y=tuple(x)
print(y)
'''
'''
x=eval(input("Enter a Tuple:"))
print(x)
s=x[2:6]
print(s)
'''
'''
#WAP to unpack a tuple in several variable.
x=eval(input("Enter a Tuple:"))
print(x)
n1,n2,n3=x
print(n1+n2+n3)
n1,n2,n3,n4=x
'''
'''
#WAP to reverse a Tuple.
x=eval(input("Enter a Tuple:"))
x=x[::-1]
print(x)
'''
'''
#WAP that interactively creates a nested tuple to store the marks in 3 subjects of 5 students.
t1=eval(input("Enter marks of student 1:"))
t2=eval(input("Enter marks of student 2:"))
t3=eval(input("Enter marks of student 3:"))
t4=eval(input("Enter marks of student 4:"))
t5=eval(input("Enter marks of student 5:"))
t=t1+t2+t3+t4+t5
print(t)
'''
'''
#WAP to return the length of the shortest string in a Tuple.
t=eval(input("Enter the string Tuple: "))
s=t[0]
for i in t:
    if len(i)<len(s) :
        s=i
print("Smallest string in Tuple:",s)
'''
#Give the output of the following:
'''print("Ranjan said,"It'a lovely day"')'''
'''
print("ram said,\"I AM LEARNING PYTHON")
print("A goal\n without a plan is just a\t wish")
'''
'''
#Write a program to compute the area and circumference of a circle using a function.
r=float(input("Enter the radius:"))
def areaperi(r):
    x=3.14*r*r
    y=2*3.14*r
    return(x,y)
x,y=areaperi(r)
print("Area of Circle: ",x)
print("Perimeter of Circle:",y)
'''
'''
#Write a program to input n numbers from the user. Store these numbers in a tuple. Print the maximum and minimum number from this tuple.
t=tuple()
n=int(input("Enter total Number of Tuples:"))
def tupl(n):
    for i in range(n):
        a=input("Enter Elements:")
        t=t+(a,)
a=tupl(n)
print("maximum value:",max(t))
print("minimum value:",min(t))
'''



