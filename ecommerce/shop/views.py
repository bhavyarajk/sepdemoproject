from django.shortcuts import render,redirect
from shop.models import Category,Product
def categories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'categories.html',context)
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
def products(request,i):
    c=Category.objects.get(id=i)
    p=Product.objects.filter(category=c)
    context={'cat':c,'pro':p}
    return render(request,'products.html',context)

def productdetail(request,i):
    p=Product.objects.get(id=i)
    context={'pro':p}
    return render(request,'detail.html',context)

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST.get('e')
        fn=request.POST['f']
        ln=request.POST['l']
        if(cp==p):
            user=User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln)
            user.save()
            return redirect('shop:categories')

    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']

        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')

        else:
            messages.error(request,"invalid credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:categories')

def addcategories(request):
    if(request.method=="POST"):
        n=request.POST['n']
        i=request.FILES.get('i')
        d=request.POST.get('d')
        c=Category.objects.create(name=n,image=i,desc=d)
        c.save()
        return redirect('shop:categories')
    return render(request,'addcategories.html')


def addproducts(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES.get('i')
        d = request.POST.get('d')
        s=request.POST.get('s')
        p=request.POST.get('p')
        c=request.POST.get('c')   #category name

        cat=Category.objects.get(name=c)  #Retrieve a category record matching with that name

        p=Product.objects.create(name=n,image=i,desc=d,stock=s,price=p,category=cat)   #here category is foreign key field
        p.save()
        return redirect('shop:categories')
    return render(request, 'addproducts.html')


def addstock(request,i):
    p=Product.objects.get(id=i)
    if(request.method=="POST"):
        p.stock=request.POST['n']
        p.save()
        return redirect('shop:detail',i)

    context={'pro':p}
    return render(request,'addstock.html',context)







