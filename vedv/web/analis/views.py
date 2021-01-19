from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.http import HttpResponse
from .diuretic import *
from .make_describe_excel import *
from .gena import *
import os
import pandas as pd
import ast
from django.contrib.auth.decorators import permission_required, login_required

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
    # html_list = create_html_tables_list(n, shifr)
    html_list, df_list = get_diuretic_html_data(shifr, n)
    print('sdds')
    print(type(df_list))
    df = {}
    for i in df_list:
        df[i] = df_list[i].to_dict()
    string_protocols_df_to_excel(str(df))
    return render(request, 'analis/protocols.html', context={'d':html_list, 'df_list':df})
    
@login_required
def get_analis(request):
    string = request.GET.get('q')
    df_list = string_df_to_dict(string) #  orient='index'
    desc_list_html = create_describe_list(df_list)[0]
    return render(request, 'analis/describe.html', context={'dff':desc_list_html})
