#-------------------------------fibonacci_series--------------------------------------
#formula fro fibonacci series F(a)=F(a-1)+F(a-2)
#------------- using recursion -----------
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(6))    






