from django.shortcuts import render, HttpResponse

# Create your views here.
def first(request):
    html = "Django Response"
    return HttpResponse(html)

def second(request):
    return render(request, 'index.html')