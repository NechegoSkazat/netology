from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    sorting_rules = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}
    if not sort:
        phone_objects = Phone.objects.all()
    else:
        phone_objects = Phone.objects.all().order_by(sorting_rules.get(sort))
    template = 'catalog.html'
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone_object}
    return render(request, template, context)