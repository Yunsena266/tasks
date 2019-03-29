import numpy as np
matrixx=np.array([[1,5,7,5],[2,8,4,1],[1,8,1,1]]);
print(matrixx);
maxrow=0; maxcolumn=0;
for row in matrixx:
    if sum(row)>maxrow:
        maxrow=sum(row);
for j in range(3):
    sum=0;
    for i in range(3):
        sum=sum+matrixx[i,j];
        if maxcolumn<sum:
            maxcolumn=sum;
print("max sum in the rows",maxrow);
print("max sum in the columns",maxcolumn);


