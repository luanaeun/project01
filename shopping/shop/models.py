from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, null=False)
    slug = models.SlugField(allow_unicode=True)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)    

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])
    
    # def save(self, *args, **kwargs):
    #     value = self.title
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)




class Closet(models.Model):

    COLOR = (
        ('Red','Red'), ('Pink','Pink'), ('Orange','Orange'), ('Yellow','Yellow'),
        ('Green','Green'), ('Blue','Blue'), ('Purple', 'Purple'), ('Black','Black'),
        ('Grey','Grey')
    )

    # CATEGORY_CHOICES = (('상의','top'), ('반팔','short_shirt'), ('긴팔','long_shirt'),
    #                     ('민소매','sleeveless_shirt'), ('하의','bottom'), ('바지','pants'), 
    #                     ('치마','skirt'), ('원피스','dress')
    # )

    user_id = models.CharField(max_length=10, blank=True)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    clothes_name = models.CharField('옷 이름', max_length=20, unique=True)

    clothes_category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)

    clothes_color = models.CharField(max_length=10, blank=True, choices=COLOR)

    clothes_image = models.ImageField()

    put_date = models.DateField(auto_now_add=True)

    use_count = models.IntegerField(null=True, blank=True, default=0)

    
    def __str__(self):
        return self.clothes_name

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Product,self).save(*args, **kwargs)

    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

    
  