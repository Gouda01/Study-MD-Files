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

##### لعرض كل المنتجات اللي البراند بتاعها ( علاقة )  الاي دي بتاعة يساوي 5

```django
data = Product.objects.filter(brand__id = 5)
```

##### لعرض كل المنتجات اللي البراند بتاعها ( علاقة )  الاسم بتاعة يساوي Apple

```django
data = Product.objects.filter(brand__name = 'Apple')
```

##### لعرض كل المنتجات اللي البراند بتاعها ( علاقة )  الاي دي بتاعة اكبر من 200

```django
data = Product.objects.filter(brand__id__gt = 200)
```



#### <u>Text :</u>

##### لعرض كل المنتجات اللي الاسم فيها بيحتوي علي كلمة Joseph

```django
data = Product.objects.filter(name__contains = 'Joseph')
```

##### لعرض كل المنتجات اللي الاسم فيها بيبدأ بكلمة Joseph

```django
data = Product.objects.filter(name__startswith = 'Joseph')
```

##### لعرض كل المنتجات اللي الاسم فيها بتنتهي بكلمة Joseph

```django
data = Product.objects.filter(name__endswith = 'Joseph')
```

##### لعرض كل المنتجات اللي السعر فيها بيكون فارغ 

```django
data = Product.objects.filter(price__isnull = True)
```

##### لعرض كل المنتجات اللي السعر فيها بيكون غير فارغ 

```django
data = Product.objects.filter(price__isnull = False)
```

##### لعرض كل المنتجات اللي السعر فيها بيكون غير فارغ 

```django
data = Product.objects.filter(price__isnull = False)
```



##### <u>Date:</u>

##### لعرض كل المنتجات سنة معينة او شهر معين او يوم معين 

```django
data = Product.objects.filter(created_at__year = 2022) 
data = Product.objects.filter(created_at__month = 2) 
data = Product.objects.filter(created_at__day = 12) 
```



##### <u>*Complex Queries*:</u>

##### لعرض كل المنتجات اللي الفلاج فيها بيكون جديد والسعر اكبر من 98 (يطبق شرطين) 

```django
data = Product.objects.filter(flag = 'New',price__gt = 98) 
```

