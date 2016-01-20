from django.template import Library
import re

register = Library()
@register.filter
def remove_html_tags(value, tags):
    try:
        tags = re.split(", |,", tags)
        for tag in tags:
            value = re.sub(r"<"+tag+">.*</"+tag+">", "", value)
        return value
    except ValueError:
        return value
