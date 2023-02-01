from django.shortcuts import render

# Create your views here.
def yakoyo_app(request):
    return render (request, "index.html", {})
