class Students :
    def __init__(self,name):
        print(f'Welcome {name}')
        self.marks = []
    def add_mark (self,mark):
        self.marks.append(mark)
        print (self.marks)
    def get_avg (self):
        print(sum(self.marks)/len(self.marks))

    
        
    
S1 = Students('Ahmed')
S1.add_mark(100)
S1.add_mark(120)
S1.add_mark(110)
S1.add_mark(130)
S1.get_avg()



