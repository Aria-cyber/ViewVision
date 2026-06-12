from django import template

register = template.Library()

GENRE_ICON_MAP = {
    'action': 'fas fa-fire',
    'drama': 'fas fa-theater-masks',
    'comedy': 'fas fa-face-laugh-beam',
    'sci-fi': 'fas fa-rocket',
    'horror': 'fas fa-ghost',
    'thriller': 'fas fa-eye',
    'adventure': 'fas fa-compass',
    'animation': 'fas fa-palette',
    'documentary': 'fas fa-video',
    'romance': 'fas fa-heart',
    'crime': 'fas fa-shield-halved',
    'fantasy': 'fas fa-hat-wizard',
}

DEFAULT_ICON = 'fas fa-film'


@register.filter
def genre_icon(genre_slug):
    """Return the Font Awesome icon class for a genre slug."""
    return GENRE_ICON_MAP.get(genre_slug, DEFAULT_ICON)
