#print out a special number which is less than 100 or greater than 
#or equal to 300. and it is divisible by 3, 7 or both.




number  = 303

if (number < 100 or number >= 300) and (number % 3 == 0 or number % 7 ==0 ):
    print("special number")
else:
    print("not special number")

