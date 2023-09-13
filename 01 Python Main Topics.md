#### <u>Python Variables :</u>

##### Python Data Types :

1. int 	: For integer numbers                                      ex :          x = 5
2. str     : For Strings                                                        ex :          x = "Mohamed Gouda"
3. float  : For float numbers                                           ex:           x = 5.20
4. bool  : For bool [True / False ]                                   ex:            x = False
5. list     : For list of values                                              ex:            x = [5 , 3 , 'Ahmed','Ali]      # Can be edited
6. tuple : For list of values                                              ex:            x = (5 , 4 , 6)      # Cant be edited
7. dict    : For list of values                                              ex:            x = { 1: 'Ahmed' , 2: 'Mohamed' }



#### <u>Python Operator :</u>

- Arithmetic operators

- Comparison operators

- Assignments operators

  

#### <u>Python Conditions  ( IF ) :</u>

- if

- If - elif - elif - elif - else

- if - and 

- if - or

- if not

- if  any

- if all

  

#### <u>Python loop :</u>

- for loop

  ```python
  for x in range (1,13) :
      for y in range (1,13):
          print (f'{x} * {y} = {x*y}')
          y += 1
      print ('=====================')
      x += 1
  ```

  ```python
  for x in 'python' :
      print(x)
  ```

  

- while loop

  ```python
  x = 1
  while x <= 12 :
      y = 1
      while y <= 12 :
          print (f'{x} * {y} = {x*y}')
          y += 1
      x += 1
      print ('===================')
  ```



#### <u>Python functions :</u>

```python
def mysum(x,y) :
    return x + y

print(mysum(10,5))

```

##### Some Important functions in python :

```python
name = 'Mohamed gouda'

print(name.upper())
print(name.lower())
print(name.title())
print(name.split(' '))
print(name.replace('gouda','Atalla'))
print(len(name))
print(len(name.replace(' ' ,'')))
```

##### Results :

```python
MOHAMED GOUDA
mohamed gouda
Mohamed Gouda
['Mohamed', 'gouda']
Mohamed Atalla
13
12
```

