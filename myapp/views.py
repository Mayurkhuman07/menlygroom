from django.shortcuts import render,redirect
from .models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout, authenticate
from django.contrib import messages
import razorpay
# from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    if request.user.id:
    #count Cart
        
        count= Cart.objects.filter(user_id=request.user.id).count()

        prod = Product.objects.all()
        temp = []
        for i in prod:
            temp.append(i.id)
        print(temp)
        import random
        tp=random.sample(temp, 8)
        print(tp)
        products = Product.objects.filter(id__in=tp)[:8]
        print(len(products))
        
    
        return render(request,"index.html",{'products': products,'count':count})
    else:
        return redirect('login')

def shop(request,id):
    if request.user.id:


#count Cart
   
        count= Cart.objects.filter(user_id=request.user.id).count()

        cat_name= Category.objects.get(id=id)
        prod = Product.objects.filter(cat_name_id=id)
        sub_cat = SubCategory.objects.filter(cat_name_id=id)
        for i in sub_cat:
            print(i)
        return render(request,"shop.html",{'products':prod,'sub_cat':sub_cat,'cat_name':cat_name,'count':count})

def add_to_cart(request,id):

   
    if  request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        print(user.id,"KKKKKKKKkk")
        product = Product.objects.get(id=id)
        count = Cart.objects.filter(user_id=request.user.id,product_id=product.id).count()
        cart = Cart.objects.filter(user_id=request.user.id,product_id=product.id)
       
        if count>0:
            qty = cart[0].qty + 1
            price = qty * product.price
            Cart.objects.filter(user_id=request.user.id,product_id=product.id).update(qty=qty,price=price)
            return redirect('index')
        else:
            qty =1
            cart = Cart(user=user,product=product,qty=qty,price=product.price)
            cart.save()
            return redirect('index')
    else:
        return redirect('login')

def remove_item(request, cart_item_id):
     Cart.objects.filter(user_id=user.id).delete()
     return redirect('cart')

def buynow(request,id):

   
    if  request.user.is_authenticated:
       
        product = Product.objects.get(id=id)
        count = Cart.objects.filter(user_id=request.user.id,product_id=product.id).count()
        cart = Cart.objects.filter(user_id=request.user.id,product_id=product.id)
        if count>0:
            qty = cart[0].qty + 1
            price = qty * product.price
            Cart.objects.filter(user_id=request.user.id,product_id=product.id).update(qty=qty,price=price)
            return redirect('cart')
        else:
            cart = Cart(user_id=request.user.id,product_id=product.id,qty=1,price=product.price)
            cart.save()
            return redirect('cart')
    else:
        return redirect('login')


def productsingle(request):

    #count Cart
 
    count= Cart.objects.filter(user_id=request.user.id).count()
    cart= Cart.objects.filter(user_id=request.user.id)
    cid=request.GET.get('cid')
    var=Product.objects.get(pk=cid)
    if cid:
        return render(request,"productsingle.html",{'count':count,'var1':var,'cart':cart })
        var=Product.objects.get(pk=cid)
    else:
        return render(request,"productsingle.html")
    


   
    

def cart(request):

    #count Cart
   
    count= Cart.objects.filter(user_id=request.user.id).count()

    if request.user.is_authenticated:
     
       
        cart_j = Cart.objects.filter(user_id=request.user.id)
        list1 = []
        for i in cart_j:
            list1.append(i.price)
        print(list1)
        total = sum(list1)
        
        return render(request,"cart.html",{'all_product':cart_j,'count':count,'total':total})
    else:
        return redirect('login')




def about(request):

    #count Cart
   
    count= Cart.objects.filter(user_id=request.user.id).count()

    return render(request,"about.html",{'count':count})

def blog(request):
    #count Cart
    
    count= Cart.objects.filter(user_id=request.user.id).count()

    return render(request,"blog.html",{'count':count})

def contact(request):
    #count Cart
   
    count= Cart.objects.filter(user_id=request.user.id).count()

    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        msg=request.POST['msg']
        obj =Contact(name=name,email=email,subject=subject,msg=msg)
        obj.save()
        return redirect ('index')
    else:
        return render(request,"contact.html",{'count':count})

def blogsingle(request):
    #count Cart
    
    count= Cart.objects.filter(user_id=request.user.id).count()

    return render(request,"blog-single.html",{'count':count})

def login1(request):
    if request.method =='POST':
        name=request.POST['name']
        pass1=request.POST['pass1']
        try:
            # user = authenticate(usrename=name,password=pass1)
            user = authenticate(username=name, password=pass1)

            if user is not None:
                login(request,user)
                messages.success(request, 'Logged Successfully !!')
                return redirect('index')
            else:
                messages.error(request, 'Username or password Incorrect !!')
                return redirect('login')
        except:
            messages.error(request, 'Username or password Incorrect !!')
            return redirect ('login')
    else:
        return render(request,"login.html")
def logout1(request):
    logout(request)
    messages.success(request, 'logout Successfully !!')
    return redirect('login')

