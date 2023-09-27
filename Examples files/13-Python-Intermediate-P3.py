import datetime

today = datetime.date.today()
print(today)  #To print full date
print(today.day)    #To print day only of today
print(today.month)  #To print month only of today
print(today.year)   #To print year only of today

# To create date :
mydate = datetime.date(2008,10,4)
print (mydate)

# To add date :

week = datetime.timedelta(days=7)  # Use to add 7 days
add_hours = datetime.timedelta(hours=24) # Use to add hours

print(mydate + week)
print(mydate + add_hours)
