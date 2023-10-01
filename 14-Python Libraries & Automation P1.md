#### Date And times in Python :

```python
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
```



#### Files And Folders in Python :

```python
import os
# To Create Folder :
os.mkdir('test')

# To Print The Path which i work in it
print(os.getcwd())

# To rename file using os
os.rename('test2.txt','test3.txt')

# To create folder or folders in path using os :
os.makedirs('test/folder1/folder2/folder3')

# To remove folder but the folder must be empty :
os.rmdir('test/folder1/folder2/folder3')

# To remove all path :
os.removedirs('test/folder1/folder2')

# To display everything in path or direction
d = "C:/Users/goda6/Downloads"
print(os.listdir(d))

```



#### The Dir the directory and display all in the path in list :

```python
import os

d = "C:/Users/goda6/Downloads"

for dirpath , dirname , filename in os.walk(d):
    print(f'Path is : {dirpath}')
    print(f'Name is : {dirname}')
    print(f'File is : {filename}')
```



#### The Task To make folder For every type And move file in it :

```python
import os
import shutil

os.chdir('Many_files')
for file in os.listdir('.'):
    if file.endswith(('.jpg','.png')) :
        os.makedirs('Images', exist_ok=True)
        shutil.move(file,'Images')

    elif file.endswith(('.pdf','.xlsx','docx')) :
        os.makedirs('Documents', exist_ok=True)
        shutil.move(file,'Documents')

    elif file.endswith(('.sql')) :
        os.makedirs('Database', exist_ok=True)
        shutil.move(file,'Database')

    elif file.endswith(('.mp4')) :
        os.makedirs('Videos', exist_ok=True)
        shutil.move(file,'Videos')

    elif file.endswith(('.ttf','.otf')) :
        os.makedirs('Fonts',exist_ok=True)
        shutil.move(file,'Fonts')
```



#### The Task To make folder For every type And move file in it :

```python
import os
import shutil
import mimetypes

os.chdir('test_files')
for file in os.listdir('.'):
    #kind = filetype.guess(file).EXTENSION
    kind , _ = mimetypes.guess_type(file)
    if os.path.isfile(file) :
        if kind :
            type_name = kind.split('/')[0]
            os.makedirs(type_name, exist_ok=True)
            shutil.move(file,type_name)
        else :
            os.makedirs('Others', exist_ok=True)
            shutil.move(file,'Others')
```



#### To Test which function is the fast :

```python
import timeit

def func1 ():
    numbers = list(range(1,100))
    result = []
    for x in numbers :
        result.append(x*x)
    return result
    
def func2 () :
    numbers = list(range(1,100))
    result = [x*x for x in numbers]
    return result

def func3 () :
    numbers = list(range(1,100))
    result = (x*x for x in numbers)
    return result

print(timeit.timeit(func1,number=10000))
print(timeit.timeit(func2,number=10000))
print(timeit.timeit(func3,number=10000))
```

