import threading

class Massenger(threading.Thread):
    def run(self):
        for _ in range(5):
            print(threading.currentThread().getName());
x=Massenger(name="Send out massenger");
y=Massenger(name="Recieve the massenger");
x.start()
y.start()




def square(num):
    print(threading.currentThread().getName());
    print(num*num);
if __name__=='__main__':
    for i in range(10):
        mythread=threading.Thread(target=square,args=(i,))
        mythread.start()



