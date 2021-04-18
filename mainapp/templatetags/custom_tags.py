from django import template

register = template.Library()

@register.filter(name='indexVal')
def indexVal(lis,i):
    return list(lis)[i]