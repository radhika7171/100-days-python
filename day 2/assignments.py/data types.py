#data type
#subscripting
#type casting


from lib2to3.pgen2.tokenize import TokenError


two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))
num_1= int(two_digit_number[0])
num_2= int(two_digit_number[1])
result = num_1+num_2

print(result)