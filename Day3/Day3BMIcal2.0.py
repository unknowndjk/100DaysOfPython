height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = (weight / (height * height))

if weight < 18.5:
    mzg = "you are slightly overweight."
else:
    if bmi > 18.5 and bmi < 25:
        mzg = "you have a normal weight."  
    else:
        if bmi > 25 and bmi < 30:
            mzg = "you are slightly overweight."
        else:
            if bmi > 30 and bmi < 35:
                mzg = "you are obese."
            else:
                mzg = "you are clinically obese."                  

bmi_n = round(bmi)

print(f"Your BMI is {bmi_n}, {mzg}")                 
