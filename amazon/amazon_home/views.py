from django.shortcuts import render

# Create your views here.
def method(request):
    return render(request, "index.html")

def method2(request):
    return render(request, "sec_page.html")

def method3(request):
    return render(request, "footer.html")

def method4(request):
    return render(request, "fourth_pg.html")