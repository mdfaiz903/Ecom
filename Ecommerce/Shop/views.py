from django.shortcuts import render
from django.views import View
from .models import product,customer,cart,orderPlaced
# Create your views here.
class productView(View):
     def get(self,request):
       gentspant = product.objects.filter(catagory = 'GP')
       Borkha = product.objects.filter(catagory = 'BK')
       babyfashion = product.objects.filter(catagory = 'BF')
       return render(request,'Shop/home.html',{'gentspant':gentspant,'Borkha':Borkha,'babyfashion':babyfashion})

class productDetailView(View):
  def get(self,request,pk):
    Product = product.objects.get(pk=pk)
    return render(request,'Shop/productdetail.html',{'product':Product})

     
# def home(request):
#      return render(request, 'Shop/home.html')

# def product_detail(request):
#  return render(request, 'Shop/productdetail.html')

def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

def buy_now(request):
 return render(request, 'Shop/buynow.html')

def profile(request):
 return render(request, 'Shop/profile.html')

def address(request):
 return render(request, 'Shop/address.html')

def orders(request):
 return render(request, 'Shop/orders.html')

def change_password(request):
 return render(request, 'Shop/changepassword.html')

def lehenga(request):
 return render(request, 'Shop/lehenga.html')

def login(request):
     return render(request, 'Shop/login.html')

def customerregistration(request):
 return render(request, 'Shop/customerregistration.html')

def checkout(request):
 return render(request, 'Shop/checkout.html')
