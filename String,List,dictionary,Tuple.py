'''
str1=input("Enter String1:")
str2=input("Enter String2:")
if str1 in str2:
    str3=str2[:4]+"Restore"
print("Final String",str3)
'''
'''
s=input("Enter a String:")
if s[::-1]==s:
    print("It is a Palindrome:")
else:
   print("It is not a palindrome")
'''
'''
s=input("Enter a String:")
l=int(len(s)/2)
n=-1
f=True
print(l,n,f)
for i in range(0,l):
    if s[i]!=s[n]:
        print(s,"is not a palindrome")
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
'''
#WAP to display sum of even numbers upto number n entered by the user
n=int(input("Enter a Stop Value:"))
sum=0
i=0
while(i<n):
   sum=sum+i
   i=i+2 
   print(i)
'''
'''
#WAP to Print fibonnaci series upto a certain limit.
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
'''
#WAP to find the sum of the geometric series given below range,
#s=ar+ar^2+ar^3+...+ar^n.
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
'''
#WAP to print the sum of the series: 1+x^1/1!+x^2/2!+...+x^n/n!.
x=float(input("Enter Value of x:"))
n=float(input("Enter Value of n:"))
t=1
s=sum(x,n)
for i in range(1,n+1):
    t+=((x**i)/i)
print("Factorial:",t)
'''
'''
#WAP that find an elements index/position in a tuple. Without using index ().
t=eval(input("Enter a City Names:"))
x=eval(input("Enter city name to find its index:"))
l=len(t)
for i in range(0,l):
    if t[i]==x:
        print("Index of",x,"is:",i)
        break
'''
'''
#WAP that checks for presence of a value inside a dictionary and prints its keys with ignore case.
d={1:"apple",2:"banana",3:"grapes",4:"orange",5:"kiwi"}
a=""
d.values==a
for i in d:
    x=input("Enter a value to be Searched in the Dictionary:")
    if a in x:
        print("Key:",d.keys())
    break
'''
'''
#Write a Menu driven program to calculate: (a) Area of the circle, (b) Area of the square, (c) Area of rectangle.
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
'''
#WAP to create a dictionary named years whose keys are months names and values are corresponding number of days.
ask="y"
years={}
while ask=="y":
    months=input("Enter The Month Names:")
    days=input("Enter the Number of Days In the Corresponding Months:")
    years[months]=days
    ask=input("Do you want to enter more Months?(y/n):")
print("Years =",years)
'''
'''
#WAP that repeatedly asks the user to enter product name and prices. Store all of them in a dictionary whose keys are product names and values are prices. Also write a code to search an item form a dictionary.
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
#Patterns:-
'''
#Same Stars in all the rows:
n=5  
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
'''
'''
#To print Alphabets in order like this:
A 
B C
D E F
G H I J
K L M N O
P Q R S T U'''
'''
ch=65
r=int(input("Enter number of rows:"))
for i in range(1,r+1):
    for j in  range(0,i):
        print(chr(ch),end=" ")
        ch+=1
    print()
'''
'''
#Pattern in Increasing Order:
a="*"
r=int(input("Enter the number of rows:"))
for i in range(1,r+1):
    for j in range(0,i):
        print(a,end=" ")
        i+=1
    print()
'''
''''
#Pattern in Descending Order:
a="*"
r=int(input("Enter the number of rows:"))
for i in range(1,r+1):
    for j in range(i,r):
        print(a,end=" ")
        i+=1
    print()
'''
'''
#Pascals triangle
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
'''
#left to right Descending order:-
for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i+1,6):
        print("*",end=" ")
    print()
'''
'''
#left to right Descending order:-
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
'''
#Hills triangle:-
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
'''
#Hills trinagle Alter:-
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
'''
#WAP to create a tuple storing 9 terms of the Fibonacci series.
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
'''
#WAP as per following regulations:
#(a) Return the length of the shortest string in the tuple of a strings.
#(b)PRECONDITION:-the tuple contains at least one element.
t=eval(input("Enter a Tuple:"))
s=t[0]
for i in t:
    if len(i)<len(s):
        s=i
print("Smallest String:",s)
'''
'''
#Write a function check(key) which takes a key as argument and check weather that key is present in dictionary or not.
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
'''
#WAP to accept the number of terms say n form the user and display the dictionary in the form of {n:n*5}.
n=int(input(("Enter a Number:")))
d={}
for x in range(1,n+1):
    d[x]=x*5
print(d) 
'''
'''
#WAP to display maximum and the minimum value in a dictionary.
d={"Mathematics":95,"Computer Science":98,"Physcis":91,"Chemistry":96,"English":93}
maxvalue=max(d.values())
minvalue=min(d.values())
print("Maximum Value:",maxvalue)
print("Minimum Value:",minvalue)
'''


