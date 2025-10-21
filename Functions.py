'''
#FUNCTIONS:-
1)Built-in 
2)User Defined
3)Module Defined
4)Variable Length
'''
#Arguments:
#1>Positionl
#2>Keyword
'''
def sum(a,b):
   print(a+b)
sum(10,20)
'''
'''
def sum(a,b=5):
   print("a=",a)
   print("b=",b)
sum(10,20)
sum(20)
'''
'''
def sum(a,b=5):
   print("a=",a)
   print("b=",b)
sum(20)
'''
'''
def sum(a,b,c):
   print("a=",a)
   print("b=",b)
   print("c=",c)
   return a,b,c
sum(c=1,a=2,b=3)
'''

#WAF to check weather a number is perfect or not.
#A number is a perfect number which is a positive interger that is equal to the sum of its proper positive divisors,
#excluding the number itself,equivilately a perfect number is a number  that is half the sum of all its poitive divisiors.
'''
def perfectnumber(n):
   sum=0
   for i in range(1,n):
      if n%i==0:
         sum+=i
   return sum==n

n=int(input("Enter a Number:"))
print("Perfect Number?:",perfectnumber(n))
'''
'''
#WAF to calculate the HCF and LCM.
def LCM(n,m):
   if n>m:
      LCM=n
   else:
      LCM=m
   while True:
      if LCM%n==0 and LCM%m==0:
         break
      else:
         LCM+=1
   return LCM

n=int(input("Enter Number 1:"))
m=int(input("Enter Number 2:"))
print("LCM:",LCM(n, m))
'''

#Write a function to input a list, P, from the user and modify its content in such a way that the elements, 
#which are multiples of 10 swap with the value present in the very next position in the list. 
'''
def cal():
   i=9
   while i>1:
      if i%2==0:
         x=i%2
         i=i-1
      else:
         i=i-2
         x=i
      print(x**2)
cal() #49 25 9 1
'''
'''
def check(a):
   for i in range(len(a)):
      a[i]=a[i]+5
   return a
b=[1,2,3,4]
c=check(b)
print(c)  #[6,7,8,9]
'''
'''
def calc(u):
   if u%2==0:
      return u+10
   else:
      return u+2
def pattern(M,B=2):
   for CNT in range(0,B):
      print(calc(CNT),M,end="")
   print()
pattern("*")
pattern("#",4)
pattern("@",3)
'''
'''
def revert(num,last=2):
   if last%2==0:
      last=last+1
   else:
      last=last-1
   for c in range(1,last+1):
      num+=c
   print(num)
a,b=20,4
revert(a,b)
b=b-1
revert(b)
'''
'''
def convert(x=45,y=30):
   x=x-y
   y=x-y
   print(x,"&",y)
   return x
a=250
b=150
a=convert(a,b)
print(a,"&",b)
b=convert(b)
print(a,"&",b)
a=convert(a)
print(a,"&",b)
'''
'''
def change(p,q=30):
   p=p+q
   q=p-q
   print(p,"#",q)
   return(p)
r=150
s=100
r=change(r,s)
print(r,"#",s)
s=change(s)
'''
import random
'''
play=[40,50,10,20]
round=random.randint(2,3)
for j in range(round,1,-1):
   print(play[j],":",end="")
'''
'''
str1="EXAM2018"
str2=""
i=0
while i<len(str1):
   if str1[i]>="A" and str1[i]<"M":
      str2=str2+str1[i+1]
   elif str1[i]>="0" and str1[i]<="9":
      str2=str2+(str1[i-1])
   else:
      str2=str2+"*"
   i=i+1
print(str2)
'''
'''
Mystring="What@OUTPUT!"
str=" "
for i in range(len(Mystring)):
   if not Mystring[i].isalpha():
      str=str+"*"
   elif Mystring[i].isupper():
      val=ord(Mystring[i])
      val=val+1
      str=str+chr(val)
   else:
      str=str+Mystring[i+1]
print(str)
'''
'''
def convert(Str,l):
   S=""
   for Count in range(len(str)):
      if str[Count].isupper():
         S=S+Str[Count].lower()
      elif Str[Count].islower():
         S=S+Str[count].upper()
      elif Str[Count].isdigit():
         S=S+str(int(Str[Count])+1)
      else:
         S=S+"*"
   print(S)
text="CBSE Exam 2021"
Size=len(text)
convert(text,Size) #=>cbse*eXAM*3132
'''
'''
def Mycode(Msg,C):
   M=""
   for i in range(len(Msg)):
      if "B"<=Msg[i]<="H":
         M=M+Msg[i].lower()
      elif Msg[i]=="A" or Msg[i]=="a":
         M=M+C
      elif i%2==0:
         M=M+Msg[i].upper()
      else:
         M=M+Msg[i-1]
   print("New Line=",M)
text="ApaCHeSeRvEr"
Mycode(text,"#")  #=>New Line= #A#chHSSRReE
'''
'''
def Big(A,B):
   if(A>B):
      return chr(ord(A)+1)
   else:
      return chr(ord(B)+2)
WX="Exam"
W=""
L=len(WX)
for i in range(0,L-1,1):
   W=W+Big(WX[i],WX[i+1])
W=W+WX[L-1]
print(W)     #=>zyom
'''
'''
def jumbleup(t):
   ct=" "
   l=len(t)
   for c in range(0,l,2):
      ct=ct+t[c+1]
      ct=ct+t[c]
   t=ct
   ct=" "
   print(t)
   for c in range(1,len(t),2):
      if "U">=t[c]>+"M":
         if t[c]>="M" and t[c]<="U":
            ct=ct+"@"
      else:ct=ct+t[c-1:c+1]
   print(ct)
Str="HARMONIOUS"
jumbleup(Str) # => AHMRNOOISU AH@@OI@

'''
'''
a="Hello"
L=list(a)
a=" ".join(reversed(L))
print(a)
'''
'''
def count(start,end,step):
   for i in (start,end+1,step):
      print(i)
start=int(input("Enter Start Value:"))
end=int(input("Enter End Value:"))
step=int(input("Enter Step Value:"))
count(start, end, step)
'''
#Q1. Write a Python method/function Count(Start, End,Step) 
#    to display natural numbers from Start to. End in equal intervals of Step For example : If the values of Start as 14, End as 35 and Step as 6 The method should be displayed as 14 20 26 32
#Q2. Write a python method/function Count3and7(N) to find and display
#    the count of all those numbers which are between 1 and N,
#    which are either divisible by 3 or by 7. For Example: If the value of N is 15 The sum should be displayed as 7 (as 3,6,7,9,12,14,15 in between 1 to 15 are either divisible by 3 or 7)
#Q3.Write a method in python to find and display the prime numbers
#   between 2 to N. Pass N as argument to the method.

import math
# Write a generator function generatesq() that displays the square roots of numbers from 100 to n  where n is passed as an argument.
'''
def generatesq(n):
   for i in range(100,n+1):
      print((math.sqrt(i)))
n=int(input("Enter the End value:"))
generatesq(n)
'''
#Write a function in Python to find and display the prime number between 2 to n. Pass n as an argument to the method.
'''
n=int(input("Enter the End value:"))
for n in range(2,n+1):
      flag=True
      n1=n//2
      for i in range(2,n1):
         if n%i==0:
            flag=False
            break
      if flag==True:
         print(n,"Is a Prime number")           
'''
