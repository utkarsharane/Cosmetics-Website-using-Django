from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Product,Bag,Wishlist,RegisterBlog,Order
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import random
import razorpay



# Create your views here.


#---------------------------------------------------- index section ----------------------------------------------------

def index(req):
    username = req.user.username
    allproducts = Product.objects.all()
    context = {"allproducts": allproducts, "username":username}
    return render(req,'index.html',context)

# -----------------------------------------------Signin/Register section------------------------------------------------

def register(req):
    if req.method == "POST":
        uname=req.POST['uname']
        upass=req.POST['upass']
        ucpass=req.POST['ucpass']
        context = {}
        if uname =="" or upass=="" or ucpass=="":
            context["errmsg"] = "Field can't be empty"
            return render(req, "register.html",context)
        elif ucpass != ucpass:
            context["errmsg"] = "Password and confirm password doesn't match"
            return render(req, "register.html",context)
        else:
            try:
                u = User.objects.create(username=uname,password=upass)
                u.set_password(upass)
                u.save()
                return redirect("/signin")
            except Exception:
                context["errmsg"] = "User already exists"
                return render(req, "register.html",context)
    else:
        return render(req,'register.html')
    

def signin(req):
    if req.method == "POST":
        uname=req.POST['uname']
        upass=req.POST['upass']
        context = {}
        if uname =="" or upass=="":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signin.html",context)
        else:
            u = authenticate(username=uname,password=upass)
            if u is not None:
                login(req,u)
                return redirect("/")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(req, "signin.html",context)
    else:
        return render(req,'signin.html')
    
def signout(req):
    logout(req)
    return redirect("/")


# ----------------------------------------Cart section------------------------------------------

def bag(req):
    if req.user.is_authenticated:
        username = req.user.username
        allbags = Bag.objects.filter(userid=req.user.id)
        total_price = 0
        for x in allbags:
            total_price += x.product_id.price * x.qty
        length = len(allbags)
        context = {
            "bag_items": allbags,
            "total": total_price,
            "items": length,
            "username": username,
        }
        return render(req, "bag.html", context)
    else:
        allbags = Bag.objects.filter(userid=req.user.id)
        total_price = 0
        for x in allbags:
            total_price += x.product_id.price * x.qty
        length = len(allbags)
        context = {
            "bag_items": allbags,
            "total": total_price,
            "items": length,
        }
        return render(req, "bag.html", context)


def movetobag(req, product_id):
    if req.user.is_authenticated:
        user = req.user
    else:
        user = None
    allproducts = get_object_or_404(Product, product_id=product_id)
    bag_item, created = Bag.objects.get_or_create(product_id=allproducts, userid=user)
    if not created:
        bag_item.qty += 1
    else:
        bag_item.qty = 1
    bag_item.save()
    return redirect("/bag")


def removefrombag(req, product_id):
    if req.user.is_authenticated:
        user = req.user
    else:
        user = None
    bag_item = Bag.objects.filter(product_id=product_id, userid=user)
    bag_item.delete()
    return redirect("/bag")

def updateqty(req, qv, product_id):
    allbags = Bag.objects.filter(product_id=product_id)
    if qv == "1":
        totol = allbags[0].qty + 1
        allbags.update(qty=totol)
    else:
        if allbags[0].qty > 1:
            totol = allbags[0].qty - 1
            allbags.update(qty=totol)
        else:
            allbags = Bag.objects.filter(product_id=product_id)
            allbags.delete()
    return redirect("/bag")



# ------------------------------------------Categories section-----------------------------------------------------

def makeup(request):
    if request.method == "GET":
        allproducts = Product.prod.makeup()
        context = {"allproducts":allproducts}
        return render(request, "index.html",context)
    else:
        allproducts = Product.objects.all()
        context = {"allproducts":allproducts}
        return render(request,"index.html",context)

def haircare(request):
    if request.method == "GET":
        allproducts = Product.prod.haircare()
        context = {"allproducts":allproducts}
        return render(request, "index.html",context)
    else:
        allproducts = Product.objects.all()
        context = {"allproducts":allproducts}
        return render(request,"index.html",context)
    
def skincare(request):
    if request.method == "GET":
        allproducts = Product.prod.skincare()
        context = {"allproducts":allproducts}
        return render(request, "index.html",context)
    else:
        allproducts = Product.objects.all()
        context = {"allproducts":allproducts}
        return render(request,"index.html",context)
    
