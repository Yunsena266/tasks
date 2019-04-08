def calculator_health(age=0,vegetables_in_day=0, smoking="unknown"):
    if smoking=="no":
        print(age*vegetables_in_day/1000);
    elif smoking=="yes":
        print((age*vegetables_in_day*0.7)/1000);
    else:
        print("Incorrect info")
calculator_health(21,5,"no");
anna_datas=[30,10,"yes"];
calculator_health(*anna_datas)




