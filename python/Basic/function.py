# functions
def hello():
    print("Helle World")

hello()

def maker(name):
    print(name , " Kumar")

maker("Kite")


def list1(lis2):
    for i in lis2:
        print("-", i, end=" ")
    
list1([1, 2, 3, 4, 5, 6])

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments

def help(*, hello):
    print(hello)

help(hello = "hello")
# help("hello") here got the error because in function definition before argument astrik used so we must to used the argument during calling the function.

# Positional-Only Arguments
# it only create the postional argument in simple word we must match the position of the argument

def pos_arg(a, b, c, /):
    print(a, b, c)

pos_arg(1, 3, 4)


# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.

# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)



# What is *args?
# the *args parameters allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple containing all the passed arguments:

def my_fun(*args):
    print("Hello: ", args[0])
    print("Hello: ", args[1])
    print("Hello: ", args[2])
    print("Hello: ", args[3])
    print("Hello: ", args[4])

my_fun(1, 2, 3, 4, 5)

# we can combine the *args with Regular Arguments

def my_fun(x, *u):
    print(x, u)

my_fun(1, 2, 3, 4, 5)

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

def my_func(**kwargs):
    print(kwargs["name"], " ", kwargs["age"])

my_func(name="Rahul", age=33)

# Unpacking Dictionaries with **
# if u have keyword  arguments stored in a dictonary, you can as ** inpack them.



# Decorators
# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

# Multiple Decorator Calls
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())



# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
# Example
# Normally, a function's name can be returned with the __name__ attribute:

# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)

print(myfunction.__name__)
