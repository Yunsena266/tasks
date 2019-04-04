import urllib.request
import re
url="http://humanresearch.jsc.nasa.gov/elements/smo/dosc/IRP_HRP-47065.pdf";
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line=line.strip();
        for a in line:
            res=re.findall('Nasa',a);
print(res)
