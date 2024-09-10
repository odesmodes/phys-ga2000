#  Part 1: Figure out how NumPy's 32-bit floating point representation represents the number 100.98763 in bits.

binary = '01000010110010011111100110101011' 

# Part 2: Calculate what that 32-bit number is and how much the actual number differs from its 32-bit floating point representation.

# Define the three parts of the representation (using formula off wikipedia)

sign = binary[0]
exponent = binary[1:9] # 1 to 9 since lists are indexed from zero
mantissa = binary[9:] # : nothing means go to the end

# Convert the bits into integers

sign_int = int(sign,2)  
exponent_int = int(exponent,2) - 127 # standard to subtract 127 (offset binary)

mantissa_int = 1 # start mantissa with leading one
pos = 1 # making a position counter to keep track of position in mantissa
for bit in mantissa:
    mantissa_int += int(bit)*2**(-pos) # from wikipedia
    pos += 1 # += set equal to previous value plus whatever is on the other side of the equal sign)

# Now we can combine it all together

float_calc = (-1)**sign_int * 2**exponent_int * mantissa_int

difference = -(float_calc - 100.98763)

print(float_calc)
print(difference)


