class Country():
    name="";
    population=0;
    continent="";
    def __init__(self,newName):
        print("there is info about some country")
        self.name=newName;
    def info(self):
        print(self.name,self.population,self.continent);
    def cont(self):
        if (self.population>2000000):
            print("this is the country with a big population")
        else:
            print("it's small country")
country=Country("China");
country.population=3000000000;
country.continent="Asia";
country.cont();
country.info();
