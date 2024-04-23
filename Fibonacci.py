def fibonaci(n):
    if n<=0 :
        print("Incorrect input")
    elif (n==1):
        return 0
    elif (n==2):
        return 1
    else : 
        return  fibonaci(n-1) + fibonaci(n-2)

n = int(input("Enter a number : "))
if (fibonaci(n)==True):
    print("Given number is fibonaci")
else :
    print("Given number is not fibonaci")