def register(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['number']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        print(name,email,phone,pass1,pass2)
        if not  User.objects.filter(username=name,email=email).exists():
            if pass1 == pass2:
                user = User.objects.create_user(username=name,email=email)
                user.set_password(pass2)
                user.save()
                messages.error(request, 'Account Created Successfully !! ')
                return redirect ('login')
            else:
                messages.error(request, 'Password  and Confirm Password are not match !!')
                return redirect("register")
        else:
            messages.error(request, 'Username or email Already exists !! ')
            return redirect("register")
    else:
        return render(request,"register.html")
    

def order(request):
    if request.method =='POST':
        
       
        cart = Cart.objects.filter(user_id=request.user.id)
        data = serializers.serialize('json',cart)
        fname = request.POST['fname']
        lname = request.POST['lname']
        products = data
        email = request.POST['email']
        postcode = request.POST['postcode']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        import random
        order_id = random.randint(00000,99999)

        print(fname,lname,email,postcode,phone,address,city,order_id,products)
        obj = Order(user=request.user,fname=fname,lname=lname,order_id=order_id,products=products,email=email,phone=phone,city=city,postcode=postcode,address=address)
        obj.save()
        Cart.objects.filter(user_id=request.user.id).delete()
        return redirect('thankyou')
    else:
        return render(request,"cart")


def thankyou(request):
    return render(request,'thankyou.html')


def checkout(request):
    amount=0
    count= Cart.objects.filter(user_id=request.user.id).count()    
    if request.user.is_authenticated:

        if request.method =='POST':
            print("Hello")
            cart = Cart.objects.filter(user_id=request.user.id)
            data = serializers.serialize('json',cart)
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            postcode = request.POST['postcode']
            phone = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            import random
            order_id = random.randint(00000,99999)

            # print(fname,lname,email,postcode,phone,address,city,order_id,products)
            obj = Order(user=request.user,fname=fname,lname=lname,order_id=order_id,products=data,email=email,phone=phone,city=city,postcode=postcode,address=address)
            obj.save()
            
                
            return redirect('payment')
            
        return render(request,"checkout.html")

    return redirect('login')

def payment(request):
    if request.user.is_authenticated:
        order_id = Order.objects.filter(user__id=request.user.id).last()
        print(order_id)
        cart_j = Cart.objects.filter(user_id=request.user.id)
        amount = 1000
        for i in cart_j:
            amount += i.price * 100
                
        client = razorpay.Client(auth=("rzp_test_FajQFRRkHwQVGd", "58lrcrY3Ocya9uLnP4wMI83H"))

        response = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': 0})
        response ={'amount':amount,'payment':payment,"order_id":order_id}
        Cart.objects.filter(user_id=request.user.id).delete()
        return render(request,"payment.html",response)
    else:
        return redirect('login')

@csrf_exempt
def success(request,oid):
    order_st = Order.objects.get(user=oid)
    order_st.payment_status=True
    order_st.save()
    return redirect('trackorder')

def plus(request):
    if request.method == 'POST':
        cid=request.POST['plus']
        print(cid)
        var2=Cart.objects.get(pk=cid)
        var2.qty+=1
        var2.price=var2.product.price * var2.qty
        var2.save()
        return redirect('cart')
        
        
    return redirect('cart')

def minus(request):
    if request.method == 'POST':
        cid=request.POST['minus']
        print(cid)
        var2=Cart.objects.get(pk=cid)
        var2.qty-=1
        var2.price=var2.product.price * var2.qty
        var2.save()
        return redirect('cart')
        
    return redirect('cart')


def remove(request,id):
    var2=Cart.objects.get(pk=id)
    var2.delete()
    return redirect('cart')
def s_add_to_cart(request):

   
    if  request.user.is_authenticated:
        if request.method =="GET":
            p_id = request.GET["p_id"]
            p_qty = request.GET["p_qty"]
            print(p_qty)
            print(p_id)


            user = User.objects.get(username=request.user)
            product = Product.objects.get(id=p_id)
            count = Cart.objects.filter(user_id=request.user.id,product_id=product.id).count()
            cart = Cart.objects.filter(user_id=request.user.id,product_id=product.id)
           
            if count>0:
                qty = cart[0].qty + 1
                price = qty * product.price
                Cart.objects.filter(user_id=request.user.id,product_id=product.id).update(qty=qty,price=price)
                response = {'status': 0, 'message': _("Your error"), 'url':''} 
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                cart = Cart(user=user,product=product,qty=p_qty,price=product.price*int(p_qty))
                cart.save()
                response = {'status': 0, 'message': _("Your error"), 'url':''} 
                return HttpResponse(json.dumps(response), content_type='application/json')
        else:
            pass
    else:
        return redirect('login')
import json
def trackorder(request):
    order = Order.objects.filter(user=request.user,payment_status=True)
    for o in order:
        
        for j in json.loads(o.products):
            print(type(j['fields']))
            order_data = Product.objects.filter(id=j['fields']['product'])
            return render(request,"trackorder.html",{"order_data":order_data})


def singleaddtocart(request):
    pass

def account(request):
    pass

