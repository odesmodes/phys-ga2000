from matplotlib import pyplot as plt
import numpy as np
import time

# Using the explicit method

def matrix_mult(N):
    start = time.time() # Starts calculating time 
    A = np.zeros([N,N]) # Double parantheses since np.ones is a function, also we are making matrices now to multiply with each other
    B = np.zeros((N,N)) 
    C = np.zeros((N,N), float) # Following the example 

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] = A[i,k] * B[k,j] # Doing matrix multiplication 
   
    end = time.time() # End calculating time
    return(end-start)

def matrix_mult_dot(N):
    start = time.time()
    A = np.zeros((N,N))
    B = np.zeros((N,N))
    C = np.dot(A,B)

    end = time.time()
    return(end-start)

matrix_size = range(10,100,10) # Making a range that the matrix N will go up to

discrete_list = [matrix_mult(i) for i in matrix_size] # Make a list of the time it takes to do the matrix_mult function as the size increases
#dot_list = [matrix_mult_dot(i) for i in matrix_size]

plt.scatter(matrix_size, discrete_list) # Make a scatter plot of above
#plt.scatter(matrix_size, dot_list)
plt.title('Matrix Multiplication Time as N increases: Explicit')
plt.xlabel('Matrix Size')
plt.ylabel('time')
#plt.show()
plt.savefig('Q1_explicit.png')

plt.figure(2)
matrix_size = range(10,1000,10)
dot_list = [matrix_mult_dot(i) for i in matrix_size]
plt.scatter(matrix_size, dot_list)
plt.title('Matrix Multiplication Time as N increases: Dot Function')
plt.xlabel('Matrix Size')
plt.ylabel('Time')
plt.savefig('Q1_dot.png')   
#plt.show()


 


