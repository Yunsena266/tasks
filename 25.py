#Use a function with uncertain numbers of input parameters
def func(*args):
    sum=0;
    for a in args:
        sum=sum+int(a);
    print(sum)
func(2,3,7,8,16,5,4)

# Write a function takes a gender info
def gender(gen="Unknown"):
    if gen=='m':
        gen="m"
        print("Your gender is ", gen)
    elif gen=="f":
        gen="f";
        print("Your gender is ", gen)
    else:
        print("Error!")
gender("ttt");
gender();



