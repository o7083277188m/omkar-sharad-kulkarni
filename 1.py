
'''
a=eval(input("enter list:"))
c=list(a)
b=max(a)
c.remove(b)
print (max(c))

'''

'''
a=eval(input("enter list:"))
d=list(a)
if c==max(a):
  print("the number",c)
'''


'''
a,b,c=[float(x)for x in input("enter the 3 float numbers:").split()]
print("the sum is:",a+b+c)
'''

      
"""

 _____________REVERSING THE STRING _______________--

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = "Omkar"
  
print ("The main string of 1st way : ",end="") 
print (s) 
  
print ("The reversed string  of 1st way: ",end="") 
print (reverse(s)) 






txt = "omkar"[::-1]
print("the reversed string of 2nd output is:",txt)



def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 
  
s = "omkar"
  
print ("The main string 3rd : ",end="") 
print (s) 
  
print ("The reversed 3rd string is : ",end="") 
print (reverse(s)) 




txt = "omkar"[::-2]
print("the reversed string of GK output is:",txt)





"""

"""

for printing just 1st ,2nd....and repeating a same string


s="durga"
print("the value is:",s[0])

s="durga"
print("the value is:",s[1:5])

a=s*3
print("the new string is:",a)

"""


"""
a=int(123.12)
print("the value is :",a) 

b=float(15)
print("the value is:",b)

c=complex(10)==>10+0j
print("the value of c is:",c)


"""

'''

list = [] 
   
n = int(input("Enter number of elements : ")) 
   
for i in range(0, n): 
    y = int(input()) 
  
    lst.append(y) 
      
print(n)



def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

'''
"""
def sum(numbers):
    total=0
    for x in numbers:
       total += x
    return total
print(sum(list))


list=eval(input("enter list:"))

print(list)
print(int(list))


"""

'''
s="learning python is very easy"
l=s.split()
print(l)


s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
k=[5,6,7,8]
c=s*3
print(c)

print(s[0],k[0])


print(s[2:7:2])
print(s[2:13:2])



i=0
while i<len(s):
   print(s[i])
   i=i+1   


s[2]=150
print(s)

c="venkatesh"
a=list(c)
print(a)

i=0
for i in a:

'''    
     

"""

    
list=eval(input("enter list:"))
print(list)

def multiply(numbers):
    count=1
    for x in numbers:
       count= count * x
    return count
print(multiply(list))


def sum(numbers):
    count=0
    for i in numbers:
        count += i
    return count
print(sum(list))
"""


"""
def addition(n):
    return n + n

a=(4,5,6)


x= map(addition, a)
print(list(x))


def multiplication(n):
    return n*n

b=(1,2,3,4,5,6)

y= map(multiplication, b)
print(list(y))


def display(a,b):
  a=(1,2,3,4,5,6)
  b=(7,8,9,0)

  x=a+b
"""

"""
f=(1,2,3)

y =map(f,x)
print(list(y))
"""


"""

l=['abc','def','ghi','jkl']
b=[]
c=l+b
x=list(map(list,c))
print (x)
"""




"""

# Return double of n 
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 



x=list(map(int,input("enter multiple values:").split()))


n=int(input("enter a number:"))


for a in x:
    for b in x:
        if a+b==n:
            print(a,b)


"""
















"""
n=int(input("enter the number"))
for i in range(0,3):
    print("7"*n)
"""


n=int(input("tne number is"))
for i in range(1,n+1):
 print("x")
 for j in range(i,i+1):
  print("*",j)
'''
b='Hello World From Pankaj Hi There abc'
a= " ".join(b.split())
print (a)




v='HelloWorldFromPankaj HiThere'
h=v.replace(" ", "")
print(h)






string = '?????mkar and ayur?????'
  
print(string.strip('?')) 
  
string = 'www.omkarandmayur.org'
  
print(string.strip('.grow'))  
'''

'''
import re



a=' omkaar and mayur '
print(re.sub (r"^\s+", "", a), sep='')
print(re.sub (r"\s+$", "", a), sep='')  
'''

"""

import re


s = '  he is a good coder '

print(re.sub (r"\s+", "", s), sep='')  
print(re.sub (r"^\s+", "", s), sep='')  
print(re.sub (r"\s+$", "", s), sep='')  
print(re.sub (r"^\s+|\s+$", "", s), sep='') 

"""

