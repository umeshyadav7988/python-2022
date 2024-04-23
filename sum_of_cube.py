def cube(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i*i)
    return sum

n=int(input("Enter a number : "))
print(cube(n))