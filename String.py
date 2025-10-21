'''
string1=input("Enter a String:-")
print("The",string1,"in reverse order is")
length=len(string1)
for a in range(-1,(- length -1),-1):
    print(string1[a] )
'''
'''SLICING
x="python"
print(x[::])
'''
'''x="Python"
x[0]="y"
print(x)
'''
'''
x="python"
for i in range(0,len(x)):
print(i)
print(x[i]
'''
'''
x="python is fun"
print(x.capitalize())
'''
'''
x="python is fun"
print(x.count("i",4,8))'''

'''
x="python is fun"
print(x.find("i"))
'''
'''
x="python is fun"
print(x.index("z"))
'''

'''
x="python is fun"
y="7"
print(x.isdigit())
print(y.isdigit())
'''
'''
#Negative Indexing:-
x="Python"
print(x[-1])
'''
'''
x="Python"
print(x.upper())
print(x.lower())
'''
'''x="Python1"(if space b/w Python and 1 then OUTPUT= false)
print(x.isalnum())
'''
'''print("abc,DEF".split(","))
#split breaks one string into multiple string at space and returns the string
'''
'''
x="abc"
y="ABC"
print(x==y)
''' 
# OUTPUT is false as they have different ASCII values.
'''
x=str(input("Enter your string: "))
i=0
for i in range(0,len(x)):
    i+=int(x[i])
print(i)
'''
'''
x="Python is fun"
y=x.replace("fun", "nice")
print(y)
'''
'''
x="    Python            "
print(x) 
print(x.lstrip())
print(x.rstrip())
'''
'''
x="python is fun"
z= "x.istitle()"
y="Python is fun"
print(x.istitle(),  y.istitle(),  z.istitle())
'''
'''
x=str(input("Enter string:"))
a=0
for i in range(0,len(x)):
      if(a.islower()):
            a+=1
print("The number of lowercase characters is:")
print(a)
'''

'''
x=input("Enter a String:")
if (x==x[::-1]):
    print(x,"Is a palindrome.")
else:
    print(x,"Is not a palindrome.")
'''
'''
x=input("Enter a String:")
y= input("Enter a Character: ")
z= input("Enter the New Character: ")
i= x.replace(y,z)
print("Old String: ", x)
print("New String: ", i)
'''
'''
x=input("Enter a string:")
y=input("Entera word:")
if(x.find(y)==-1):
      print("Substring not in string")
else:
      print("Substring in string")
'''
'''
x=input("Enter a string:")
i=0
for a in x:
      i+=1
print("Length of the string is:")
print(i)
'''

'''
x = input("Enter a String:")
y = "!@$%^&*()-+?_=,<>/"
if y == x:
    print("yes")
else:
    print("no")
'''

'''
x="Python is fun"
print(x.swapcase())
'''

'''
x="Python is fun"
print(x.partition('i'))
print(x.split('i'))
'''

'''
x="Python is fun"
y=':'
print(y.join(x))
'''
'''
x=0
line=input("Enter a string:")
for i in line:
    if(i.isspace()):
        x+=1
print("The number of spaces are: ",x)
'''
'''
x=input("Enter string:")
v=0
for i in x:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            v+=1
print("Number of vowels are:")
print(v)
'''

'''
x=input("Enter string:")
x=x.replace(' ','-')
print("Next string:")
print(x)
'''

'''
x=input("Enter string:")
y=0
for i in x:
      y+=1
z=x[0:2]+x[y-2:y]
print("New string=:")
print(z)
'''

'''
x=input("Enter string:")
y=0
z=0
for i in x:
      if(i.isdigit()):
            y+=1
      z+=1
print("The number of digits are:")
print(y)
print("The number of letters are:")
print(z)
'''
'''
str1 ='python'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])
'''

'''
x = int(input("Enter a Number: "))
str = input("Enter a String: ")

digitsStr = ''
digitsNum = 0;

for ch in str :
    if ch.isdigit() :
        digitsStr += ch

if digitsStr :
    digitsNum = int(digitsStr)

print(x, "+", digitsNum, "=", (x + digitsNum))
'''

