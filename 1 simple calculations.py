def ariphmetic(x,y,operation):
    if (operation=="+"):
        z=x+y;
    elif (operation == "-"):
        z = x - y;
    elif (operation == "*"):
        z = x *y;
    elif (operation == ":"):
        z = x /y;
    else:
        z='Unknown operation'
    print("result of operation: ",z);
ariphmetic(2,5,"we")


def square(a):
    s=a**2; perimetr=2*a; res=(s,perimetr);
    print("площадь и периметр",res);
square(2);


def seasontime(mth):
    mth=str(mth);
    if (mth=="1") or  (mth=='2')or (mth=="12"):
        print("winter");
    if (mth=="3") or  (mth=="4")or (mth=="5"):
        print("spring");
    if (mth == "6") or (mth == "7") or (mth == "8"):
        print("summer");
    if (mth=="9") or  (mth=="10")or (mth=="11"):
        print("autumn");
seasontime(2);

def bank(a,years):
    for i in range(years):
        a=a+a*0.1;
    print("contribution after"+str(years)+"years",a)
bank(20000,3);

