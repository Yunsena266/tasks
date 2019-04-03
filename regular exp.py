#return the first word in the row
import re
sen='Trust only yourself';
res=re.findall(r'^\w+',sen);
print(res)



#return the first two symbols of every word in sentence
senn="One life - one chance";
res=re.findall(r'\b\w.',senn);
print(res);

