from django import template
from ..helpers import obfuscate

register = template.Library()

@register.filter(name='obfuscate')
def obfuscate_url_parameter(value):
    print('in obfuscate_url_parameter tags')
    if isinstance(value, int):
        print('Integer-----', value, type(value))
        return obfuscate(str(value))
    else:
        print('String-----', value, type(value))
        temp = value.encode('utf8')
        print(temp, type(temp))
        return obfuscate(str(value))
