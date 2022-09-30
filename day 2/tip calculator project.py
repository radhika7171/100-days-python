print("Welcome to the tip calculator")
totalBill = float(input("What was the total bill ? \n"))
tip = int(input("What percentage tip would you like to give ? 10, 12 or 15 ? \n"))
splitBillInPeople =int(input("How many people to split the bill ?\n"))

billWithTip = ((totalBill *tip)/100) + totalBill
finalAmount = round((billWithTip/splitBillInPeople),2)

print(f"Each perosn should pay : {finalAmount}")

