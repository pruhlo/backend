from django.shortcuts import render

# Create your views here.
def  get_home_page(request):
    return render(request, 'department/home_page.html')