#### try  ...... except :

```python
try :
    age = int(input('Enter your Age : '))
    print(age / 20)
except ValueError:
    print('Enter number please')
except ZeroDivisionError :
    print('Enter number > 0 please')
```



##### If i want it return the error type and print it :

```python
try :
    age = int(input('Enter your Age : '))
    print(age / 20)
except ValueError as e:
    print('Enter number please')
    print (e)
except ZeroDivisionError as e:
    print('Enter number please')
    print (e)
```



##### Or we can use many except in group :

```python
try :
    age = int(input('Enter your Age : '))
    print(age / 20)
except (ValueError,ZeroDivisionError):
    print('Enter number please')

```



##### If i want to make except to all problems :

```python
try :
    age = int(input('Enter your Age : '))
    print(age / 20)
except Exception :
    print('Enter number please')

```

##### try  .... except .... else .... finally



<u>**try**:</u>

**<u>except</u>**: do this code if try make error

**<u>else</u>** : do this code with try if it happen

**<u>Finally</u>** : do this code always



