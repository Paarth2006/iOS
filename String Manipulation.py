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

