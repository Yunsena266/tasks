#create the class describing the student
class Student():
    age=0;
    name="";
    money=0;
    def poor(self):
        print(self.name,"умирает от голода");
stud=Student()
stud.name="Sasha";
stud.money=0;
stud.poor();
