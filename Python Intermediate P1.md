#### Normal Loop :

```python
names = ['ahmed','ali','mahmoud','aid','hassan']
new_names = []
for x in names :
    new_names.append(x.upper())

print(new_names)
```



#### List Comprehension :

```python
new_names2 = [x.upper() for x in names]
new_names3 = [x.upper() for x in names if len(x)>3]
new_names4 = [x.upper() if len(x)>3 else '.....' for x in names]

print(new_names2)
print(new_names3)
print(new_names4)
```

