from django.shortcuts import render
from .models import CurrentShow
from .models import PreviousVenue

# Create your views here.

def eventsView(request):
    current_shows = CurrentShow.objects.order_by('end_date')
    previous_venues = PreviousVenue.objects.order_by('venue_name')
    return render(request, 'events.html', {'currentShows' : current_shows, 'previousVenues': previous_venues})
