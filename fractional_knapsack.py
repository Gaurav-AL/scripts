value = [int(x) for x in input("Enter the value of items :").split(" ")]
weight = [int(x) for x in input("Enter the weight of items :").split(" ")]
cap = int(input("Enter the knapsack Capcity :"))
ratio = {}
for i in range(len(weight)):
    ratio[i] = value[i]/weight[i]

maxweight,rem_weight,bias = 0,0,0
for k,v in sorted(ratio.items(), key=lambda x:x[1],reverse = True):
    print(weight[k])
    if(rem_weight + weight[k] <= cap):
        maxweight += value[k]
        rem_weight = rem_weight + weight[k]
    else:
        rem_weight = cap - rem_weight
        bias = v
maxweight +=  v * rem_weight
print(maxweight)
