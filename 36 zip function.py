#1 Connect two lists by using function zip
list1=["Russia","China","Yakutia"];
list2=["russian","chinese","yakutian"];
languages=zip(list1,list2);
for a in languages:
    print(a);

#2lambda function
answer=lambda x: x+2;
print(answer(6));

#3 Find the min and max of dictionary by using zip

my_dict={'Vera':157, 'Maria': 176, 'Yulia': 145 };
print("The shortest girl",min(zip(my_dict.values(),my_dict.keys())));


