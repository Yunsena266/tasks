#open the file in the net and define the frequency of the words
import urllib.request
from collections import defaultdict
url="http://dfedorov.spb.ru/python3/src/romeo.txt";
dictt=defaultdict(int);
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line=line.strip();
        for a in line:
            dictt[a]+=1;
print(dictt)