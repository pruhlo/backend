from django.shortcuts import render

# Create your views here.
def  get_home_page(request):
    return render(request, 'department/home_page.html')

def  get_start_page(request):
    return render(request, 'department/start_page.html')