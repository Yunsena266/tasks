#Task1  Make a two-player Rock-Paper-Scissors game
player1=input("Your choice is : ",)
player2=input("Your choice is : ",)
if player1==player2:
    print("No one wins.Let's start a new game")
elif (player1=='scissors')& (player2=='rocks'):
    print("The 2nd player won")
elif (player2=='scissors')& (player1=='rocks'):
    print("The 1st player won")
elif (player2=='paper')& (player1=='rocks'):
    print("The 2nd player won")
elif (player1 == 'paper') & (player2 == 'rocks'):
    print("The 1st player won")
elif (player2 == 'paper') & (player1 == 'scissors'):
    print("The 1st player won")
elif (player1 == 'paper') & (player2 == 'scissors'):
    print("The 2nd player won")


#Task2  Write a program (function!) that takes a list
# and returns a new list that contains all the elements of the
# first list minus all the duplicates.
new_list=[];
def newlist(_list):
    for a in _list:
        if a not in new_list:
            new_list.append(a);
    print(new_list)
newlist([1,4,7,7,3,2,6,]);