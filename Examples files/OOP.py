class Calculator :
    def __init__(self,name):
        print(f"Welcome {name}")

    def sum(self,x,y):
        return x + y

    def mul (self,x,y):
        return x * y


s1 = Calculator('Mohamed')
print(s1.sum(5,6))
print(s1.mul(5,6))
