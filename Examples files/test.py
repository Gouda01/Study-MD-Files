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
