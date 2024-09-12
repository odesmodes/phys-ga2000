# Write a program to calculate and print the Madelung constant for sodium chloride. Use as large a value of L as you can, while still having your program run in reasonable time- say in a minute or less. Note that the physical constants drop out so you do not need to worry about them. Write two versions of the code, one which uses a for loop and one which does not. USe %timeit to determine which one is faster. 

import numpy as np

# VERSION ONE: WITH A FOR LOOP

# Step 1: Define potential V(i,j,k) 

def V(i,j,k):
    return  1 / (np.sqrt((i)**2 + (j)**2 +(k)**2))

L = 100

# First we loop through i j and k for the sum and then we have three cases to consider: if i+j+k is even then V is negative and if it is odd then V is positive so we can do if the remainder of dividing that total sum by two is zero then V is negative and vice versa, additionally we have to think about i j k equalling zero in which case we will just continue without doing anything to avoid inf error.

M = 0

for i in range (-L,L):
    for j in range (-L,L):
        for k in range (-L,L):
            if i==j==k==0:
                continue #continue on to the next loop without doing anything
            if (i+j+k)%2 == 0:
                M += -V(i,j,k)
            if (i+j+k)%2 != 0:
                M += +V(i,j,k)

print(M)


# VERSION TWO: WITHOUT A FOR LOOP
