from django import template
import re

register = template.Library()

@register.filter
def regex_match(value, pattern):
    return re.match(pattern, value)