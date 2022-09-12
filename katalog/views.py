from django.shortcuts import render
from katalog.models import CatalogItem

# Views
def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
    'list_item': data_item_katalog,
    'nama': 'Muhammad Iqbal Dwitama',
    'id': '2106750490'
    }
    return render(request, "katalog.html", context)