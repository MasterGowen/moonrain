from django import template
import time
register = template.Library()


def toduration(value):
    try:
        value = int(value)
    except:
        pass
    if isinstance( value, int ):
        return time.strftime('%H:%M:%S', time.gmtime(value))
    else:
        return value

register.filter('toduration', toduration)