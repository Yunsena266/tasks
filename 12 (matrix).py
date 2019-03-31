# there is a square matrix. Find the composition of all the elements located below the main diagonal.
import random
matrix=[];
a=int(input("enter the size of square matrix",));
for i in range(a):
    row=[];
    for j in range(a):
        row.append(int(random.random()*10));
    matrix.append(row);
print(matrix)
sum=0;
for i in range(a):
    for j in range(a):
        if i>j:
            sum=sum+matrix[i][j];
print(sum)