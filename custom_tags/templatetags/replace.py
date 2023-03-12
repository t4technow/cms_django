from django import template

register = template.Library()

@register.simple_tag
def replace_category(text):
    return text.replace('/category/', '').capitalize()


@register.simple_tag
def replace_tag(text):
    return text.replace('/tag/', '').capitalize()

@register.simple_tag
def replace_post(text):
    return text.replace('/post/', '').capitalize()

@register.simple_tag
def replace_author(text):
    return text.replace('/author/', '').capitalize()