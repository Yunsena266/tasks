def typenumber(num):
    n=0;
    for i in range(2,99):
        if (num%i==0):
            n=n+1;
    if n==1:
        print("простое число")
    else:
        print("сложное число")
typenumber(11);


def calendar(day,month,year):
    days=range(31); months=range(12); years=range(2019);
    if (day in days) & (month in months) & (year in years):
        print("this data exists in calendar")
    else:
        print("sorry, doesn't exist");
calendar(30,12,2025);

