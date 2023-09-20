'''
If in
If Any
If not
If all
'''

# If in
names = ['Ahmed','Mohamed','Ali','Hany']
your_name = input('Enter your name : ')

if your_name in names :
    print(f'Welcome {your_name}')
    x = float(input('Enter Your Mark : '))

    if x > 100 :
        print('Mark not allow to be more than 100 Try again')
    elif x >= 50 :
        if x >= 90 :
            print('Your Grade is : Excellent')
        elif x >= 75 :
            print('Your Grade is : Very good')
        elif x >= 60 :
            print('Your Grade is : Good')
        else :
            print('Your Grade is : Pass')
    elif x < 50 and x >=0 :
        print('Not Pass and Good luck next year')
    else :
        print('Please input right value')
else :
    print ('Try again')

#If Not
if your_name not in names :
    print ('Not allowed')


m = 10
n = 15
o = 16

if all([m==10 , n==15 , o==16]) :
    print('Good All')

if any([m==12 , n==10 , o==16]):
    print('Good Any')
    







