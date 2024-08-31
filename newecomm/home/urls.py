
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_registerpage, name='register'),
    path('login/', views.user_loginpage, name='login'),
    # path('forget_password/', views.user_forget_password, name='forget_password'),
    # path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('logout/', views.user_logoutpage, name='logout'),
    # path('contact/', views.user_contactpage, name='contact'),
    # path('my_account/', views.my_accountpage, name='my_account'),
    # path('add_address/', views.add_address_page, name='add_address'),
    # path('update_address/', views.update_address_page, name='update_address'),
    # path('checkout_update_address/', views.checkout_update_address_page, name='checkout_update_address'),
    # path('update_account_details/', views.update_account_details_page, name='update_account_details'),

    #============= Product Details================================
    # path('product_details/', views.product_details_page, name='product_details'),

    #============= Blog Details ==================================
    # path('blog_details/', views.blog_details_page, name='blog_details'),

    #============= Shop Details ==================================
    # path('shop_left_details/', views.shop_left_details_page, name='shop_left_details'),

    #============= cart ==================================
    # path('cart_view/', views.cart_view_page, name='cart_view'),
    # path('cart_update/', views.cart_update_page, name='cart_update'),
    # path('cart_delete/', views.cart_delete_page, name='cart_delete'),

    #============= Checkout ==================================
    # path('cart_checkout/', views.cart_checkout_page, name='cart_checkout'),

    #============= Payment ==================================


    # path('place_order/', views.handle_paypal_payment, name='place_order'),

    # path('paypal/create/', views.create_payment, name='create_payment'),
    # path('paypal/execute/', views.execute_payment, name='execute_payment'),
    # path('order_placed/',views.order_placed,name='order_placed')
]