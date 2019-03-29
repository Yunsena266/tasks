#sort the positive and negative numbers into 2 lists
import numpy as np
lista=np.random.randint(-100,100,10); pos=[];neg=[];
for a in lista:
    if a>0:
        pos.append(a);
    else:
        neg.append(a);
print("Positive group",pos)
print("Negative group",neg)



#there is the list of integer numbers. Replace the positive numbers by 1, negative by -1. Don't change 0.
listt=np.random.randint(-5,5,5);
print(listt);
for i in range(len(listt)):
    if (listt[i]>0) & (listt[i]!=0):
        listt[i]=1;
    elif (listt[i]<0) & (listt[i]!=0):
        listt[i]=-1;
print(listt);


