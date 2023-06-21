from django.shortcuts import render,redirect
from django.contrib import  messages
from .forms import *
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


def home(req):
    if req.method == 'GET':
        newsform = NewsForm()
        contactform = ContactUsForm()
        context = {
        'newsform': newsform,
        'contactform': contactform,
        'last4product': Product.objects.filter(status=True)[:3][::-1]
                    }
        return render(req, 'home/index.html',context=context)
    elif req.method == 'POST':
        if req.POST.get('subject'):
            contactform = ContactUsForm(req.POST)
            contactform.save()
            return redirect('/')
        else:
            newsform = NewsForm(req.POST)
        
            if newsform.is_valid():
                newsform.save()
                messages.add_message(req,messages.ERROR,'Your email has been sent.')
                return redirect('/')
            else:
                messages.add_message(req,messages.ERROR,'The Email is not valid !')
                return redirect('/')





def products(req,category=None):
    if req.method == 'GET':
        products = Product.objects.filter(status=True)
        if category:
            products = Product.objects.filter(status=True,category__name=category)
        # if req.GET.get('search'):
        #     products = Product.objects.filter(status=True,title__name=req.GET.get('search'))
        if req.GET.get('search'):
            search_query = req.GET.get('search')
            products = products.filter(title__icontains=search_query)
        newsform = NewsForm()
        category = Category.objects.all()[::-1]
        products = Paginator(products, 3)
        try:
            page_number = req.GET.get('page')
            products = products.get_page(page_number)


        except PageNotAnInteger:
            products = products.get_page(1)
     
        except EmptyPage:
            products = products.get_page(1)

        context = {
        'newsform': newsform,
        'products':products,
        'category':category,
                    }
        return render(req, 'home/product.html',context=context)
    elif req.method == 'POST':        
        newsform = NewsForm(req.POST)
        
        if newsform.is_valid():
            newsform.save()
            messages.add_message(req,messages.ERROR,'Your email has been sent.')
            return redirect('home:products')
        else:
            messages.add_message(req,messages.ERROR,'The Email is not valid !')
            return redirect('home:products')

def product(req,pid):
    if req.method == 'GET':
        newsform = NewsForm()
        try:
            product = Product.objects.get(id = pid, status=True)
            context = {
            'product': product,
            'newsform': newsform,
                        }
            return render(req, 'home/product-info.html',context=context)
        except:return render(req, 'home/404.html',{'newsform':NewsForm()})
    elif req.method == 'POST':        
        newsform = NewsForm(req.POST)
        
        if newsform.is_valid():
            newsform.save()
            messages.add_message(req,messages.ERROR,'Your email has been sent.')
            return redirect(req.META.get('HTTP_REFERER'))
        else:
            messages.add_message(req,messages.ERROR,'The Email is not valid !')
            return redirect(req.META.get('HTTP_REFERER'))    


@login_required
def create_product(req):
    if req.method=="GET":
          form = ProductForm()
          context = {
               'form':form,
          }
          return render(req, 'registration/create_product.html',context=context)
    elif req.method=='POST':
            form = ProductForm(req.POST,req.FILES)
            print(req.POST)
            if form.is_valid():
                form.save()
            return redirect('home:products')
            # else :
            #     messages.add_message(req,messages.ERROR,'The input data is not valid !')
            #     return redirect('home:create_product')    

      