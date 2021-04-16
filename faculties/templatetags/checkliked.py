from django import template
from django.core.exceptions import ObjectDoesNotExist
register = template.Library()
from news.models import Like

@register.simple_tag
def check(postId,session):
    try:
        Like.objects.get(post_id=postId,user=session)
        return "active"
    except ObjectDoesNotExist:
        return ""