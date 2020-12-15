from django.shortcuts import render
from django.http import StreamingHttpResponse
from .diuretic import *
from .make_describe_excel import *
import os

def get_home(request):
    return render(request, 'analis/home.html')

def stream_response(request):
    if request.method == 'POST':
        if request.POST.get('numero', False):
            m = request.POST['numero']   
            # print "My Number %s" % m #watch your command line 
            resp = StreamingHttpResponse(m)
            return resp

    return render(request, 'analis/some.html', context={'resp':resp})

def get_protocols(request):
    if request.method == 'POST':
        if request.POST.get('n', False):
            n = int(request.POST['n'])
        if request.POST.get('shifr', False):
            shifr = request.POST['shifr']
    html_list = create_html_tables_list(n, shifr)

    return render(request, 'analis/protocols.html', context={'d':html_list})

def get_analis(request):
    two_up =  os.path.abspath(os.path.join(__file__ ,"../.."))
    html_list = create_describe(two_up+'/assets/protocols_diuretic.xlsx')
    return render(request, 'analis/describe.html', context={'d':html_list})