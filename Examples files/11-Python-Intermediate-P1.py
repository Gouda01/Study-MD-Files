names = ['ahmed','ali','mahmoud','aid','hassan']
new_names = []

# Normal Loop :

for x in names :
    new_names.append(x.upper())

print(new_names)

# List Comprehension :

new_names2 = [x.upper() for x in names]
new_names3 = [x.upper() for x in names if len(x)>3]
new_names4 = [x.upper() if len(x)>3 else '.....' for x in names]

print(new_names2)
print(new_names3)
print(new_names4)



# Dictionary  : 

employee = {'Mohamed':5000 , 'Ahmed':6000 ,'Ali':7000}
new_employee = {}
# Normal Loop :
for (k,v) in employee.items() :
    n = v * 1.25
    new_employee[k] = n

# Dictionary Comprehension : 

new_employee1 = {k:v*1.25 for (k,v) in employee.items()}

print(new_employee)
print(new_employee1)


# Tuple -> Generator :

customers = ['ahmed','ali','mahmoud','aid','hassan']
new_customers = (x.upper() for x in customers)

print(list(new_customers))

# Functional Programing :

def wordupper(n):
    return n.upper()

def wordlength(n):
    if len(n)>3 :
        return n.upper()

result = map(wordupper,customers)
result1 = filter(wordlength,customers)

print(list(result))
print(list(result1))


from functools import reduce

numbers = list(range(1,100))
def mysum  (x,y):
    return x + y

result2 = reduce(mysum,numbers)
print(result2)




