name = input("imput your name: ")
age = input("input your age: ")

def nameAge(name, age):
  print(name +" "+ age)

def printTwo(one, two):
  print(one + two)

def decades(age):
  return(int(age)//10)

nameAge(name, age)
printTwo(name, age)
print decades(age)