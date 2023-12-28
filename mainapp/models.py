from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from mainapp.utils import seo

class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Size(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
     
class Color(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
   
class Product(BaseMixin):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    hoverimage = models.ImageField()
    stock = models.PositiveSmallIntegerField(default=0)
    price = models.PositiveSmallIntegerField()
    discount_price = models.PositiveSmallIntegerField(default=0)
    wishlist = models.ManyToManyField(User)
    size = models.ForeignKey(Size,on_delete=models.CASCADE,null=True,blank=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    rating = models.CharField(null=True,blank=True,max_length=1)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.name)
        self.slug = new_slug
        if Product.objects.filter(slug=new_slug).exists():
            count = 0
            while Product.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.name)}-{count}"
                count += 1
        super(Product, self).save(*args, **kwargs)
    
    
class BasketItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='carditems')
    quantity = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return self.product.name

    
    
        
