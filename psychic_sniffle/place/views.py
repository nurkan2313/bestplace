from django.shortcuts import render

from .models import Place, Category
# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def show_list(request):
    places = Place.objects.all().order_by('-created')
    categories = Category.objects.all()
    return render(request, 'places/list.html', {'places': places, 'categories': categories})


def category_list(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    places = Place.objects.filter(category=category)

    return render(request, 'places/list.html', {
        'places': places, 'category': category, 'categories': categories,
    })


def place_detail(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render(request, 'places/detail.html', {'place': place})


def search(request):
    context = {}
    q = request.GET.get('q', None)

    if q:
        places = Place.objects.filter(name__icontains=q)
        context = {'query': q, 'places': places}
        template = 'places/list.html'
    return render(request, template, context)

