#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_v = float(input("Enter the bill value: "))
precentage = int(input("Enter the precentage tip would you like give ? 12 ,13 or 15: "))
people_n = int(input("How many people to split the bill? "))

tip = float(bill_v/people_n * ((precentage/100)+ 1))
tip_n = round(tip,2)
print(f"Tip value is {tip_n}")
