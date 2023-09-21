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

def muli_table (x,y):
    for n in range(x,y) :
        print (x)

muli_table(1,10)
