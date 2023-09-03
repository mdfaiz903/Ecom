from django.contrib import admin
from . models import orderPlaced,cart,product,customer
# Register your models here.
@admin.register(customer)
class customerModelAdmin(admin.ModelAdmin):
    list_display=[
        'id','user','name','division','thana','vill_or_road','zipcode'
    ]

@admin.register(product)
class productModelAdmin(admin.ModelAdmin):
    list_display=[
        'id','title','selling_price','discount_price','description','brand','catagory','product_img'
    ]


@admin.register(cart)
class cartModelAdmin(admin.ModelAdmin):
    list_display=[
        'id','user','product','quantity'
    ]

@admin.register(orderPlaced)
class orderPlacedModelAdmin(admin.ModelAdmin):
    list_display=[
        'id','user','customer','product','quantity','ordered_date','status'
    ]

