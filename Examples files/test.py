'''
odd_numbers =[]
even_numbers = []

def odd_even (x,y) :
    for n in range(x,y) :
        if n%2 == 0 :
            odd_numbers.append(n)
        elif n%2 != 0 :
            even_numbers.append(n)

    print(f'Odd Number = {odd_numbers}')
    print(f'Even Number = {even_numbers}')

odd_even (100,200)
'''

'''
def divided_numbers (x,y) :
    for n in range (1,101) :
        if n%x ==0 and n%y ==0 :
            print (n)
        
divided_numbers(5,6)
'''

'''
def muli_table (x,y):
    for n in range(x,y) :
        print (x)

muli_table(1,10)
'''

'''

names = ['ahmed','ali','mahmoud','aid','hassan']

# Normal List :
new_names = []
for x in names :
    new_names.append(x.upper())

# List Comprehension

new_names1 = [x.upper() for x in names]
new_names2 = [x.upper() for x in names if len(x) > 3]
new_names3 = [x.upper() if len(x) > 3 else '.............' for x in names]



print(new_names)
print(new_names1)
print(new_names2)
print(new_names3)

'''

'''

class StudentDetails :
    def add_student (self,name):
        self.mark = []
        print(f'Welcome {name}')

    def add_mark(self,mark) :
        self.mark.append(mark)
        print(self.mark)

    def mark_avg (self):
        mark_avg = sum(self.mark) / len(self.mark)
        print(mark_avg)

s1 = StudentDetails()
s1.add_student('Mohamed')
s1.add_mark (20)
s1.add_mark (30)
s1.add_mark (50)
s1.mark_avg()
'''

'''
class Bank :
    def __init__(self,name,age) :
        print(f'Welcome {name}')
        self.name = name
        self.age = age
        self.balance = 0
    
    def deposite (self,amount) :
        self.balance += amount
        print(f'The deposite done successful and your balance is : {self.balance}')
    
    def withdraw (self,amount) :
        if self.balance >= amount :
            self.balance -= amount
            print(f'The withdraw done successful and your balance is : {self.balance}')
        else :
            print('The withdraw not done because your balance not allow')
    
    def show_details (self):
        print(f
    Customer Name       : {self.name}
    Customer age        : {self.age}
    Customer balance    : {self.balance}

#)


c1 = Bank('Mohamed',21)
c1.deposite(5000)
c1.deposite(10000)
c1.withdraw(7000)
c1.show_details()

'''

'''
class Customers :
    def __init__(self,name,age) :
        print(f'Welcome {name}')
        self.name = name
        self.age = age
        

    def show_details (self):
        print(f#
    Customer Name       : {self.name}
    Customer age        : {self.age}
    Customer balance    : {self.balance}

#)



class Bank(Customers) :

    def __init__(self,name,age) :
        super().__init__(name,age)
        self.balance = 0

    def deposite (self,amount) :
        self.balance += amount
        print(f'The deposite done successful and your balance is : {self.balance}')
    
    def withdraw (self,amount) :
        if self.balance >= amount :
            self.balance -= amount
            print(f'The withdraw done successful and your balance is : {self.balance}')
        else :
            print('The withdraw not done because your balance not allow')



c1 = Bank('Mohamed',21)
c1.deposite(5000)
c1.deposite(10000)
c1.withdraw(7000)
c1.show_details()

'''


class Game :
    def __init__(self):
        while True :
            print('''
    Welcome to our Game please Choose the game number :
            1 - No Dublicate sentence 
            2 - Numbers
            3 - Exit the Game
            ''')
            while True :
                user_choice = int(input('Enter Game Number : '))
                if user_choice in range (1,4):
                    break
                else :
                    print ('Please Enter number between 1 to 3')

            
            if user_choice == 1 :
                self.no_deplicate_sentence()
            elif user_choice == 2 :
                self.my_numbers()
            elif user_choice == 3 :
                print('Goodbye ...... ')
                break

            play_again = input('Press any key to play again or press n to Exit : ')
            if play_again == 'n' :
                print('Goodbye ...... ')
                break

                
            
    def no_deplicate_sentence (self) :
        sentence = input('Enter your sentence : ')
        words = sentence.split(' ')
        new_words = []
        for x in words :
            if x not in new_words :
                new_words.append(x)
        new_sentence = " ".join(new_words)
        print(new_sentence)

    def my_numbers (self):
        first_number = int(input('Enter your first number : '))
        second_number = int(input('Enter your second number : '))

        for x in range (1,101) :
            if x % first_number == 0 and x % second_number == 0 :
                print(x)


s1 = Game()