"""
c=input("enter the character")

print("the ascii value of ",ord(c))



a=int(input("the number is"))

c=input("enter the character")

for i in range(1,11):
 print(c*a)

"""
"""a=int(input("the number is"))

for i in range (1,10):
 print("a",end="")
 for j in range (2,i+1):
  print("*",j)

"""
"""  

   return x / y  
# take input from the user  
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")  


"""
"""

def add(x,y):
    
 return x+y

def sub(x,y):
 return x-y

def mul(x,y):
 return x*y

def div(x,y)
 return x/y

print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

c=input("enter the choice(1/2/3/4):")

num1=int(input("enter first number"))

num2=int(input("enter second number"))


if c=='1':
    print(num1,"+",num2,"="add(num1,num2))

elif c=='2':
    print(num1,"-",num2,"=",sub(num1,num2))


elif c=='3':
    print(num1,"*",num2,"=",mul(num1,num2))

elif c=='4':
    print(num1,"/",num2,"="div(num1,num2))

else:
    print("invalid input")

    """


n=int(input("take a input "))
for i in range(1,n-1):
    for j in range(1,n+1):
      print(j,end="")
    print() 
    








'''
tuple =('rahul',10)
tuple1 =('om',20)
a=tuple+tuple1
print(a)

str='omkar sharad kulkarni'

print (str[0:2])
print(str[4])
print(str*2)


"""
def add(x,y):
    
 return x+y

def sub(x,y):
 return x-y

def mul(x,y):
 return x*y

def div(x,y):
 return x/y

print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.you want to continue")

c=input("enter the choice(1/2/3/4):")

num1=int(input("enter first number"))

num2=int(input("enter second number"))


if c=='1':
    print(num1,"+",num2,"=",add(num1,num2))

elif c=='2':
    print(num1,"-",num2,"=",sub(num1,num2))


elif c=='3':
    print(num1,"*",num2,"=",mul(num1,num2))

elif c=='4':
    print(num1,"/",num2,"=",div(num1,num2))

elif c=='5':
    print(c)
else:
    print("invalid input")

    
"""
    
a,b=0,1
while b<10:
print(b)    
 a,b=b,a+b


















a=20
b=10
c=print(a-b)


num = int(input("enter the number"))  
if num%2 == 0:  
    print("Number is even")
else:
    print("number is odd")


a=int(input("enter the number"));
b=int(input("enter the number"));
c=int(input("enter the number"));

if a>b and a>c:
  print("a is largest",a);
if b>c and b>a:
  print("b is largest",b);
else:
  print("c is largest",c);


marks=int(input("the marks are"))

if marks<5 and marks>2:
 print ("marks are in between 0-80")
  
else:
  print ("number")  
         



i=1
num=int(input("the numbers are"))
for i in range(0,10):
 print(i,end='')

'''

'''

n=int(input("Enter the number"))  
for i in range(0,100):  
    print(i,end = ' ')  

'''

''' 
num = int(input("Enter a number:"));  
for i in range(1,15):  
    print("%d X %d = %d"%(num,i,num*i));  

'''
'''
a= int(input("the number is"))

for i in range(0,a):
    print("#")

    for j in range(0,i+1):
     print("*$",end="")

     


n = int(input("Enter the number of rows you want to print?"))  
i,j=0,0  
for i in range(0,n):  
    print()  
    for j in range(0,i+1):  
        print("*",end="") 


'''
"""
n=int(input("the value"))

for i in range(0,n+1):
  for j in range(0,n+1):
      print(i,end="")
 
  print()



"""
'''
n=int(input("the value is"))

for i in range(0,n):
  print("*")
  for j in range(0,i+1):
     print("#",end="") 


'''

"""
n=int(input("the value is"))
for i in range(0,n+1):
   print("a")
   for j in range(i,n+1):
    print(i,end="")


"""

a=int(input("enter the value"))

'''

while i<=10:  
    print("%d X %d = %d \n"%(number,i,number*i));  
    i = i+1;  
'''
'''
while i<=10:
    print("%d x %d = %d \n"%(a,i,a*i))
    i= i+1
'''

'''
i=1
while i<=5:
    print(i)
    i=i+1
 break:
     print()

else:
    print("the while loop is exausted")
''''



i=1;  
while i<=10:    
    i=i+1;
    print(i);





'''
list=eval(input("the numbers in the list:"))
k=sorted(list,reverse=True)
print('Sorted list (in Descending):', k)

def mycmp(a, b):
    a, b = str(a), str(b)
    ab, ba = a + b, b + a
    if ab == ba:
        return 0
    if ab < ba:
        return -1
    return 1

for a in data:
    print ('In:', a)
    a.sort(cmp=mycmp, reverse=True)
    print ('Out:', a)
    
'''

'''
a=int(input("print the value"))
print (a)

i=eval(input("the numbers in the list:"))
d=sum(i)
'''

x = lambda a, b : a + b 
print(x(5, 6))

'''
if a==d and d<=a:
    print("heloo")

else:
    print("no match found")
'''































