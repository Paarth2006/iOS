#PRACTICAL FILE:-
#Q1.Write a program to check a number whether it is palindrome or not.
#A.
'''
x=input("Enter a String:")
z=x[::-1]
for i in x:
    y=input("Enter Another String:")
    if y==z:
        print("It is a Palindrome")
    else:
        print("Not a Palindrome")
    break
'''
#Q2.Write a program to display ASCII code of a character and vice versa.
#A.
'''
while True:
    a=int(input("Enter 1 for ASCII CODE\nEnter 2 for ASCII VALUE\nEnter your Choice:"))
    if a==1:
        x=input("Enter a Character:")
        print(ord(x))
    a=int(input("Enter 1 for ASCII CODE\nEnter 2 for ASCII VALUE\nEnter your Choice:"))
    if a==2:
        y=int(input("Enter a Number:"))
        print(chr(y))
    b=input("Do you Want to Try for again?(y,n):")
    if b in "yY":
        a=int(input("Enter 1 for ASCII CODE\nEnter 2 for ASCII VALUE\nEnter your Choice:"))
        if a==1:
            x=input("Enter a Character:")
            print(ord(x))
        if a==2:
            y=int(input("Enter a Number:"))
            print(chr(y))
    if b in "nN":
        break
'''        
#Q3.Write a program that adds individual elements of list 2 and 3 into 1.
#Resultant list should be in order of elements of list 3, list1,list 2.
#A.
'''
l=[]
l1=[]
l2=eval(input("Enter Elements in list 2:"))
l3=eval(input("Enter elements in list 3:"))
l1=[l2,l3]
l=[l3,l1,l2]
print(l1)
print(l)
'''
#Q9.Write a program to count number of words in a file.
#A.
'''
f=open("test file","w")
x=input("Enter some words:")
f.write(x)
f.close()
f=open("test file","r")
d=f.read()
d1=d.split()
print(len("total number of words are:",d1))
'''
#Q10.Write a Program to read and display file content line by line with each word separated by"#".
#A.
'''
f=open("hast.txt","r")
d=f.readlines()
for i in d:
    k=i.split()
    for j in k:
        print(j+"#",end=" ")
    print(" ")
'''
#Q11.Write a program to copy all the lines that not contain the character `a&#39; in a file and write it to another file.
#A.
'''
f=open("python.txt","w")
x=input("Enter some words:")
f.write(x)
f.close()
f=open("python.txt","r")
f1=open("nextpython.txt","w")
l=f.readlines()
for i in l:
    if "a" in i:
        i=i.replace("a"," ")
        f1.write(i)
f1.close()
f.close()
f1=open("nextpython.txt","r")
d=f1.read()
print(d)
'''
#Q12.Program to read the content of file and display the total number of consonants, uppercase, vowels and lower case characters.
#A.
#Done in laptop

#Q13.Program to create binary file to store Rollno and Name, Search any Rollno and display name if Rollno found otherwise "Rollno not found".
#A.
import pickle
'''
f=open("student.dat","wb")
lst_master=[]
a="y"
while a=="y":
        rollno=int(input("Enter a Roll Number:"))
        name=input("Enter the Name:")
        lst_master.append([rollno,name])
        a=input("Do you want to Enter More Elements?(y/n)")
pickle.dump(lst_master,f)
f.close()
print("Data Written Successfully")
f=open("student.dat","rb")
lst_master=[]
while True:
    try:
        lst_master=pickle.load(f)
    except EOFError:
        break
a="y"
while a=="y":
    found=False
    x=int(input("Enter the Rollno you want to find:"))
    for i in lst_master:
        if i[0]==x:
            print("Name is:",i[1])
            found=True
            break
        else:
            print("Rollno not found")
    break
f.close()
'''
#Q14.Program to create binary file to store Rollno, Name and Marks and update marks of entered Rollno.
#A.
'''
f=open("school.dat","wb")
lst_master=[]
l=[]
a="y"
while a=="y":
    rollno=int(input("Enter the RollNo:"))
    Name=input("Enter the Name:")
    marks=int(input("Enter the Marks:"))
    l=([rollno,Name,marks])
    lst_master.append(l)
    a=input("Do You Want To Enter More Elements?(y/n):")
pickle.dump(lst_master,f)
f.close()
print("Data Dumped Successfully")
f=open("school.dat","rb+")
flag=0
try:
    d=pickle.load(f)
    srch_rollno=int(input("Enter Roll No for which record is to be updated:"))
    for i in d:
        if i[0]==srch_rollno:
            print("Current marks are:",i[2])
            i[2]=input("Enter Updated Marks:")
            flag=1
            break
    if flag==0:
        print("No record found")
    else:
        f.seek(0)
        pickle.dump(d,f)
        print("Data updated successfully!")
        print(d)
except Exception:
    f.close()
'''
#Q15.Write a program to perform read and write operation with .csv file.
#A.
import csv
'''
f=open("test.csv","w",newline="")
w=csv.writer(f)
w.writerow(["Item Code","Item Desc","Quantity","Price"])
x=int(input("Enter number of elements:"))
l=[]
for i in range(x):
    itemcode=int(input("Enter Item Code:"))
    itemdescription=input("Enter Item Description:")
    quantity=int(input("Enter Quantity:"))
    price=int(input("Enter the price:"))
    l.append([itemcode,itemdescription,quantity,price])
w.writerows(l)    
f.close()
def item():
    f=open("test.csv","r")
    sw=csv.reader(f)
    y=int(input("Enter Item code to be searched:"))
    for i in sw:
        if i[0]==str(y):
            print(i)
    f.close()
item()
'''
s=input("Enter a String:")
c=0
for i in s:
    c+=1
    print(c)

