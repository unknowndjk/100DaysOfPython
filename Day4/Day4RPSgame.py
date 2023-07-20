import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

icon = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
]

print("Welcome to game..!")



for i in range(1,5,1):
  computer_p = random.randint(0, 2)
  user_p = input("Enter your position(R or P or S): ")
  if user_p == "r" or user_p == "s" or user_p == "p":
    if user_p == "r":
      your_p = 0
    elif user_p == "p":
      your_p = 1
    else:
      your_p = 2

    if computer_p == 0 and your_p == 0:
        mzg = "Match is draw"
    elif computer_p == 0 and your_p == 1:
        mzg = "You win"
    elif computer_p == 0 and your_p == 2:
        mzg = "Computer is win"
    elif computer_p == 1 and your_p == 0:
        mzg = "You win"
    elif computer_p == 1 and your_p == 1:
        mzg = "Match is draw"
    elif computer_p == 1 and your_p == 2:
        mzg = "Computer is win"
    elif computer_p == 2 and your_p == 0:
        mzg = "You win"
    elif computer_p == 2 and your_p == 1:
        mzg = "Computer is win"
    elif computer_p == 2 and your_p == 2:
        mzg = "Match is draw"
    else:
        mzg = "Enter correct position"
    
    print("your p is")
    print(icon[your_p])
    print("computer p is")
    print(icon[computer_p])
    print(mzg)
  else:
    print("Enter valid latter")
  print("---------------------------------------------------------------") 
  print("---------------------------------------------------------------") 
  print("---------------------------------------------------------------") 