def appliances(request):
    if request.method == "GET":
        allproducts = Product.prod.appliances()
        context = {"allproducts":allproducts}
        return render(request, "index.html",context)
    else:
        allproducts = Product.objects.all()
        context = {"allproducts":allproducts}
        return render(request,"index.html",context)
    

#-------------------------------------------- search section  ----------------------------------------------

def searchcosmetic(request):
    query = request.GET.get("c")
    if query:
        allproducts = Product.objects.filter(Q(product_name__icontains=query)|Q(category__icontains=query)|Q(price__icontains=query))
    else:
        allproducts = Product.objects.all()
    context = {"allproducts": allproducts, "query":query}
    return render(request,"index.html", context)

# ----------------------------------------------wishlist section-----------------------------------------

def wishlist(req):
    if req.user.is_authenticated:
        username = req.user.username
        allwishlists = Wishlist.objects.filter(userid=req.user.id)
        context = {
            "wishlist_items": allwishlists,
            "username": username,
        }
        return render(req, "wishlist.html", context)
    else:
        allwishlists = Wishlist.objects.filter(userid=req.user.id)
        context = {
            "wishlist_items": allwishlists,
        }
        return render(req, "wishlist.html", context)

def addtowishlist(req, product_id):
    if req.user.is_authenticated:
        user = req.user
    else:
        user = None
    allproducts = get_object_or_404(Product, product_id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(product_id=allproducts, userid=user)
    if not created:
        wishlist_item.qty += 1
    else:
        wishlist_item.qty = 1
    wishlist_item.save()
    return redirect("/wishlist")


def removefromwishlist(req, product_id):
    if req.user.is_authenticated:
        user = req.user
    else:
        user = None
    wishlist_item = Wishlist.objects.filter(product_id=product_id, userid=user)
    wishlist_item.delete()
    return redirect("/wishlist")


#--------------------------------------------Blog section---------------------------------------------------

def blog(req):
    blog = RegisterBlog.objects.all()
    context = {"blog":blog}
    return render(req, "blog.html", context)

def registerblog(req):
    if req.method == "GET":
        return render(req,"registerblog.html")
    else:
        if (
            "photo" in req.FILES 
            and "title" in req.POST 
            and "name" in req.POST
            and "description" in req.POST
        ):
            photo = req.FILES["photo"]
            title = req.POST["title"]
            name = req.POST["name"]
            description = req.POST["description"]
            blog = RegisterBlog.objects.create(photo=photo,title=title, name=name, description=description)
            blog.save()
            return redirect("/blog")
        else:
            return HttpResponse("Invalid request method")
        
        
def deleteblogs(req,id):
    blog=RegisterBlog.objects.filter(id=id)
    blog.delete()
    return redirect("/blog")


#--------------------------------------------Order section---------------------------------------------------

def myorder(request):
    if request.user.is_authenticated:
        user=request.user
    else:
        user=None
    allbags = Bag.objects.filter(userid=user)
    total_price = 0
    length = len(allbags)
    for x in allbags:
        total_price += x.product_id.price * x.qty
    context={}
    context['bag_items']=allbags
    context['total']=total_price
    context['items']=length
    context['username']=user
    return render(request,'myorder.html',context)


def removefromorder(request, product_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    orders=Order.objects.filter(userid=user,product_id=product_id)
    orders.delete()
    return redirect("/bag")


#--------------------------------------------Payment section---------------------------------------------------


def payment(request):
    if request.user.is_authenticated:
        user=request.user
        order_id=random.randrange(100,9999)
        allbags = Bag.objects.filter(userid=user)
        for x in allbags:
            o=Order.objects.create(order_id=order_id,product_id=x.product_id,userid=x.userid,qty=x.qty)
            o.save()
            x.delete()
        orders=Order.objects.filter(userid=user)
        total_price = 0
        for x in orders:
            total_price += x.product_id.price * x.qty
            oid=x.order_id
        client = razorpay.Client(auth=("rzp_test_XbhYMD4vITX4b9","nfOAGJwKiCmnUpockwLXqfyL"))
        data = { "amount": total_price*100, "currency": "INR", "receipt": str(oid) }
        payment = client.order.create(data=data)
        context={}
        context['data']=payment
        context['amount']=payment
        return render(request,'payment.html',context)
    else:
        user=None
        return redirect('/signin')
    

def userorders(req):
    if req.user.is_authenticated:
        user=req.user
        allorders = Order.objects.filter(userid=user)
        context = {"allorders": allorders, "username": user}
        return render(req, "userorders.html", context)
    else:
        user=None
        return redirect('/signin')