#create a class StringVar for work with string type of datas,
# including methods set() and get(). get() - for getting the contents
# of the lines, set()- for changing the line.
class StringVar():
    sen="";
    def set(self,newSen):
        self.sen=newSen;
        print("The sentence is changed",self.sen)
    def get(self):
        print(self.sen);
obj=StringVar();
obj.sen="Pythoon";
obj.get();
obj.set("YES")

