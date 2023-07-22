#Password Generator Project
import random
import secrets

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passw = "";
for x in range(0,nr_letters,1):
  r_num = random.randint(0,23)
  r_latter = letters[r_num]
  passw += r_latter 

for x in range(0,nr_symbols,1):
  r_num = random.randint(0,9)
  r_symbole = symbols[nr_symbols]
  passw += r_symbole

for x in range(0,nr_numbers,1):
  r_num = random.randint(0,9)
  r_number = numbers[r_num]
  passw += r_number 

passlist = []
for x in passw:
  passlist += x

random.shuffle(passlist)
newpassword = ""
for x in passlist:
  newpassword += x
  
print(f"Your Normal password is: {passw}")

print(f"New password is: {newpassword}")
