'''
#WAP to concatenate following dictionaries:-
#dic1={1:10,2:20}
#dic2={3:30,4:40}
#dic3={5:50,6:60}
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)
'''
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)'''
'''
#sample_dict = {'a': 100, 'b': 200, 'c': 300}
#Write a Python program to check if value 200 exists in the following dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 is present in dict')
'''
'''
#WAP  that repeatedly asks the user to enter product names and prices. Store all of them in a dictionary whose keys are product names and values are prices. Also write a code to search an item from the dictionary.any(i)
dic={}
while True :
    product=input("Enter the Name of the Product:")
    if product=="a"or product=="A":
        break
    else :
        price=int(input("Enter product price:"))
        dic[product]=price
while True :
    name=input("Enter(Enter a for Quit) the name of the product:")
    if name=="a"or name=="A" :
        break
    else :
        if name not in dic :
            print("Invalid Name")
        else :
            print("Product Price:",dic[name])
'''       
'''
#What will be the status of the following list after fourth pass of bubble sort arranging it in descending order?
#95, -1, 38, 2, 100, 65, 78
l=[95,-1,38,2,100,65,78]
for i in range(4):
    for i in range(0,len(l),-i-1):
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            print(l[j])
'''
'''
#WAP to print the series:
(i)10 9 8.....1
(ii) 1 -4 7 -10......-40
(iii) 1 8 27 64.....n
(iv) 1, 11, 111, 1111.....n
'''
'''
(i)
for i in range(10,0,-1):
    print(i,end=" ")
'''
'''
(ii)
x=1
for i in range(1,41,3):
    if i%2==0:
        x=-1
    print(i*x,end=" ")
'''
''' 
(iii)  
n=int(input("Enter the range:"))
i=1
while(i<=n):
    print(i*i*i,end=" ")
    i+=1
'''
'''
(iv)
x=int(input("Enter the repetating value:"))
for i in range(x):
    print('1'*i, end =" ") 
'''
'''
#WAP to input a line and count the number of spaces.
x=input("Enter anything:")
count=0
for i in range(0, len(x)):
        if x[i]==" ":
            count+=1
            print("No.of Spaces",count)
'''
'''
#WAP to find whether the given character is a digit or a letter.
x=input("Enter a Value:")
if x[0].isalpha() :
    print(x[0],"It is an alphabet")
elif x[0].isdigit() :
    print(x[0],"It is a digit")
'''
'''
#WAP to convert a lowercase letter to uppercase letter.
x=input("Enter a String:")
print("UpperCase:",x.upper())
'''
'''
#Write a program to read 3 numbers in ascending order.
x=int(input("Enter a Number:"))
y=int(input("Enter a Number:"))
z=int(input("Enter a Number:"))
if x<y:
    print(x,y)
elif:
    print(y,x)
else:
    print(z,x)
'''
'''
#WAP to find word,character,consonant and vowels.
s=input("Enter a String:")
v=0
c=0
for i in s:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or 
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           v=v+1
    else:
        c=c+1
print("The number of vowels:",v)
print("The number of consonant:",c)
'''
'''
#WAP to print all number in a range divided by a given number.(as 5)
l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))
for i in range(l,u+1):
   if(i%5==0):
      print(i)
'''
'''
#WAP to find largest and smallest number out of 10 numbers.
l=[]
n= int(input("Enter till which number:"))
for i in range(n):
    numbers= int(input("Enter a number:"))
    l.append(numbers)
print("Maximum element in the list is:", max(l))
print("Minimum element in the list is:", min(l))
'''
'''
#WAP to accept the age of n employees and count the number of person in the
#following age group:a. Under 18  b. 18-25  c. 26-50  d. 51-80  e. above 80.
n=int(input("Enter the number of employees:"))
count17=0
count1825=0
count26=0
count51=0
count81=0
list=[]
for i in range(1,n+1):
    age=int(input("Enter the age of employee:"))
    list.append(age)
    print(list)
for i in list:
    if int(i)<18:
        count17 += 1
    elif 17 < int(i) <26:
        count1825 += 1
    elif 25 < int(i) < 51:
        count26 += 1
    elif 50 < int(i) <81:
        couunt51 += 1
    elif int(i) > 80:
        count81 += 1
print("<18:",count17)
print("18-25",count1825)
print("26-50:",count26)
print("51-80:",count51)
print(">80:" ,count81)
'''
'''
#Create a dictionary "odd" of odd numbers between 1 and 10, where the key is the decimal number and the value is the corresponding number in words. Perform the following operations on this dictionary:
#(a) Display the keys
#(b) Display the values
#(c) Display the items
#(d) Find the length of the dictionary
#(e) Check if 7 is present or not
#(f) Check if 2 is present or not
#(g) Retrieve the value corresponding to the key 9
#(h) Delete the item from the dictionary corresponding to the key 9
odd={1:"One",3:"Three",5:"Five",7:"Seven",9:"Nine"}
print(odd.keys())
print(odd.values())
print(odd.items())
print(len(odd))
print(7 in odd.keys())
print(2 in odd.keys())
print(odd.get(9))
del odd[9]
'''
'''
#Write a program to enter names of employees and their salaries as input and store them in a dictionary.
n=int(input("Enter the number of Employees:"))
i=1
employee={}
while i<=n:
    Name=input("Enter the Employee Name:")
    Salary=int(input("Enter Employee Salary:"))
    employee[Name]=Salary
    i+=1
print("\nEmployee",Name,Salary)
'''
#Write a program to read email IDs of n number of students and store them in a tuple. Create two new tuples, one to store only the usernames from the email IDs and second to store domain names from
#the email IDs. Print all three tuples at the end of the program. [Hint: You may use the function split()]
'''
n= int(input("Enter the number of students:"))
lst=[]
for i in range(n):
    email=input("Entera valid email:")
    lst.append(email)
tup1=tuple(lst)
names=[]
domains=[]
for i in tup1:
    n,d=i.split("@") 
    names.append(n)
    domains.append(d)
names=tuple(names)
domains=tuple(domains)
print("Names:",names)
print("Domains:",domains)
print("Tuple:",tup1)
'''






