from collections import defaultdict
arr = [int(x) for x in input("Enter array :").split(" ")]
k = int(input("Enter the K value :"))
lookup = defaultdict(int)
lookup[0] = 1
tsum,rem,total = 0,0,0
for x in range(len(arr)):
    tsum += arr[x]
    rem = tsum % k
    if(rem < 0):
        rem += k
    total += lookup[rem]
    lookup[rem] += 1

print(lookup,total)




