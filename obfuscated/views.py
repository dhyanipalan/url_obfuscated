from django.shortcuts import render
from url_obfuscated.decorators import deobfuscate
from url_obfuscated.helpers import obfuscate

def home(request):
    links = list()
    for i in range(10):
        links.append(obfuscate('Name %d' % (i+1)))
    return render(request, 'index.html', { 'links': links })

@deobfuscate
def obfuscated_link(request, name):
    return render(request, 'obfuscate_result.html', { 'name': name })

@deobfuscate
def optional_param(request, param=None):
    return render(request, 'optional_param.html', { 'param': param })
