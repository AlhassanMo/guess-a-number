x = input("please think of a number between 0 and 100") # (input can be replaced with print)
low = 0
high = 100
ans = (high + low)/2
y = 0
while y != "c":
    ans = (high + low)/2
    print ("is the number =" + str(round(ans))+"?")
    y = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if y == "l" :
        low = ans
    elif  y == "h" :
        high = ans 
        ans = (high + low)/2
    else :
        print("Sorry, I did not understand your input.")
if y == "c" :
    print ("the number is " + str(round(ans)))  
    
    # the user gusses a number and the computer will discover it !
    # Bisection search 
    # i use round() to remove fractions
