from django.shortcuts import render
from .models import Photograph
from .models import Acrylic
from .models import Watercolor

# Create your views here.


def artView(request):
    watercolors = Watercolor.objects.order_by('my_order')
    acrylics = Acrylic.objects.order_by('my_order')
    photos = Photograph.objects.order_by('my_order')
    return render(request, 'art.html', {'watercolors': watercolors, 'acrylics': acrylics, 'photos': photos})
