class cakes():
    amount=5;
    def __init__(self,price,name):
        self.price=price;
        self.name=name;
        print("You have bought",name," for the",price, "dollars each");
    def eat(self):
        self.amount-=1;
    def buy(self):
        self.amount+=1;

pinkcakes=cakes(2, 'donuts');
donuts=cakes(3, 'biscuits');
pinkcakes.eat();