'''
m="Python Programming"
S=''
L=len(m)
for i in range(0,L):
	if i%2==0:
		S+=m[i].upper()
	else:
		S+=m[i]
print(S,"#",i)
'''
'''ch="Our 3 Boys"
string=""
for p in range(0, len(ch)-1):
	if ch[p].isdigit():
		string +="-"
	elif ch[p].isupper():
		string +=ch[p+1].lower()
	elif ch[p].islower():
		string +=ch[p+1].upper()
	elif ch[p]=="":
		string +="*"
print(string)
'''
'''
x=input("Enter a String:-")
length=len(x)
a=0
b=''
lenb=0
for i in range(length):
    if x[i]in 'aeiou'or x[i]in 'AEIOU':
        if len(b)>a:
            b=a
            a=lenb
            b=''
            lenb=0
    else:
        b+= x[a]
        lenb=len(b)
    a+=1
    print("Maximum Lenght is:",a,end='')
    print("With",a,"Characters")
'''

'''
x=input("Enter a String:")
y=input("Enter a Character:")
print("Deleted Characters are:-")
print(x.replace(y,''))
''' 

'''x=(input("Enter a String:"))
if  len(x)>3:
        print("length is greater than 3")
else:
        print("length is less than 3") 
'''
'''x="Python is fun"
print(x[-2])
print(x[9])
'''
'''x=eval(input("Enter a list"))
print(x)
print(type(x))
'''
'''a=input("Enter a String:")
length=len(a)
print("Original String",a)
b=""
for i in range(0,length,2):
    b+=a[i]
    if i< (length-1):
        b+=a[i+1].upper()
print("Alternatively Capitalized String:",b)
'''
'''a=input("Enter a String:")
length=len(a)
b=0
c=''
d=''
lend=0
for i in range(length):
    if a[i] in'aeiou' or a[i] in 'AEIOU':
        if lend>b:
            c=d
            b=lend
            d=''
            lend=0
    else:
        d+=a[i]
        lend=len(d)
    i+=1
print("Maximum length consonant substring is:",c,end='')
print(" with",b,"Characters")
'''
'''s="This is a book"
print(s.split("i"))
'''
'''x=[]
y=list()
'''
#list within a list is called nested list
#list is a mutable datatype,its memory location can be changed

'''
x=["xyz",1,[["lmn","pqr"],"abcdef"]]
print(x[1:3])
print(x[2][0][1])
x[1:3] = "python"
print(x):-['xyz', 'p', 'y', 't', 'h', 'o', 'n']
'''
#WAP to input two list and create a third one that contains all the elements of both the lists.

'''x=eval(input("Enter List 1 : "))
y=eval(input("Enter List 2 : "))
z=x+y
print(z)
'''
#WAP to put even and odd elements in a list into 2 different list

'''a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)
'''
'''l=list(input("list:"))
x=int(input("No.="))
for i in range(0,len(l)):
    z=str(l[i])
    if z.isdigit():
        if z==x:
            print('id=',i, 'digit=',end="")
            print(l[i])
'''
'''#WAP to display square of an element if it is an integer and change the place if the element is  a string.
x=(input("Enter a List:"))
z=0
for i in x:
    if str(i).isdigit():
        i=int(i)*int(i)        
        z.append(i)
    elif str(i).isalpha():
            i=str(i).swapcase()
            z.append(i)
    else:
        z.append(i)
print(z)
'''
'''n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
'''
'''#WAP that reads a line then counts how many times a substring occurs and display the count.
x=input("Enter a String:")
a=0
for i in range(len(x)):
    print(x)
    a+=1
print("Total No. Of Words:",a)
'''
'''
#WAP to input a list from the user add 5 in all the odd values and add 10 in all the even values of the list, display the final list.
a=[]
n=int(input("Enter number of elements:"))
b=int(input("Enter element:"))
a.append(b)
for i in range(1,n+1):
    even=[]
        odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
else:
    odd.append(j)
print("The even list",even)
print("The odd list",odd)
'''
'''#WAP to delete all odd numbers and negative numbers in a given list.
x=eval(input("Enter a list:"))
for i in x: 
    if i % 2 == 1:
        x.remove(i)
        print(x)
    elif i < 0:
        print(x.remove(i))
'''
'''
#WAP which accepts a number from the user and prints the frequnecy of the number in the list. If number not in list print number not in list.
x=eval(input("Enter the list:"))
y=[1,2,3,4,5]
for i in x:
    i=x.count()
if i==0:
    print("Not in List.")
else:
    print("Frequency:",y)
'''
'''
#WAP 
x=eval(input("Enter a list:"))
for i in x:
    if type(i)==int:
        print(i**2)
    elif type(i)==str:
        print(i.swapcase())
    else:
        print("No")
'''
#WAP that inputs a line of text and prints each word in a seperate line also print the count of words.
'''x=input("enter a list:")

a=0

for i in x.split():
    print(i)

    a+=1

print("Words are:",a)
'''

