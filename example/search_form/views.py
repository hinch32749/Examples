from django.shortcuts import render

from .models import Rubric, Category, Product
from .forms import Searchform


def search(request):
    form = Searchform()
    rubrics = Rubric.objects.all()

    if request.method == "POST":
        print(request.POST)
        categories = dict(request.POST)
        items = []
        for category in categories['category']:
            items.append(Category.objects.get(id=category))
        context = {'form': form, 'rubrics': rubrics, 'items': items}
        return render(request, 'search_form/search_form.html', context)

    context = {'form': form, 'rubrics': rubrics}
    return render(request, 'search_form/search_form.html', context)
