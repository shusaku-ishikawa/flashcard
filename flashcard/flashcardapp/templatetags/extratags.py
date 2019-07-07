import re
from django import template
from django.conf import settings
from ..models import *

register = template.Library()

@register.filter
def multiply(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    return int(value) * int(arg)

@register.filter
def ismistakenby(value, arg):
    mistaken = CardMistaken.objects.filter(card = value, user = arg)
    return len(mistaken) != 0


