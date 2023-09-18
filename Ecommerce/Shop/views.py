from django.shortcuts import render,redirect
from django.views import View
from .models import product,customer,cart,orderPlaced
from . forms import CustomerRegistrationForm,customerprofileViewForm
from django.contrib import messages
from django.db.models import Q 
from django.http import JsonResponse
# Create your views here.
def plus_cart(request):
    if request.method == 'GET':
      prod_id = request.GET['prod_id']
      c = cart.objects.get(Q(product=prod_id) & Q(user=request.user))
      
      c.quantity +=1
      c.save()
      amount = 0.0
      shipping_amount = 100.0
      cart_product = [p for p in cart.objects.all() if p.user==request.user]
      for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount  
            totalamount = amount + shipping_amount
      data = {
         'quantity': c.quantity,
         'amount': amount,
         'totalamount': totalamount
      }
      return JsonResponse(data)
    
def minus_cart(request):
    if request.method == 'GET':
      prod_id = request.GET['prod_id']
      c = cart.objects.get(Q(product=prod_id) & Q(user=request.user))
      
      c.quantity -=1
      c.save()
      amount = 0.0
      shipping_amount = 100.0
      cart_product = [p for p in cart.objects.all() if p.user==request.user]
      for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount  
            totalamount = amount + shipping_amount
      data = {
         'quantity': c.quantity,
         'amount': amount,
         'totalamount': totalamount
      }
      return JsonResponse(data)
  
def add_to_cart(request):
  user = request.user
  product_id = request.GET.get('prod_id')
  Product = product.objects.get(id=product_id)
  cart(user=user,product=Product).save()
  return redirect('/cart/')

def show_cart(request):
   if request.user.is_authenticated:
      user = request.user
      Cart = cart.objects.filter(user=user)
      amount = 0.0
      shipping_amount = 100.0
      total = 0.0
      cart_product = [p for p in cart.objects.all() if p.user==user]
      if cart_product:
         for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount  
            totalamount = amount + shipping_amount
         return render(request, 'Shop/addtocart.html', {'carts':Cart, 'totalamount':totalamount,'amount':amount })
      else:
         return render(request, 'Shop/emptycart.html')



class profileView(View):
  def get(self, request):
    form = customerprofileViewForm
    return render(request, 'Shop/profile.html',{'form':form,'active':'btn-primary'})
  def post(self,request):
    form = customerprofileViewForm(request.POST)
    if form.is_valid():
      usr = request.user
      name = form.cleaned_data['name']
      division = form.cleaned_data['division']
      thana = form.cleaned_data['thana']
      vill_or_road = form.cleaned_data['vill_or_road']
      zipcode = form.cleaned_data['zipcode']

      data = customer(user = usr,name=name,division=division,thana=thana,vill_or_road=vill_or_road,zipcode=zipcode)
      data.save()
      messages.success(request,'Congratulations! Profile updated .')
      return render(request,'Shop/profile.html',{'form':form,'active':'btn-primary'})




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

     


def buy_now(request):
 return render(request, 'Shop/buynow.html')



def address(request):
 data = customer.objects.filter(user= request.user)
 return render(request, 'Shop/address.html',{'data':data,'active':'btn-primary'})

def orders(request):
 return render(request, 'Shop/orders.html')



def lehenga(request,data=None):
  if data==None:
   lehengas = product.objects.filter(catagory='L')
  elif data=='infinity' or data== 'lubnan':
   lehengas = product.objects.filter(catagory='L').filter(brand=data)
  elif data == 'below':
   lehengas = product.objects.filter(catagory='L').filter(discount_price__lt=4000)
  elif data == 'above':
   lehengas = product.objects.filter(catagory='L').filter(discount_price__gt=4000)
   
  return render(request, 'Shop/lehenga.html',{ 'lehengas' :lehengas})


class customerregistration(View):
  def get(self,request):
    form = CustomerRegistrationForm()
    return render(request, 'Shop/customerregistration.html',{'form':form})
  def post(self,request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      messages.success(request,'Congratulations registration done.')
      form.save()
    return render(request, 'Shop/customerregistration.html',{'form':form})


def checkout(request):
 return render(request, 'Shop/checkout.html')
