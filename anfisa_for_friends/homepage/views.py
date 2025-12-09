from django.shortcuts import render
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'title', 'id', 'description', 'price'
        ).filter(is_published=True,
                 is_on_main=True,
                 category__is_published=True
                 ).order_by('output_order', 'title')[0:3]
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
