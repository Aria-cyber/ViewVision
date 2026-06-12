from pathlib import Path


def social_links(request):
    """Read social media links from links.txt and pass them to all templates."""
    links = {
        'instagram': '#',
        'telegram': '#',
        'linkedin': '#',
        'github': '#',
    }
    links_file = Path(__file__).resolve().parent.parent / 'links.txt'
    try:
        with open(links_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if '=' in line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    key = key.strip().lower()
                    value = value.strip()
                    if key in links and value:
                        links[key] = value
    except FileNotFoundError:
        pass
    return {'social_links': links}
