factors = [1]
x = int(input("Enter the number to find Factor :"))
if(x - x/2 == int(x/2)):
    factors.append(int(x/2))
for i in range(2,int(x/2)):
    if(x % i == 0):
        factors.append(i)
print(factors)
