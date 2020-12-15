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

@register.simple_tag
def makelist(string):
    value_list = string.split(', ')
    return value_list

@register.simple_tag
def pathithem(path, ithem):
    if type(path)==str and type(ithem)==str:
        value = path + ithem
    return value