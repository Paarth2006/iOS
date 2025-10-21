
'''#Write a Python script that accepts a lower-case string from the user at run-time and prints
#it after capitalizing every alternate character of the string.
x=input("Enter a String:")
l=len(x)
a=""
for i in range(l):
    if i%2!=0:
        a=a+x[i].upper()
    else:
        a=a+x[i].lower()
print("The New strig is:",a)
'''
'''
#Write a Python script that checks a given list of integers and prints “Balanced Oddity” if
#the list contains more odd numbers than even numbers, and prints “Unbalanced Oddity” otherwise.
x=eval(input("Enter a List of Integers:"))
l=len(x)
ev=0
od=0
for i in range(l):
    if x[i]%2==0:
        ev+=1
    else:
        od+=1
if ev>od:
    print("Unbalanced Oddity:",ev)
else:
    print("Balanced oddity:",od)
'''
'''
#Write a Python script that removes all the duplicate elements from a given list of integers. Display the list after making the changes.
x=eval(input("Enter a List:"))
l=[]
x1=len(x)
for i in range(x1):
    if x[i] not in l:
        l.append(x[i])
print("The New list is:",l)
'''
'''
#Write Python script to display the count of all the four-letter words of a string entered by the user at run-time.
x=input("Enter a Sentence:")
y=x.split()
c=0
for i in range(len(y)):
    if len(y[i])==4:
        c+=1
print("The Count for 4 Letter words is:",c)
'''
'''
#Write a Program to check if the entered number is Armstrong or not.
x=int(input("Enter a Number:"))
y=x
sum=0
d=0
while y>0:
    d=y%10
    sum=sum+d**3
    y=y//10
if sum==x:
    print(x,"is an armstrong number")
else:
    print(x,"it is not an armstrong number")
'''
'''
#WAp to print the following pattern:
#          5 
#        4 5
#      3 4 5
#    2 3 4 5
#  1 2 3 4 5
n=int(input("Enter the No. of rows:"))
for i in range(n):
    print("  "*(n-i),end="")
    for j in range(n-i,n+1):
        print(j,end=" ")
    print()
''' 
'''
#Insertion Sort:-
l=eval(input("Enter a Element:"))
n=len(l)
for i in range(1,n):
    temp=l[i]
    prev=i-1
    while prev>=0 and l[prev]>temp:
        l[prev+1]=l[prev]
        prev=prev-1
    l[prev+1]=temp
print("The Sorted List is:",l)
'''
'''
#Bubble Sort:-
l=eval(input("Enter the elements:"))
n=len(l)
for i in range(0,n-1):
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
print("THe sorted list is",l)
'''
'''
#Linear search:-
l=eval(input("Enter a list:"))
n=int(input("Enter the Number to be searched:"))
for  i in range(len(l)):
    if l[i]==n:
        print(n,"Found")
        break
    else:
        print(n,"Not Found")
'''
'''
#Binary Search:-
l=[]
n=int(input("Enter the size of list:"))
for i in range(n):
    element=int(input("Enter the elements:"))
    l.append(element)
sn=int(input("Enter Number to search:"))
l.sort()
fn=0
ln=len(l)-1
while fn<=ln:
    mn=(fn+ln)//2
    if l[mn]==sn:
        print(sn,"found at index",mn)
        break
    elif l[mn]<sn:
        fn=mn+1
    else:
        ln=mn+1
else:
    print(sn,"is not present in the given list.")
'''
'''
x=int(input("no."))
p=x
l=[]
while p!=0:
    a=x-((x//10))*10
    p=p//10
    x=x//10
    l.append(a)
if l==l[::-1]:
    print("palindrome")
else:
    print("not palindrome")
'''


