arr = [int(x) for x in input("Enter array :").split(" ")]
k = int(input("Enter the K value :"))
lookup = {}
tsum = 0
for x in range(len(arr)):
    tsum += arr[x]
    lookup[x] = tsum%k
count = 0
lis = []
key = 0
for k,v in lookup.items():
    if(v == 0):
        count += 1
        continue
    if(v in lis):
        key = lis.index(v)
        print(lis)
        if(abs(k - key) > 1):
            count += 1
    lis.append(v)
print(count,lis)

