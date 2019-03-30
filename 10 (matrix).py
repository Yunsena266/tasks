#There is a matrix of integer numbers. Number is entered. Define, which rows and columns contains this number.
import numpy as np
import random
N=int(input()); M=int(input());
matrixx=[];
for i in range(N):
    row=[];
    for j in range(M):
        row.append(int(random.random()*10))
    matrixx.append(row)
print(matrixx); l=0;
number=int(input());
for row in matrixx:
    for i in range(N):
        if row[i]==number:
            print("number of row and column containing the number",l,i);
    l=l+1;
