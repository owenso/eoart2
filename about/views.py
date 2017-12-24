from django.shortcuts import render
from .models import SelfPhoto
from .models import Friends
from .models import Bio

# Create your views here.


def aboutView(request):
    bio = Bio.objects.get()
    self_photo = SelfPhoto.objects.get()
    friends = Friends.objects.order_by('my_order')
    return render(request, 'about.html', {'bio': bio, 'selfPhoto': self_photo, 'friends': friends})
