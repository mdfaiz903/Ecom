from django.db import models
from django.contrib.auth.models import User
# Create your models here.
DIVISION_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Noakhali','Noakhali'),
    ('khulna','khulna'),
    ('Borishal','Borishal'),
    ('chattagram','chattagram'),
    ('Sylhet','Sylhet'),
)
class customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    division = models.CharField(choices=DIVISION_CHOICES,max_length=50)
    thana = models.CharField(max_length=100)
    vill_or_road = models.CharField(max_length=255)
    zipcode = models.IntegerField
    def __str__(self):
        return str(self.id)
CATAGORY_CHOICES=(
    ('GP','Gents Pant'),
    ('BK','Borkha'),
    ('BF','Baby Fashion'),
    ('S','Sharee'),
    ('L','Lehenga'),

)
class product(models.Model):
    title = models.CharField(max_length=255)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=50)
    catagory = models.CharField(choices=CATAGORY_CHOICES,max_length=2)
    product_img = models.ImageField(upload_to='product_img')
    def __str__(self):
        return str(self.id)
    
class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    

STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Cancel','Cancel'),
)

class orderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date=models.DateField(auto_now=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICE,default='pending')
    def __str__(self):
        return str(self.id)


