# There is the list of numbers. The programe should find
# the sum of the two neighbours for the every number.
list1=[int(i) for i in input().split()]
list2=[];
list2.append(list1[1]+list1[len(list1)-1])
for i in range(1,len(list1)-1):
    list2.append(list1[i-1]+list1[i+1])
list2.append(list1[len(list1)-2]+list1[0])
print(''.join([str(i)for i in list2]))