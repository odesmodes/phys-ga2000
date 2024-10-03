import numpy as np
from matplotlib import pyplot as plt
from gaussxw import gaussxwab

x_range = np.linspace(0,5,100)
a_range = [2,3,4]

def integrand(x,a):
    return x**(a-1)*np.exp(-x)

#part A:
for a in a_range:
    res = []
    for x in x_range:
        res.append(integrand(x,a))
    plt.plot(x_range,res)
plt.savefig("Q2.png")
#plt.show()
#end part A

#part E
def integrand2(a,z):
    c = a - 1
    numerator=(c*z/(1-z))**(a-1)*np.exp(-c*z/(1-z))
    denominator = (1-z)**2
    return numerator/denominator 

def gamma(a):
    x,w = gaussxwab(N,0,1)

    s = 0
    for k in range(N):
        s+=w[k]*integrand2(a,x[k])
    return s * (a-1)

    
N = 50
a = 1

#part f:
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


print(gamma(3/2))
print("3=",gamma(3),",6=",gamma(6),",10=",gamma(10))
print("2!=" + str(fact(2)) + " ,5!=" + str(fact(5)) + " ,9!=" + str(fact(9))) 