#WAP to input a string and print each individual word of it along with its length.

'''x=input("Enter a String:")

a=x.split(' ')

for i in x:

    print(i,len(i))
'''

#WAP that removes all capitalisation and common punctuation from a string "s".

'''s1=input("Enter 1st String:")
s2=input("Enter 2nd string:")
print("Initial Strings:",s1,s2)
if s1 in s2:
    s3=1
    s3=s2[:4]
print("Final Strings:",s1,s3)
'''
#WAP that reads email id of a person in the form of a string and ensures that it belong to domain @edupillar.com.

'''email=input("Enter your e-mail ID:")
domain='@edupillar.com'
z=email[len(email)-len(domain)]
if z== domain:
    if len(domain)!=len(email):
        print("Valid email")
    else:
        print("Invalid email")
else:
    print("This email is not at all valid")
'''
#WAP that ask the user for a string and creates a new string that doubles each character of the original string.
'''s=input("Enter a String:")
a=" "
for i in s:
    a=a+i*2
print("Original String:", s)
print("Doubled String:",a)
'''
'''x=input("Enter a String:")
y=0
z=1
for i in x:
    y==1
    if(i==' '):
        z+=1
print("Number of words are",z)
print("Number of characters are",y)
'''
#WAP to find the largest element in the list.
'''x=[]
y=int(input("Enter number of elements:"))
for i in range(1,y+1):
    z=int(input("Enter an element:"))
    x.append(z)
x.sort()
print("Largest element is:",x[y-1])
'''
'''l=[123,456,4647]
l.insert(0,465)
print(l)

l=[123,456,4647]
l.reverse()
print(l)

l=[1,2,3,4,5,3]
print(l.index(3))

l=[1,34,55,7,686]
l.sort(reverse=True)
print(l)
'''
'''
#DEL STATEMENT:-
l=[1,34,43,46]
del l[0:2]
print(l)

#POP FUNCTION:-
l=[1,35,45,46]
l.pop()
print(l)
#REMOVE FUNCTION:-
l=[1,34,43,46]
l.remove(34)
print(l)
'''
'''
#Write a program with a user defined function to count the number of times a character occurs in a given string.
def str():
    s=input("Enter a string: ")
    l=[]
    for i in s: 
        if i not in l:
            l.append(i)
    for j in l:
        print(" ",j,s.count(j))
str()
'''
'''
#Write a program with a user defined function with string as a parameter which replaces all vowels in the string with.
Str=input("Enter a String:")
def replace(Str):
    s=""
    for i in Str:
        if i in "aeiouAEIOU":
            s+="*"   
        else:
            s+=i
    print("Original string:",Str)
    print("New String:",s)
replace(Str)
'''
'''
#Write a user-defined function to check if a number is present in the list or not. If the 
#number is present, return the position of the number. Print an appropriate message if the number is not present in the list.
l=eval(input("Enter a list:"))
n=int(input("Enter number to search:"))
def search(l,n):
    if n in l:
        print("Element",n,"Found at Index:",l.index(n))
    else :
        print(n,"Element not Found")
search(l,n)
'''
