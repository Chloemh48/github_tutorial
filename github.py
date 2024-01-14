# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return (fib(n-1) + fib(n-2))

# n = 10
# for i in range(1, n+1):
#     print(n,":" , fib(i) )

def sum(n):
    if n == 0:
        return n
    else:
        return n+sum(n-1)

print('The sum is:',sum(5))
    


