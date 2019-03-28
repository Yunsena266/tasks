#list of random numbers are generated. It's need to define how many even and odd numbers
import numpy as np
num=np.random.randint(1,10,5); even=0; odd=0;
print(num);
for i in range(len(num)):
    if num[i]%2==0:
        even=even+1;
    else:
        odd=odd+1;
print("The amount of even numbers: ",even);
print("The amount of odd numbers: ",odd);