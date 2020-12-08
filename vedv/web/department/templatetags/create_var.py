from django import template

register = template.Library()

@register.simple_tag
def makedict(string):
    key_value_list = string.split(', ')
    data = {}
    for key_value in key_value_list:
        key = key_value.split('=')
        data[key[0]] = key[1]
    return data
