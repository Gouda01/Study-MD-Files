'''
try :
    age = int(input('Enter your Age : '))
    print(age / 20)
except ValueError:
    print('Enter number please')

try :
    age = int(input('Enter your Age : '))
    print(age / 20)
except ValueError as e:
    print('Enter number please')
    print (e)
except ZeroDivisionError as e:
    print('Enter number > 0 please')
    print (e)

# Or we can use many except in group :

try :
    age = int(input('Enter your Age : '))
    print(age / 20)
except (ValueError,ZeroDivisionError):
    print('Enter number please')

# If i want to make except to all problems :

try :
    age = int(input('Enter your Age : '))
    print(age / 20)
except Exception:
    print('Enter number please')


'''
'''
file = open('test.txt','r')
#print(file.readlines())

data = file.readlines()
for x in data :
    print (x)
'''

'''
file = open('test.txt','w')
file.write('\nWelcome to out file')
file.close()
'''

'''
file = open('test.txt','a')
file.write('\nWelcome to out file')
file.close()

'''

# We can use it without close :
with open('test.txt','a') as file :
    file.write('\nWelcome With open')





