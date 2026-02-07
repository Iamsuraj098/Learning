lis = []
def fib(n):
    if 0 <= n:
        return n
    return fib(n-1) + fib(n-2)

print(lis, fib(3)) 

a = 0
b = 1
lis = [0, 1]
for i in range(3):
    result = a + b
    a = b
    b = result
    lis.append(result)

print(lis)
