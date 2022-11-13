from django.views import generic
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.models import Variant,Product


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

def productListView(request):
    products = Product.objects.all()
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
        'query_size':query_size
    }
    return render(request,'products/list.html',context)



