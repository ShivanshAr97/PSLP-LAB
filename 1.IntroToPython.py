print("Hello")

name=input("Enter name")
print("Hello", name)

x=int(input("Enter no. 1"))
y=int(input("Enter no. 2"))
z=x+y
print(x+y)

y=[1,3,4,5,6]
print(y)
print(*y)
print(*y, sep=", ")

for x in range(1,10,2):
  print (x)

i=1
while i<6:
  print (i)
  i=i+1

x=5
if(x<40):
  print ("Fail")
elif(x>=75):
  print("Distinction")
else:
  print("Pass")

def greet(name):
  print("Hello "+name)
  
greet("Shivansh")