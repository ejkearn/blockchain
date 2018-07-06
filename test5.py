import random
import datetime

num1 = random.random()
num2 = random.randint(1,10)
thedate = datetime.date(random.randint(1,3000), random.randint(1,12), random.randint(1,28))

print(num1)
print(num2)
print(thedate)