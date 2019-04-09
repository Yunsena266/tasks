#Downloading the cvs-file from internet
from urllib import request
url_file="https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1552114255&period2=1554792655&interval=1d&events=history&crumb=nhSVISfqgRw";
def download_file(cvs_url):
    get=request.urlopen(cvs_url);
    cvs=get.read();
    cvs_str=str(cvs);
    lines=cvs_str.split("\\n"); #split the rows of files
    file_cvs=r'goog.cvs';
    with open(file_cvs,"w") as file:
        for line in lines:
            file.write(line+"\n");
download_file(url_file);


