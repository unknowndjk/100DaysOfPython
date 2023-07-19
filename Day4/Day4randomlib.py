import random

random_number = random.randint(1,10)
print(random_number)

random_float = random.random() * 5
print(random_float)

toss = random.randint(1,2)
if toss == 1:
  print("You won toss")
else:
  print("You lost toss")
