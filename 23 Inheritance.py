class Animal():
    name="";
    def __init__(self,newName):
        name=newName;
        print(name,"is created")
    def eat(self):
        print("Nyam-nyam");
    def getName(self):
        print(self.name)
    def setName(self,NewName):
        self.name=NewName;
        print("The name was changes",self.name);
    def makenoice(self):
        print(self.name,"GRRRRR-RRR");
class Cat(Animal):
    def __init__(self,newName):
        Animal.__init__(self,newName);
Ala=Cat("Helen");

