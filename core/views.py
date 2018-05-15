from django.shortcuts import render

# Create your views here.


def test_staticfiles(request):
    template = 'core/test_staticfiles.html'
    return render(request, template, {})
