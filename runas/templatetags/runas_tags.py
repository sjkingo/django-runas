from django import template

from ..middleware import _SESSION_KEY

register = template.Library()

@register.inclusion_tag('includes/runas/banner.html', takes_context=True)
def runas_banner(context):
    return {
        'runas_active': _SESSION_KEY in context['request'].session,
        'impersonated_user': context['user'],
    }
