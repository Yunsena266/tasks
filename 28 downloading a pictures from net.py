import random
import urllib.request

def download_image(url):
    name=random.randrange(0,100);
    full_name=str(name)+".jpg";
    urllib.request.urlretrieve(url,full_name); #show where is the picture
download_image("https://cdn.bitrix24.ru/b8244759/landing/8c9/8c9d42ade58f9bd72cb600a15ad62642/python_logo_notextsvg_mq7wlht.png");

