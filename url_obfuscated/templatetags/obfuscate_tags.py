from django import template
from ..helpers import obfuscate

register = template.Library()

@register.filter(name='obfuscate')
def obfuscate_url_parameter(value):
    if isinstance(value, int):
        return obfuscate(str(value))
    else:
        return obfuscate(str(value))
