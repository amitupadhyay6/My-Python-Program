from itertools import combinations
#len of the list
n = int(input())
# Enter lower letters with space
lis = input().strip().split()[:n]
# number of the comvination
k = int(input())
templis = list(combinations(lis,k))
j =0
for i in range(len(templis)):
    if "a" in templis[i]:
        j += 1
percentage = (j/len(templis))* 100
print(percentage)



