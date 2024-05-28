from django import template
import re

register = template.Library()

@register.simple_tag(takes_context=True)
def match_path(context, pattern):
    path = context['request'].path
    return re.match(pattern, path)