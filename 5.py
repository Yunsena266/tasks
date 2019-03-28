#find the longest word in the proposition

prop=input("enter the proposition: ",);
propp=prop.split(); idlong=0;
for i in range(1,len(propp)):
    if (len(propp[i]))>len(propp[idlong]):
        idlong=i;
print(propp[idlong]);




