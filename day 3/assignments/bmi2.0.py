weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

floatResult = float(weight/(height*height))
result = round(floatResult)

if result < 18.5:
  print(f"Your BMI is {result}, you are underweight.")
elif result < 25 :
  print(f"Your BMI is {result}, you have a normal weight.")
elif result < 30:
  print(f"Your BMI is {result}, you are slightly overweight.")
elif result < 35:
  print(f"Your BMI is {result}, you are obese.")
else:
  print(f"Your BMI is {result}, you are clinically obese.")

