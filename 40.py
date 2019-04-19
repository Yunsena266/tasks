#1 task there are two lists. Create a third list which contains the elements that
#common in these two lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common=[];
for i in a:
    if (i in b) & (i not in common):
        common.append(i);
print(common);


#2 Ask the user for a string and print out whether this string is
# a palindrome or not. (A palindrome is a string that reads the same
# forwards and backwards.)
word=(input("Please, enter the word: ",))
b=[]; k=0;
for a in word:
    b.append(a);
long=len(b)//2;
for i in range(long):
    if (b[i]==b[-(i+1)]):
        k+=1;
    else:
        break
if k>0: print("string is a palindrome")
else: print("NO")
