'''
#Write a program to show entered string is a palindrome or not.
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("It is a palindrome")
else:
      print("Not a palindrome")
'''
'''
#Write a program to show statistics of characters in the given line (to counts the number of alphabets, digits, uppercase, lowercase, spaces and other characters).
text = input("Enter a string:")
lower=upper=digit=space=0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch == ' ':
        space += 1
print("The number of uppercase letters:", upper)
print("The number of lowercase letters:", lower)
print("The number of digits:", digit)
print("The number of whitespace characters:", space)   
'''
'''
#WAP to remove all odd numbers from the given list.
x=eval(input("Enter a list of Numbers:"))
print(x)
for i in x:
      if i%2!=0:
            x.remove(i)
print(x)
'''
'''
#WAP to display those string which are starting with ‘A’ from the given list.
x=str(input("Enter a String:"))
y=x.split()
for i in y:
    if i.startswith("A"):
        print("Word Starts with A")
    else:
        print("Word doesn't start with A")
'''
'''
#WAP to find and display the sum of all the values which are ending with 3 from a list.
x=eval(input("Enter a Number:"))
sum=0
for i in x:
    if i%3==0:
        sum+=i
        print("Their sum=",sum)
    else:
        print("The Number doesn't end with 3")

'''
'''
#WAP to swap the content with next value, if it is divisible by 7 in a list.
num=eval(input("Enetr a list:"))
num.reverse()
for i in range(len(num)-1):
    if num[i]%7==0:
        num[i-1],num[i]=num[i],num[i-1]
num.reverse()
print("The required answer:",num)
'''
'''
#WAP to accept values from a user and create a tuple.
t=eval(input("Enter a Tuple:"))
print(type(t))
'''
'''
#WAP to input total number of sections and stream name in 11th class and display all information on the output screen.
n=int(input("Enter Number of Sections:"))
l={}
for i in range(n):
    a=input("Enter Section:")
    b=input("Enter Stream:")
    l[a]=[b]
print("Class","\t","Section","\t","Stream")
for i in l:
  print("XI","\t",i,"\t","\t",l[i])
'''
'''
#WAP to find factorial of entered number.
num=int(input("Enter a Number:"))    
factorial=1    
if num<0:    
   print(" Factorial does not exist for negative numbers")    
elif num==0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial=factorial*2    
   print("The factorial of",num,"is",factorial)    
'''
'''
#WAP to call func() to find greater out of entered two numbers.
x=int(input("Enter a Number:"))
y=int(input("Enter a Number:"))
if x>y:
    print(x,"is greater than",y)
else:
    print(y,"is greater than",x)
'''
'''
#WAP to show all prime numbers in the entered range.
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 +1)):
        if(Number% i==0):
            count=count+1
            break
    if (count==0 and Number != 1):
        print("%d"%Number,end='  ')
'''
'''
#WAP to insert item on selected position in list and print the updated list. 
x=eval(input("Enter a List:"))
b=x[:]
b.insert(2,3)
print(b)
'''
'''
#WAP to input the value of x and n and print the sum of the series
x=int(input("Enter 1st Number:"))
n=int(input("Enter 2nd Number:"))
sign=x
sign==1
for a in range(2,n+1):
    f=1
    for i in range(1,a+1):
        f*=i
    term=((x**a)*sign)/f
    sign+=term 
    sign=-1
print("Sum of first",n,"terms:",sign)
'''
'''
str1=input("Enter a String:")  
newStr = "" 
for i in range(0,len(str1)):  
    if str1[i].islower():  
         newStr+=str1[i].upper();    
    elif str1[i].isupper():  
        newStr+=str1[i].lower();  
    else:  
        newStr+=str1[i];          
print("String after case conversion:"+newStr);  
'''
'''
x=eval(input("Enter a List"))
ev_li=[]
od_li=[]
for i in x:
    if (i%2==0):
        ev_li.append(i)
    else:
        od_li.append(i)
print("Even lists:",ev_li)
print("Odd lists:",od_li)
'''
