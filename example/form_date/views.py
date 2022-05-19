from django.shortcuts import render

from .forms import GetDateForm


def get_date(request):
    form = GetDateForm()
    if request.method == 'POST':
        form = GetDateForm(request.POST)
        # if form.is_valid():
        #     print(form.cleaned_data)
    context = {'form': form}
    return render(request, 'form_date/form_date.html', context)


