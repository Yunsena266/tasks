#find the equations which have solution. Enter the coefficient of equal.

a1=int(input()); a2=int(input()); b1=int(input()); b2=int(input()); c1=int(input()); c2=int(input());
n=0;
for x in range(a1,a2):
    for y in range (b1,b2):
        for z in range (c1,c2):
            D=y**2-4*x*z;
            if D>0:
                print("eqaul has sol with coeff: ",x,y,n);
            else:
                n=n+1;
                print(n);


