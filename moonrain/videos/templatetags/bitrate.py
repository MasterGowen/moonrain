from django import template
from django.template import defaultfilters
register = template.Library()


def bitrate(bits):
    try:
        bits = int(bits)
    except:
        pass
    if isinstance(bits, int):
        try:
            return defaultfilters.filesizeformat(bits).replace('Б', 'Бит/с')
        except:
            return bits

register.filter('bitrate', bitrate)