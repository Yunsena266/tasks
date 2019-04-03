import re
with open("svetaeva.txt",'w') as outputfile:
     outputfile.write("Тихий вечер. Ветры кротко стихли");
with open("svetaeva.txt",'r') as file:
    data=file.read();
    result=re.search(r'дом', data);
print(result)