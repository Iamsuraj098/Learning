x = lambda x : x + 10
print(x(4))

x = lambda a, b : a * b
print(x(2, 3))

x = lambda b, c, d, a: a + b + c + d
print(x(1, 2, 3, 4))

def sum(a, b):
    return a+b

x = lambda a, b : sum(a, b)
print(x(1, 2))



def mul(b):
    return lambda a: a*b

mul1 = mul(2)
print(mul1(1))