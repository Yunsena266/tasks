#from the file take the list of names, sort in alphabet and put into the new file
with open("zzz.txt") as file:
    list_names=file.readlines();
for name in reversed(list_names):
    print(name.strip());
name_list=sorted(list_names);
with open("zzz1.txt",'w') as output_file:
    for name in name_list:
        output_file.write(name);
