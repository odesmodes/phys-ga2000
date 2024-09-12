# Demonstrate using examples that 32-bit is less precise and smaller dynamic range than 64-bit.

# Part 1: Find approximately the smallest value you can add to 1, and get an answer that is different than 1, in both 32-bit and 64-bit precision. 

# Strategy: add a really tiny number to 1 then if that number is still equal to 1 (in the computer's eyes) we keep going until the number is not equal to one
import numpy as np

limit_32bit = 100000000000

for i in range(0, limit_32bit):
    smol = np.float32(i/limit_32bit)

    if np.float32(1) + smol != np.float32(1):
        print(np.float32(1) + smol)
        break

limit_64bit = 100000000000000000

for i in range(0,limit_64bit):
    tiny = np.float64(i/limit_64bit)

    if np.float64(1) + tiny != np.float64(1):
        print(np.float64(1) + tiny)
        break

# Part 2: Approximately find the minimum and maximum positive numbers that these two types can represent with an underflow or overflow.

print(np.finfo(np.float32).max) #finfo is machine limits for floating types
print(np.finfo(np.float32).tiny) #tiny is the smallest possible positive number
print(np.finfo(np.float64).max)
print(np.finfo(np.float64).tiny)
