from django import template
from shows.models import Photo

register = template.Library()


@register.filter(name='serapiSlides')
def serapiSlides(value):
    if value.photo_category == "HOME_SLIDESHOW":
        return value.image


register.filter('serapiSlides', serapiSlides)
