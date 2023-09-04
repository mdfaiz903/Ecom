from django.urls import path
from Shop import views
from django.conf.urls.static import static
from django.conf import settings
from . forms import LoginForm
from django.contrib.auth import views as auth_v
urlpatterns = [
    # path('', views.home),
    path('', views.productView.as_view(),name='productView'),
    path('product-detail/<int:pk>', views.productDetailView.as_view(), name='product-detail'),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('lehenga/<slug:data>', views.lehenga, name='lehengaItem'),
    path('lehenga/', views.lehenga, name='lehenga'),
    path('account/login/', auth_v.LoginView.as_view(template_name='Shop/login.html',authentication_form=LoginForm),name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.customerregistration.as_view(), name='customerregistration'),
    path('logout/', auth_v.LogoutView.as_view(next_page='login'),name='logout'),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
