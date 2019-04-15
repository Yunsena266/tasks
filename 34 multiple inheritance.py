class Shrek():
    def move(self):
        print("Shrek is walking")
class Fiona():
    def helptheFiona(self):
        print("Shrek is defending Fiona from the dragon")

class Lovers(Shrek,Fiona):
    pass;

aa=Lovers();
aa.move();
aa.helptheFiona();


