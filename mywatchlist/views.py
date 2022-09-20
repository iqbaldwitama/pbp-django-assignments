from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    movie_data = MyWatchlist.objects.all()
    watched_movies = MyWatchlist.objects.all().filter(watched=True).count()
    unwatched_movies = MyWatchlist.objects.all().filter(watched=False).count()
    enough_watched = False

    if (watched_movies >= unwatched_movies):
        enough_watched = True
    else:
        enough_watched = False

    context = {
        "list_of_movies" : movie_data,
        "result" : enough_watched 
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    mywatchlist_data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", mywatchlist_data), content_type="application/xml")

def show_xml_by_id(request, id):
    mywatchlist_data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", mywatchlist_data), content_type="application/xml")

def show_json(request):
    mywatchlist_data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", mywatchlist_data), content_type="application/json")

def show_json_by_id(request, id):
    mywatchlist_data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", mywatchlist_data), content_type="application/json")
