'''string1=input("Enter a String:-")
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
'''  # OUTPUT is false as they have different ASCII values.

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
ch="Our 3 Boys"
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
