from django.shortcuts import render, HttpResponse, redirect
from home.decorators import login_required
from datetime import datetime
from home.models import Register, Login_user
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def cart_counter(user_id):
    # count = Cart.objects.filter(user__user_id = user_id).count()
    return HttpResponse("Cart.count")
    # return count

def index(request):
    # context = {'products' : Product.objects.all()}
    return render(request , 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def user_registerpage(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = Register(first_name=first_name, last_name=last_name, email = email,
                            password=password, created_at = datetime.today(), updated_at = datetime.today())
        user_obj.save()
        messages.success(request, "Your registration has been confirmed")
        return redirect('login')

    return render(request , 'register.html')
    # return HttpResponse("Hello, world. You're at the register page.")

def user_loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        check = Register.objects.get(email=email, password=password)
        if check:
            messages.success(request, "You have been successfully login")
            return render(request,'userpage.html')
        else:
            messages.error(request, "Inavlid Email or Password")
            return redirect('login')
    return render(request , 'login.html')
   

def user_logoutpage(request):
    return HttpResponse("Hello, world. You're at the logout page.")

@login_required
def cart_view_page(request):
    # if request.GET.get('to'):
    #     print("hello")
    # user_id = request.session['user_id']
    # user = User.objects.get(pk=user_id)
    # cart_counter = Cart.objects.filter(user__user_id=user_id).count()
    # cart_data = Cart.objects.filter(user__user_id=user_id).annotate(final_amount=ExpressionWrapper(F('cart_quantity') * F('cart_price'),
    #     output_field=DecimalField()
    # ))
    
    # total_amount = cart_data.aggregate(total=Sum('final_amount'))['total']
    # if total_amount is not None:
    #     total_amount_after_shipping = int(total_amount) + 70
    # else:
    #     total_amount = 0
    #     total_amount_after_shipping = 0
    # if request.method == 'POST':
    #     form = CartForm(request.POST, initial={'user': user})
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Item Added Successfully!")
    #         if request.GET.get('to'):
    #             return redirect('shop_left_details')
    #         return redirect('cart_view')
    # else:
    #     form = CartForm()
    # context = {'cart_data':cart_data,
    # 'total_amount':total_amount,
    # 'total_amount_after_shipping':total_amount_after_shipping,
    # 'cart_counter':cart_counter,
    # 'form':form,
    # }
    return HttpResponse("catr view")
    # return render(request, "cart.html", context)

@login_required
def cart_checkout_page(request):
    # cart_count = 0
    # user_id = request.session['user_id']
    # cart_count = cart_counter(user_id)
    # cart_data = Cart.objects.filter(user__user_id = user_id).annotate(final_amount=ExpressionWrapper(F('cart_quantity') * F('cart_price'),
    #     output_field=DecimalField()
    # ))

    # total_amount = cart_data.aggregate(total=Sum('final_amount'))['total']
    # if total_amount is not None:
    #     total_amount_after_shipping = int(total_amount) + 70
    # else:
    #     total_amount = 0
    #     total_amount_after_shipping = 0

    # # Address Data
    # address_exits = Address.objects.filter(address_user_id__user_id = user_id).exists()
    # if address_exits:
    #     address_data = Address.objects.get(address_user_id=user_id)
    # else:
    #     address_data = None

    # context = {'cart_data':cart_data, 'total_amount':total_amount, 'total_amount_after_shipping':total_amount_after_shipping, 'address_exits':address_exits, 'address_data':address_data, 'cart_counter':cart_count}

    # return render(request, 'checkout.html', context)
    return HttpResponse("checkout.html")

@login_required
def my_accountpage(request):
    # cart_count = 0
    # user_id = request.session.get('user_id')
    # cart_count = cart_counter(user_id)
    # if user_id:
    #     try:
    #         profile_data = User.objects.get(user_id=user_id)
    #         order = Order.objects.filter(order_user_id = profile_data)
    #         order_details = OrderDetails.objects.filter(order_user_id = profile_data)
    #         context = {'profile_data': profile_data,'order':order,'order_details':order_details}
    #     except User.DoesNotExist:
    #         context = {'error': 'User not found.'}
    # else:
    #     context = {'error': 'User not logged in.'}

    # address_exits = Address.objects.filter(address_user_id__user_id = user_id).exists()
    # if address_exits:
    #     address_data = Address.objects.get(address_user_id=user_id)
    # else:
    #     address_data = None
    # context.update({'address_exits':address_exits, 'address_data':address_data, 'cart_count':cart_count})
    # return render(request, "my_account.html", context)
    return HttpResponse("my_account.html")

def shop_left_details_page(request):
    # cart_count = 0
    # if 'user' in request.session:
    #     user_id = request.session['user_id']
    #     cart_count = cart_counter(user_id)
    # cats = Category.objects.all().distinct().annotate(counts = Count('category_name'))
    # sizes_all = Size.objects.values('size_size').annotate(counts=Count('size_size')).distinct()
    # if request.GET.get('cat_id'):
    #     shoes_data = Product.objects.filter(product_cat__category_id = request.GET.get('cat_id'))
    # else:      
    #     shoes_data = Product.objects.all()
    # product_id_list = [x.product_id for x in shoes_data]

    # discount_prices = {}
    # for offer in Offer.objects.filter(offer_product_id__product_id__in = product_id_list):
    #     discount_prices[offer.offer_product_id.product_id] = offer.offer_discount
    
    # products_with_prices = []
    # for shoes in shoes_data:
    #     size = Size.objects.filter(size_product_id = shoes.product_id)
     
    #     discount = discount_prices.get(shoes.product_id, 0)
    #     final_prices = (shoes.product_price - discount)

    #     products_with_prices.append(
    #         {"product_id":shoes.product_id,
    #         "product_image1":shoes.product_img1,
    #         "product_image2":shoes.product_img2.url if shoes.product_img2 else None,
    #         "product_image3":shoes.product_img3.url if shoes.product_img3 else None,
    #         "product_image4":shoes.product_img4.url if shoes.product_img4 else None,
    #         "product_name":shoes.product_name,
    #         "product_price":shoes.product_price,
    #         'product_desc':shoes.product_desc,
    #         'sizes':size,
    #         'category':shoes.product_cat,
    #         "product_price_after_discount":final_prices}
    #     )
    #     context ={
    #         'cats':cats,
    #         'p_data':products_with_prices,
    #         'sizes_all':sizes_all,
    #         'cart_counter':cart_count
    #     }
    return render(request, "shop2.html")
# def product(request, product_id):
#     return HttpResponse(f"You're looking at product {product_id}.")