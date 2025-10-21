# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 11:21:21 2021

@author: Paarth
"""

'''
num=10
for a in range(1,11):
    print(num,'*',a,'=',num*a)
'''
'''
n=int(input("Enter a Number:"))
i=0
sum1=sum2=0
for a in range(0,n-1):
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
    i=i+1
print("Sum Even:",sum1)
print("Sum Odd:",sum2)

n=int(input("Enter a Number:"))
i=0
sum1=sum2=0
while i<= n:
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
    i=i+1
print("Sum Even:",sum1)
print("Sum Odd:",sum2)
'''
'''
num=int(input("Enter a Number:"))
i=1
a=1
while a<= num:
    i=i*a
    a=a+1
print("The factorial of",num,"is",i)
'''
'''n = int(input("Enter the number:"))
a= 0
b= 1
print(a)
print(b)
for x in range(0, n-1):
    x = a + b
    a = b
    b = x
    print(x)
'''
'''
1 2 3
4 5 6 
7 8 9

*
**
***
****
'''
#Write a program to input some  numbers repeteadly and find their sum, the prog ends when user says"No",or programm aborts when n entered<

'''
x=i=0
n=int(input("Enter a Number:"))
if n<=0:
    print("Programm Aborted")
    break
x=x+n
i=i+1
a=input("Enter more Numbers? (Yes or No):")
print(a)
if a=="No" or a="n"
break  
else:
    print("Number Entered",i)
print("Sum of Numbers Entered:",x)
'''
'''
i=1
while i<10:
    if i%3==0:
        print(i)
    i+=1
'''
'''
Num=50 
while Num >= 10: 
    if Num==30: # error in this line
            break    3error in this line (BREAK)
elif Num>30:     #error in this line(Elif was written)
print(Num) #indentation error
else:      #indentation error
print(Num //10)
'''   
#Pattern Printing:-
'''
for i in range(1,5):
    for j in range(0,i):
        print("*",end="")
    print()
#Output
#*
#**
#***
#****   
'''
'''0
22
444
8888
'''
'''n=int(input("Enter a Number:"))
for i in range(0,n-1):
    for j in range(0,n+1):
        print(i**n-1,end="")
    print()
'''



    