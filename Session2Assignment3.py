#-----------------------------------------------------------------
# Python - Session 2 Assignment 2
# Descr - Print format of Stars
#-----------------------------------------------------------------

#Enter the max number of stars to be printed
x=5

#First for loop to print the top half
for x in range(1,x):
    for y in range(1,x+1):
        print("*",end="")
    print("")

#Second for loop to print the top half
for x in range(x-1,0,-1):
    for y in range(1,x+1):
        print("*",end="")
    print("")