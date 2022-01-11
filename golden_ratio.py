import math
golden_ratio = (1 + math.sqrt(5))/2
series = [math.ceil(golden_ratio)]
def serie(n):
    for x  in range(2,n):
        series.append(math.ceil(golden_ratio ** x))
num = int(input("Enter range :"))
serie(num)
print(series)
#not perfect for finding prime number