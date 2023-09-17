'''
class Calculator :
    def __init__(self,name):
        print(f"Welcome {name}")

    def sum(self,x,y):
        return x + y

    def mul (self,x,y):
        return x * y


class SciCalc (Calculator):
    

    def power (self,x,y):
        return x ** y
    


s1 = SciCalc('Mohamed')
print(s1.sum(5,6))
print(s1.mul(5,6))
print(s1.power(4,2))

'''





'''
- Create Student
- Add mark
- Get Marks Avg.
'''
'''
class Students ():
    def __init__(self,name):
        print(f'Welcome {name}')
        self.marks = []

    def add_mark(self,x):
        self.marks.append (x)
        print (self.marks)
    def marks_agv(self):
        avg = sum(self.marks)/len(self.marks)
        print(avg)

s1 = Students('Mohamed')
s1.add_mark(100)
s1.add_mark(200)
s1.add_mark(300)
s1.marks_agv()

s2 = Students('Ahmed')
s2.add_mark(50)
s2.add_mark(70)
s2.add_mark(90)
s2.marks_agv()

'''
class BankCustomers :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f'Welcome {self.name}')

    def show_details (self):
        print(f'Customer Name\t\t:  {self.name}')
        print(f'Customer Age\t\t:  {self.age}')
        print (f'Customer Balance\t: {self.balance}')


class Bank (BankCustomers):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.balance = 0
        
    def desposite (self,amount):
        self.balance += amount
        print(self.balance)

    def withdraw (self,amount) :
        if amount > self.balance :
            print('Sorry your Balance not allow try again other amount')
            return

        self.balance -= amount
        print(self.balance)
        self.show_details()

    

C1 = Bank('Mohamed','35')
C1.desposite(5000)
C1.desposite(10000)
C1.withdraw(7000)
print('===========================')
C1.show_details()

