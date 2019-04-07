class Pets():
    paws=0
    def out(self):
        print (self.paws)
class Cats(Pets):
    def __init__(self):
        self.paws=4
    def lt(self):
        self.name=cat
        print(self.name)
        
class Snakes(Pets):
    def __init__(self):
        self.paws=0
    def lt(self):
        self.name=snake
        print(self.name)
        
class chikens(Pets):
    def __init__(self):
        self.paws=2
    def lt(self):
        self.name=chiken
        print(self.name)


        
s=Cats()
k=Snakes()
b=chikens()

s.out()
k.out()
b.out()
s.lt()
k.lt()
b.lt()
