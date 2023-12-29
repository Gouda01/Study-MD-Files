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
OR
data = Product.objects.filter(flag = 'New').filter(price__gt = 98)
```

##### لعرض كل المنتجات اللي الفلاج فيها بيكون جديد والسعر اكبر من 98 (يطبق في حالة الشرطين معا) 

```django
from django.db.models import Q

data = Product.objects.filter(
        Q(flag = 'New') &
        Q(price__gt = 98)
        ) 
```

##### لعرض كل المنتجات اللي الفلاج فيها بيكون جديد  أو السعر اكبر من 98 (يطبق في حالة الشرط الاول او الشرط الثاني) 

```django
from django.db.models import Q

data = Product.objects.filter(
        Q(flag = 'New') |
        Q(price__gt = 98)
        ) 
```

##### لعرض كل المنتجات اللي الفلاج فيها بيكون غير ~ جديد  أو السعر اكبر من 98 (يطبق في حالة الشرط الاول او الشرط الثاني) 

```django
from django.db.models import Q

data = Product.objects.filter(
        ~Q(flag = 'New') |
        Q(price__gt = 98)
        ) 
```



##### <u>field reference:</u>

##### لعرض كل المنتجات اللي الكمية فيها بتساوي السعر  (المقارنة بين عامودين بيتم تعريف العامود التاني  بهذه الطريقة) 

```django
from django.db.models import F

data = Product.objects.filter(quantity = F('price'))
```

##### لعرض كل المنتجات اللي الكمية فيها بتساوي الاي دي في البراند (بينهم علاقة )(المقارنة بين عامودين بيتم تعريف العامود التاني  بهذه الطريقة) 

```django
from django.db.models import F

data = Product.objects.filter(quantity = F('brand__id'))
```



##### <u>Order :</u>

##### لعرض كل المنتجات مرتبة حسب الاسم تنازلي من A to Z 

```django
data = Product.objects.order_by('name')
```

##### لعرض كل المنتجات مرتبة حسب الاسم تصاعدي من Z to A 

```django
data = Product.objects.order_by('-name')
```

##### ترتيب المنتجات تنازلي من A to Z ثم عرض اول 10 نتائج

```django
data = Product.objects.order_by('name') [:10]
```

##### ترتيب المنتجات تنازلي من A to Z ثم عرض اول نتيجة

```django
data = Product.objects.earliest('name')
```

##### ترتيب المنتجات تنازلي من A to Z ثم عرض اخر نتيجة

```django
data = Product.objects.latest('name')
```

##### لعرض الاسم والسعر فقط في كل المنتجات

```django
data = Product.objects.values('name','price')  #Return in dictionary
OR
data = Product.objects.values_list('name','price') #Return in typle
```

##### لعرض كل الاعمدة ما عدا الوصف في كل المنتجات

```django
data = Product.objects.defer('description')
```



##### <u>*Lmimit related*</u>

```django
data = Product.objects.select_related('brand').all() # One To One & One To Many Relation
data = Product.objects.select_related('brand').all() # Many To Many Relation
data = Product.objects.select_related('brand').select_related('category').all()
```



##### <u>*Aggregation : Count - Min - Max - Sum - AVG*</u>

```django
from django.db.models.aggregates import Count,Sum,Avg,Max,Min

data = Product.objects.aggregate(
        myavg = Avg('price'),
        mycount=Count('id'),
        mysum=Sum('price'),
    )
```



##### <u>*Annotation :*</u>

```django
from django.db.models import F

data = Product.objects.annotate(price_with_tax = F('price')*1.14)
```

