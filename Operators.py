# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:41:57 2021

@author: Paarth
"""
'''
#print("hello world.", end="@" )
#print("hello")
#OPERATORS:-
#BINARY OPERATORS:- 
#Addition Operator=a=5+4 print(a)
#Subtraction Operator=s=5-4 print(s)
#Multiplication Operator=m=5*4 print(m)
#Division Operator=d=5/4 print(d)
#Exponential Operator=e=5**4 print(e)

#Floor Division(also knows as Integer Division) gives quotient only, mod gives remainder only.
#x=15//2
#print(x)
#print(type(x))

#RELATIONAL OPERATOR: <,>,>=,!=,==
#x=10
#y=20
#print(x==y) OUTPUT=False
#x="p,q,r,s"
#y="p,q,r,s"
#print(x<=y) OUTPUT=TRUE

#LOGICAL OPERATOR: and- multiplication , or - addition, not
#Order: not,and,or

#Identity Operator (is and is not)
#Ques:
#x=7*(8/(5//2))
#print(x)
#print(type(x))= OUTPUT=28.0

#Exponential Function is always evaluated from LHS to RHS but when there are more than two Exponential Functions then it evaluates from RHS to LHS 
#Ques:
#x=3**3**2
#print(x)
#print(type(x)) OUTPUT=19683

#Ques:
#x,z=5,10
#y=x+3
#x=x-1
#x=x+z
#print(x,y,z) OUTPUT={14 8 10}   
#Ques:
#x=(14//4)
#y=(14%4)
#z=(14/4)   
#print(x,y,z) OUTPUT:3,2,3.5

#Python Class 29/06/2021
#a=6
#a<5 and a<10
#print(a<5 and a<10) if a=2=True, if a=2=False

#Identity Operator: is(if both variables point to the same memory location)
#a=10
#b=20
#c=10
#print(a==c)
#true because they have same memory location.

#id function: Tells the memory location of a variable.

#print(hex(id(a)))
#print(hex(id(c)))

#print(a is c)
#print(a==b)
#print(a is b)

#conditions when is dosen't work like ==:

#Complex Numbers:
#a=10.2
#b=10.2
#print(a is b)
#print(0.1 + 0.1+0.1 == 0.3)
#d ="Paarth"
#print('a' in d)
#print('A' in d)


#ASCII value of a and A are different.

#Augmented Assigned operator aka shortname Assignmet operators:
#&-and operator
#|-or operator
#~-not operator

#a=10
#b=12
#'''
'''#1010
#1100
#1000
#'''
'''#print(~a&b)

#Q:not(10<20) and (10>30)
#A:False
#Q:(6==3)and(4==4)
#A:False
#Q:(6<9)and(4>2)
#A:True
#Q:x=2,1<x<3
#A:True

#Q Write a statement to 
#Assign value 10 to 5 variables
#a=b=c=d=e=10
#Assing value 11 ,12, 13 to three variables
#a,b,c=11,12,13
#print 3 words:-one.two,three on three different line
#print("one","two","three", sep="\n")

#x=10
#y=30
#print(x,y,x+y,sep='&') OUTPUT:10&30&40

#x,y=20,30
#x,y=y+2,x-2
#print(x,y)  OUTPUT:32 18

#a,b,c=11,22,33
#a,b,c=a+1,b-2,c+3
#print(a,b,c)  OUTPUT:12 20 36

#Find the error:
    
#x=float(input("Age:")) IF user inputs Age = 45

#x=int(input("Age="))  If user enters Age=abc

#str='it's' his book  Coutes error

#str='value"(Coutes error)

#x=y+3 (y is not defined)

#Which out of the following are invalid identified:
#1.8rec,finally,rec_8,word.problem,a1b2 (1st, 2nd and 3rd)
#2.prec%,yes,not,nonlocal,i123 (1st,3rd,4th)
'''