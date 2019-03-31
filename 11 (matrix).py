#There is a matrix, find the row containing the biggest number of equal elements.
import random
from collections import Counter
matrix=[];
N=4; M=4;
for i in range(N):
    row=[];
    for j in range(N):
        row.append(int(random.random()*10));
    matrix.append(row);
print(matrix)
val=[];
for row in matrix:
    c=Counter(row);
    val.append((max(c.items(),key=lambda k: k[1])));
maxx=0;
for i in range(len(val)):
    if (val[i][1])>maxx:
        maxx=val[i][1];
        maxnum=i;
print("The number of row: ",maxnum);