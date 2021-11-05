from django.shortcuts import render

# Create your views here.


def landing_page(request):
    template = "landingpage.html"
    return render(request, template)
