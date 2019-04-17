schoolarchip=[0,2700,2500];

def doublemoney(roubles):
    return roubles*2;
newmoney=map(doublemoney,schoolarchip);
compare=zip(schoolarchip,newmoney);
for a in compare: print(a)