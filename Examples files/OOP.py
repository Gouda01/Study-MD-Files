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
