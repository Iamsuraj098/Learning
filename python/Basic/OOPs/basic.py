class hello:
    X = 4
    def wish(self):
        print("Hello")

a = hello()
a.wish()
print(a.X)

del a
