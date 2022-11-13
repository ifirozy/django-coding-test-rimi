from django.views import generic
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.models import Variant,Product
import datetime
from django.db.models import Q

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

def productListUtils(products,request):
    variants = Variant.objects.filter(active=True)
    page = request.GET.get('page', 1)
    query_size = 2
    paginator = Paginator(products, query_size)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'product': True,
        'products':products,
        'query_size':query_size,
        'variants':variants
    }
    return context

def productListView(request):
    product_title   =   request.GET.get('title',None)
    variant         =   request.GET.get('variant',None)
    price_from     =   request.GET.get('price_from',None)
    price_to       =   request.GET.get('price_to',None)
    date            =   request.GET.get('date',None)
  
    if product_title and variant and price_from and price_to and date:
        products = Product.objects.filter(Q(title__icontains=product_title) | Q(created_at__date=datetime.datetime.strptime(date,'%Y-%m-%d')) |
                                            Q(product_variant__price__gte = price_from) | Q(product_variant__price__lte = price_to) |
                                            Q(product_variant__product_variant_one__variant_title=variant) |
                                            Q(product_variant__product_variant_two__variant_title=variant) |
                                            Q(product_variant__product_variant_three__variant_title=variant) )
      
    else:
        products = Product.objects.all()

    context = productListUtils(products,request)
    return render(request,'products/list.html',context)


