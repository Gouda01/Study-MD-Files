### <u>**Queryset API**</u>



#### <u>Column Number :</u>

#####  لعرض كل المنتجات

```django
data = Product.objects.all()
```

#####  لعرض كل المنتجات اللي سعرها يساوي 20

```django
data = Product.objects.filter(price = 20)
```

#####  لعرض كل المنتجات اللي سعرها اكبر من 98

```django
data = Product.objects.filter(price__gt = 98)
```

#####  لعرض كل المنتجات اللي سعرها اكبر من او يساوي 98

```django
data = Product.objects.filter(price__gte = 98)
```

#####  لعرض كل المنتجات اللي سعرها اقل من 98

```django
data = Product.objects.filter(price__lt = 98)
```

#####  لعرض كل المنتجات اللي سعرها اقل من او يساوي 98

```django
data = Product.objects.filter(price__lte = 98)
```

#####  لعرض كل المنتجات اللي سعرها بين 80 و 83

```django
data = Product.objects.filter(price__range = (80,83))
```



#### <u>Relation :</u>

###### 

###### 