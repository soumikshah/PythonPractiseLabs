def fib(n):
    """Print a Fibonacci Series upto n."""
    a,b = 0,1
    while b<n:
        print b,
        a,b = b, a+b

def fib2(n): #return Fib series upto n
    """Return a list containing the fibonacci series upto n"""
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b = b,a+b
    return result


fib(200)
f100 = fib2(100) #call it
print f100 #Write the result
print fib2(5)