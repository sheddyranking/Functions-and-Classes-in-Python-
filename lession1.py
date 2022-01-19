#print out a special number if  less than 100 or greater than 
#or equal to 300. and it is divisible by 3, 7 or both.
#print out divisible by both if divisible by both  3 and 7
#print  out divible by 3 if divisible by only 3 not 7
#print out divisible by 7 if divisible by 7 not 3
#print out not "not special number"


number  = 303

if (number < 100 or number >= 300) and (number % 3 == 0 or number % 7 == 0 ):
    print("special numbr")
    if(number % 3 == 0 and number % 7 == 0):
        print("Divisible by both")
    #elif (number % 3 == 0):
    #    print("divisible by 3")
    #elif(number % 7 == 0):
        #print("Divisible by 7")
else:
    print("not special number")

