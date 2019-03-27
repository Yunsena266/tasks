# define whether the year is bissextile
def define(year):
    if (year%4==0) & (year%400==0) & (year%100!=0):
        print("year is bissextile")
    else:
        print("no")
define(1700);



#count the number's category
num=int(input());
categ=0;
while (num!=0):
    num=num//10;
    categ=categ+1;
print("Answer is ",categ);

#you enter 2 numbers, define their the greatest common divisor
def nod(a,b):
    while (a!=0) & (b!=0):
        if a>b:
            a=a%b
        else:
            b=b%a;
    nod=a+b;
    print(nod);
nod(15,5);

