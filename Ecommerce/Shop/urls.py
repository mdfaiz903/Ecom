from django.urls import path
from Shop import views
from django.conf.urls.static import static
from django.conf import settings
from . forms import LoginForm,Mypasswoedchangeform,MypasswordResetform,MySetPasswordForm
from django.contrib.auth import views as auth_v
urlpatterns = [
  
    path('', views.productView.as_view(),name='productView'),
    path('product-detail/<int:pk>', views.productDetailView.as_view(), name='product-detail'),

    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('accounts/password_change/',auth_v.PasswordChangeView.as_view(template_name='Shop/passwordchange.html',form_class=Mypasswoedchangeform, success_url = '/passwordchangedone/'), name='changepassword'),
  
    path('accounts/password_change/done/',auth_v.PasswordChangeDoneView.as_view(template_name='Shop/passwordchangedone.html'),name='passwordchangedone'),
    path('accounts/password_reset/',auth_v.PasswordResetView.as_view(template_name='Shop/password_reset.html'),name='passwordReset'),
    path('accounts/password_reset/done/',auth_v.PasswordResetDoneView.as_view(template_name='Shop/password_reset_done.html'),name='password_reset_done'),
    path('accounts/password_reset/done/confirm/<uidb64>/<token>/',auth_v.PasswordResetConfirmView.as_view(template_name='Shop/password_rest_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('accounts/password_reset/done/confirm/complete/',auth_v.PasswordResetCompleteView.as_view(template_name='Shop/password_rest_complete.html'),name='password_reset_complete'),
    path('lehenga/<slug:data>', views.lehenga, name='lehengaItem'),
    path('lehenga/', views.lehenga, name='lehenga'),
    path('account/login/', auth_v.LoginView.as_view(template_name='Shop/login.html',authentication_form=LoginForm),name='login'),
  
    path('registration/', views.customerregistration.as_view(), name='customerregistration'),
    path('accounts/logout/', auth_v.LogoutView.as_view(next_page='login'),name='logout'),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
