# # Subscripting- pulling out element from string
# print("Hello"[0])

# # string concatination (double quotes - string + act as string concatination "jda 29839")
# print("123"+"456")

# #Integer
# #data manipulation Integer (without double quotes -  Integer  + act as addition operator )
# print(123+345)
#  #large integer 
# print(123,234,222) # (,) - add space
# print(123_234_222) # (_) - readable without space

# #Float
# 233.48
#  #Boolean
# print(True)
# print(False)

#type error, check, casting
# a = 234
# print(type(a))
# #print("70" + int("233")) # tyoe error - cant add/ concatenate str and int
# print(70 + int("233")) 
# print(str(70) + str(233)) 


#mathematical operators
# 3+2
# 3-1
# 3*7
# (6/3)  # return floats
# print(2**3) # exponential , 2 to the power 3 , returns (2*2*2 = 8)

#PEMDASLR (l= left R= Right)
# ()
# **
# * / (equal importance, but calculation left to right)
# + -

#print(3*3+3/3-3)
# 9+3/3-3
# 9+1.0-3
# 10-3
# 7
#print(3*(3+3)/3-3)  #priority () --isolation the calculation using brackets
#(3*(6)/3-3) 
#(18/3-3) 
#(6-3) 
#3

#round upto number of digits

# print(round(8/4, 6)) # with single (/) --float
# # // converts float division into integer
# print((8//3)) ## with double (//) --int

# print(type(8//3)) #int

#short hands
score =4
score +=1 # score = score +!
score /=2 #5/2
height = 1.9
isWinning = True
# print(score)


#print("your score is"+ score) # type error (only same data types are concatenated)
# print("your score is "+ str(score)+", " +str(height)+", "+ str(isWinning))

#pythonic way -- f-string
#put everything in f-string function, automatic type conversion
#consider everything as a string,except {variables in curly braces}
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
name = "radhika"
print("hello"+name)

