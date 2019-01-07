import random

numbers = []

for i in range(1000):
  numbers.append(random.randint(1,100))
  
print(numbers)
total = sum(numbers)
print(total)

average = total / 1000
print(average)
print(round(average))
