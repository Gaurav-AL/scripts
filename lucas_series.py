series = []
def lucas(n):
    a,b = 2,1
    series.append(a)
    series.append(b)
    for i in range(n):
        c  = a + b
        series.append(c)
        a,b = b,c
num = int(input("Enter range : "))
lucas(num)   
print(series)
