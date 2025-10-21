'''
str1=input("Enter String1:")
str2=input("Enter String2:")
if str1 in str2:
    str3=str2[:4]+"Restore"
print("Final String",str3)
'''
#WAP to Check weather the given the words is a Palindrome or not.
'''
s=input("Enter a String:")
if s[::-1]==s:
    print("It is a Palindrome:")
else:
   print("It is not a Palindrome")
'''
'''
s=input("Enter a String:")
l=int(len(s)/2)
n=-1
f=True
print(l,n,f)
for i in range(0,l):
    if s[i]!=s[n]:
        print(s,"is not a Palindrome")
        f=False
        break
    else:
        n=n-1
if f==True:
    print(s,"is a Palindrome")
'''
'''
s="Test"
RS=" "
for ch in s:
    RS=ch+RS  #Another method to revese a string
    print(RS)
'''
'''
a=True
b=True
c=True
d=True
print(not(a and b and c))
print(not(a or b or c))
print(not a or not b or not c)
print(not a or not b or not c)
print(not(not a or not b or not c))
'''
'''
for x in range(2):
    for y in range(2):
        print(x,y,x+y)
'''
'''
x=2
y=3
for i in range(y*2-x):
    print(i,end="")
'''
'''
for i in range(1,51,3):
    print(i,end=" ")
'''
#WAP to display sum of even numbers upto number n entered by the user
'''
n=int(input("Enter a Stop Value:"))
sum=0
i=0
while(i<n):
   sum=sum+i
   i=i+2 
   print(i)
'''
#WAP to Print fibonacci series upto a certain limit.
'''
num=int(input("Enter the Number:"))
n1=0
n2=1
print("Fibonacci Series:",n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()
'''
#WAP to find the sum of the geometric series given below range,
#s=ar+ar^2+ar^3+...+ar^n.
'''
a = int(input("Enter First Number of an G.P Series:"))
n = int(input("Enter the Total Numbers in this G.P Series:"))
r = int(input("Enter the Common Ratio:"))
t=0
v=a
print("G.P Series:",end=" ")
for i in range(n):
    print(v,end = " ")
    t=t+v
    v=v*r
print("\n""The Sum of G.P Series:",t)
'''
import math
#WAP to print the sum of the series: 1+x^1/1!+x^2/2!+...+x^n/n!.
'''
x=float(input("Enter Value of x:"))
n=float(input("Enter Value of n:"))
t=1
s=sum(x,n)
for i in range(1,n+1):
    t+=((x**i)/i)
print("Factorial:",t)
'''
#WAP that find an elements index/position in a tuple. Without using index ().
'''
t=eval(input("Enter a City Names:"))
x=eval(input("Enter city name to find its index:"))
l=len(t)
for i in range(0,l):
    if t[i]==x:
        print("Index of",x,"is:",i)
        break
'''
#WAP that checks for presence of a value inside a dictionary and prints its keys with ignore case.
'''
d={1:"apple",2:"banana",3:"grapes",4:"orange",5:"kiwi"}
a=""
d.values==a
for i in d:
    x=input("Enter a value to be Searched in the Dictionary:")
    if a in x:
        print("Key:",d.keys())
    break
'''
#Write a Menu driven program to calculate: (a) Area of the circle, (b) Area of the square, (c) Area of rectangle.
'''
print (" Menu......", "\n", "a for Area for Circle","\n","b for Area of Square","\n","c for Area of Rectangle")
x=input("Enter Your Choice:")
if x=="a":
    r=float(input("Enter Radius of the Circle:"))
    areac=3.14*r**2
    print(areac)
elif x=="b":
    s=float(input("Enter Side of the Square:"))
    areas=s*s
    print(areas)
elif x=="c":
    l=float(input("Enter Length of Rectange:"))
    b=float(input("Enter Breadth of Rectagle:"))
    arear=l*b
    print(arear)
'''
#WAP to create a dictionary named years whose keys are months names and values are corresponding number of days.
'''
ask="y"
years={}
while ask=="y":
    months=input("Enter The Month Names:")
    days=input("Enter the Number of Days In the Corresponding Months:")
    years[months]=days
    ask=input("Do you want to enter more Months?(y/n):")
print("Years =",years)
'''

#WAP that repeatedly asks the user to enter product name and prices. Store all of them in a dictionary whose keys are product names and values are prices. Also write a code to search an item form a dictionary.
'''
ask="y"
d={}
while ask=="y":
    productname=input("Enter Product Name:")
    prices=int(input("Enter the Price:"))
    d[productname]=prices
    ask=input("Do you Want to Enter another Product(y/n)?")
i=input("Enter item to be searched:")
if i in d.keys():
    print(i,":",d[i])
else:
    print("No Data Available")
'''

#WAP to create a tuple storing 9 terms of the Fibonacci series.
'''
first=0
second=1
t=(first,second)
for i in range(0,7):
    nextnum=first+second
    first=second
    second=nextnum
    t+=(nextnum,)
print(t)
'''

