from PIL import Image
Makasa=Image.open("Mikasa.jpg");
print(Makasa.size, Makasa.format);

area=(100,100, 400, 400);
cropped_Makasa=Makasa.crop(area);
Makasa.show();
cropped_Makasa.show();

