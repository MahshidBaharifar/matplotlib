import matplotlib.pyplot as plt
import math
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
x_axis=[1,2,3,4]


y1_axis=[factorial(item) for item in x_axis]
plt.plot(x_axis,y1_axis,color='b',label='n!',linestyle='solid')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

y2_axis=[item for item in x_axis]
plt.plot(x_axis,y2_axis,color='g',label='x',linestyle='solid')
plt.legend()

y3_axis=[math.log2(item) for item in x_axis if item!=0]
plt.plot(x_axis,y3_axis,color='r',label='log2(x)',linestyle='solid' )
plt.legend()



y4_axis=[item^2 for item in x_axis]
plt.plot(x_axis,y4_axis,color='y',label='x^2',linestyle='solid')
plt.legend()


y5_axis=[item*math.log2(item) for item in x_axis]
plt.plot(x_axis,y5_axis,color='c',label='xlog2(x)',linestyle='solid')
plt.legend()


y6_axis=[math.exp(item) for item in x_axis]
plt.plot(x_axis,y6_axis,color='m',label='exp(x)',linestyle='solid')
plt.legend()
plt.show()