#WAP as per following regulations:
#(a) Return the length of the shortest string in the tuple of a strings.
#(b)PRECONDITION:-the tuple contains at least one element.
'''
t=eval(input("Enter a Tuple:"))
s=t[0]
for i in t:
    if len(i)<len(s):
        s=i
print("Smallest String:",s)
'''
#Write a function check(key) which takes a key as argument and check weather that key is present in dictionary or not.
'''
def check(key):
    if key in d.keys():
        print(key,"Key Found")
    else:
        print("Key not found")
    return
d={"Jan":31,"Feb":28,"March":31}
key=input("Enter a Key:")
check(key)
'''
#WAP to accept the number of terms say n form the user and display the dictionary in the form of {n:n*5}.
'''
n=int(input(("Enter a Number:")))
d={}
for x in range(1,n+1):
    d[x]=x*5
print(d) 
'''
#WAP to display maximum and the minimum value in a dictionary.
'''
d={"Mathematics":95,"Computer Science":98,"Physcis":91,"Chemistry":96,"English":93}
maxvalue=max(d.values())
minvalue=min(d.values())
print("Maximum Value:",maxvalue)
print("Minimum Value:",minvalue)
'''

#Patterns:-
#Same Stars in all the rows:
'''
n=5  
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
'''
#To print Alphabets in order like this:
#A 
#B C
#D E F
#G H I J
#K L M N O
#P Q R S T U
'''
ch=65
r=int(input("Enter number of rows:"))
for i in range(1,r+1):
    for j in  range(0,i):
        print(chr(ch),end=" ")
        ch+=1
    print()
'''
#Pattern in Increasing Order:
'''
a="*"
r=int(input("Enter the number of rows:"))
for i in range(1,r+1):
    for j in range(0,i):
        print(a,end=" ")
        i+=1
    print()
'''
#Pattern in Descending Order:
'''
a="*"
r=int(input("Enter the number of rows:"))
for i in range(1,r+1):
    for j in range(i,r):
        print(a,end=" ")
        i+=1
    print()
'''
#Pascals triangle
'''
r=int(input("Enter the Number of rows:"))
s=r*2-1
for i in range(1,s+1):
    for j in range(0,s):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")
    s=s-2
    print()
'''
#left to right Descending order:-
'''
for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i+1,6):
        print("*",end=" ")
    print()
'''
#left to right Descending order:-
'''
a="*"
r=int(input("Enter the number of rows:"))
for i in range(1,r+1):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,r):
        print(a,end=" ")
        i+=1
    print()
'''
#Hills triangle:-
'''
n=5
a=int((n/2)*2)
for i in range(0,n,2):
    for j in range(0,a+1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    a=a-2
    print()
'''
#Hills trinagle Alter:-
'''
a="*"
r=int(input("Enter the Number of rows:"))
s=int(r/2*2)
for i in range(0,r,2):
    for j in range(0,s+1):
        print(end=" ")
    for j in range(0,i+1):
        print(a,end=" ")
    s=s-2
    print()
'''
#Write a program to read a string and print its character in different line – two characters per line.
'''
s=input("Enter a String:")
l=len(s)
for i in range(0,l,2):
    print(s[i:i+2])
'''
#Write a program to print the below pattern:
#P
#P Y
#P Y T
#P Y T H
#P Y T H O
#P Y T H O N
'''
s=input("Enter a String:")
for i in range(0,len(s)):
    print()
    for j in range(0,i+1):
        print(s[j],end=" ")
'''
#WAP to read a list of numbers and create another list which store half of each even number and double of each odd number in the list.
'''
x=eval(input("Enter a List:"))
ev=[]
od=[]
for i in x:
    if (i%2==0):
        ev.append(int(i/2))
    else:
        od.append(i*2)
print("Even lists:",ev)
print("Odd lists:",od)
'''
#WAP to input a tuple of integers and display sum of all numbers present in the tuple.
'''
t=eval(input("Enter a Tuple:"))
x=sum(t)
print("Sum of Tuple Elements:",x)
'''
#WAP to input a tuple of integers and count how many numbers are divisible by 5.
'''
t=eval(input("Enter a Tuple:"))
n=0
for i in range(0,len(t)):
    if t[i]%5==0:
        n+=1
print("Numbers divisible by 5 are:",n)
'''
#WAP to print odd and even numbers form a tuple.
'''
t=eval(input("Enter a Tuple:"))
ev=0
od=0
for i in range(0,len(t)):
    if t[i]%2==0:
        ev+=1
    else:
        od+=1
print("Even numbers:",ev)
print("odd Numbers:",od)
'''
#Find and write the output of the following python code:
'''
TXT=["20","50","30","40"]
CNT=3
TOTAL=0
for c in [7,5,4,6]:
    T=TXT[CNT]
    TOTAL=float(T)+c
    print(TOTAL)
    CNT-=1      #OUTPUT:-47.0,35.0,54.0,26.0
'''
'''print(True and not False or True and False)  #OUTPUT:-True'''
'''print(10%4+7/2)  #OUTPUT:- 5.5'''
#WAP to print the following series:-
#A 
#C E
#G I K
#M O Q S
'''
ch=65
r=int(input("Enter number of rows:"))
for i in range(1,r+2):
    for j in  range(0,i):
        print(chr(ch),end=" ")
        ch+=2
    print()
'''
#WAP to to accept a string and diplay the word which has a vowel "a" in it. Also display the number of times this vowel occurs.
'''
x=input("Enter a String:")
b=x.split()
c=0
flag = False
for i in b:
    flag= False
    for j in range(0,len(i)):
        if i[j]=="a":
            c+=1
            flag=True 
    if flag==True:
        print(i)
print ("Number of time a occurs", c)           
'''
#WAP to find the sum of elements entered by the user.
'''
n=eval(input("Enter Elements:"))
x=sum(n)
print("Sum of Elements:",x)
'''
#WAP to print the following output:-
#1
#3 3
#5 5 5
#7 7 7 7 
'''
x=4
i=1
while i<=x:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j=j+1
    i=i+1
    print(" ")
'''
#WAP to find the maximum from 10 numbers inputed by the user.
'''
x=eval(input("Enter 10 Numbers:"))
print(max(x))
'''
#Write a Python script that accepts a lower-case string from the user at run-time and prints
#it after capitalizing every alternate character of the string.
'''
x=input("Enter a String:")
l=len(x)
a=""
for i in range(l):
    if i%2!=0:
     a=a+x[i].upper()   
    else:
        a=a+x[i].lower()
print(a)
'''
#Write a Python script that checks a given list of integers and prints “Balanced Oddity” if
#the list contains more odd numbers than even numbers, and prints “Unbalanced Oddity” otherwise.
'''
x=eval(input("Enter a List:"))
l=len(x)
ev=0
od=0
for i in range(l):
    if x[i]%2==0:   # only i calculates the index value.
        ev+=1
    else:
        od+=1
if ev>od:
    print("Unbalance oddity",ev)
else:
    print("Balance oddity",od)
'''
#Write a Python script that removes all the duplicate elements from a given list of integers.Display the list after making the changes.
'''
x=eval(input("Enter a list of intergers:"))
l=[]
x1=len(x)
for i in range(x1):
    if x[i] not in l:
        l.append(x[i])
print(l)
'''
#Write Python script to display the count of all the four-letter words of a string entered by the user at run-time.
'''
x=input("Enter a Sentence:")
y=x.split()
c=0
for i in range(len(y)):
    if len(y[i])==4:
        c+=1
print("count of 4 letter word:",c)
'''
#Write a Program to check if the entered number is Armstrong or not.
'''
x=int(input("Enter a number:"))
y=x
sum=0
d=0
while y>0:
    d=y%10
    sum=sum+d**3
    y=y//10
if x==sum:
    print(x,"Is an armstrong Number:")
else:
    print(x,"Is Not an armstrong Number:")
'''
#WAP TO FIND THE SUM OF THE SERIES :- 1 +1/2 +1/3 TILL 1/N.
'''
x=int(input("Enter a Number"))
y=0
for i in range(1,x+1):
   y+=1/i
print("The Series is:",y)
'''
#WAP TO PRINT THE FOLLOWING PATTERN:-
#   *
#  ***
# *****
#*******
'''
x=int(input("Enter the number of rows:"))
for i in range(x):
    print(" "*(x-i-1),end="")
    for j in range(0,2*i+1):
        print("*",end="")
    print()
'''
#Milk calculator.
'''
x=float(input("Enter Number of liters of Milk Per Day:"))
z=int(input("Enter The Price of 1 liter Milk:"))
y=input("Enter The Month:")
y=y.lower()
ask=input("Was there any leave in the month(y/n)?:")
if ask=="y":
    b=int(input(("How many days was the leave for?:")))
else:
    b=0 
if y=="january":
        print("Your Monthly bill is of:",(31-b)*x*z)
        print("Number of litres of milk is",(31-b)*x)
elif y=="february":
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)
elif y=="march":
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)
elif y=="april":
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)
elif y=="may":
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)  
elif y=="june":
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)
       
elif y=="july":
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)
elif y=="august":
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)
elif y=="september":       
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)
elif y=="october":        
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)
    
elif y=="november":        
            print("Your Monthly bill is of:",(31-b)*x*z)
            print("Number of litres of milk is",(31-b)*x)
        
elif y=="december":
        print("Your Monthly bill is of:",(31-b)*x*z)
        print("Number of litres of milk is",(31-b)*x)
'''
#WAP to rmeove all Vowels from a word.
'''
s=input("Enter a String:")
vowels=["a","e","i","o","u"]
for i in s:
    if i in vowels:
        s=s.replace(i,"")
print(s)
'''
#ALTER
'''
x=input("Enter a String:")
b=["a","e","i","o","u","A","E","I","O","U"]
c=""
for i in x:
    if i in b:
        c+=""
    else:
        c+=i
print(c)
'''
#Multiplication table
'''
for i in range(9):
    for j in range(9):
        print((i+1)*(j+1),end="  ")
    print()
'''
