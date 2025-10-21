# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 12:21:29 2021

@author: Paarth
"""


'''#write a program to test the divisibility of a number by another number
num1=int(input("Enter Number 1:"))
num2=int(input("enter Number 2:"))

if num1%num2==0:
    print(num1,"is divisible by", num2)
else :
     print(num1,"is not divisible by", num2) 
 '''
'''    
radius=float(input("Enter radius of circle:"))
choice=int(input("Enter your Choice(1 or 2):"))
if choice==1:
    area=3.14*radius*radius
    print("Area of Circle",area)

else:
    Perimeter=2*3.14*radius
    print("Perimeter",Perimeter)
    '''
'''
Number=int(input("Enter a 6 digit Number:"))
if Number>99999:
    a1=Number%100
    aa1=Number//100    
    a2=aa1%100
    aa2=aa1//100
    a3=aa2%100
print("2 Three digit Numbers are:",a1,a2,a3)
'''
'''
max=int(input("please enter the maximum value: "))
even=0
odd=0
for num in range(1,max+1):
    if (num%2==0):
        even=even+num
    else:
        odd=odd+num
print("The sum of Even numbers 1 to {0} = {1}".format(num,even))
print("The sum of odd numbers 1 to {0} = {1}".format(num,odd))
'''
'''
i=1
while i<6:
    print(i)
    i=i+1
'''

'''
a=int(input("Enter a number:"))
while a<11:
    print(a)
    a=a+1
'''

'''
x=int(input("Enter a number:"))
n=int(input("Enter the power:"))
i=1
while i <= x:
    print(i**n)
    i=i+1
'''
'''
#Write a program to sum of even numbers upto n entered by the user
x=int(input("Enter an Number:"))
sum=0
i=1
while i<=x:
    if i%2==0:
        sum=sum+i
    i=i+1
print("Total Sum:",sum)
'''
#program to calculate and print the sums of even and odd integers of the first n natural numbers
'''
n=int(input("Enter a Natural Number:"))
i=1
sum1=sum2=0
while i<=n:
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
    i+=1
    print("Sum of Even Numbers is:",sum1)
    print("Sum of Odd Numbers is:",sum2)
'''    
'''
n=int(input("please enter the value of n: "))
sum1=sum2=0
i=1
for num in range(1,n+1):
    if (i%2==0):
        sum1+=i
    else:
        sum2+=i
print("The sum of Even numbers:"(i,sum1))
print("The sum of odd numbers:",(i,sum2))
'''
'''
n=int(input("enter a Number:"))
fact=1 
a=1
while a<=n:
    fact *=a
    a+-1
    print("Factorial of",n,"is",fact)
'''