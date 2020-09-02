from django import template

reg = template.Library()

@reg.filter(name='cut')
def cut(value, arg):
    return value.replace(arg,'')

