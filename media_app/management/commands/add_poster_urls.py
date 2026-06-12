"""
Management command to assign TMDB poster and backdrop URLs to all movies and series.
Uses The Movie Database (TMDB) public image CDN for poster images.
"""
import sys
from django.core.management.base import BaseCommand
from media_app.models import Movie, Series

# TMDB image base: https://image.tmdb.org/t/p/{size}/{path}
# Sizes: w92, w154, w185, w342, w500, w780, original

TMDB_BASE = "https://image.tmdb.org/t/p"

MOVIE_POSTERS = {
    'inception': {
        'poster': f'{TMDB_BASE}/w500/ljsZTbVsrQSqZgWeep2B1QiDKuh.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/8ZTVqvKDQ8emdgUE8xfyO3qREHJ.jpg',
    },
    'shawshank-redemption': {
        'poster': f'{TMDB_BASE}/w500/9cjIGRiQoRCgTNEMmcoADqwiBIL.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg',
    },
    'dark-knight': {
        'poster': f'{TMDB_BASE}/w500/qJ2tW6WMUDux911BTUgMe1nNaD.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/nMKdUUepR0i5zn0y1T4CsSB5kMo.jpg',
    },
    'pulp-fiction': {
        'poster': f'{TMDB_BASE}/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg',
    },
    'interstellar': {
        'poster': f'{TMDB_BASE}/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/xJHokMbljvjADYdit5fK1pVHEMm.jpg',
    },
    'the-godfather': {
        'poster': f'{TMDB_BASE}/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/tmU7GeKVybMWFButWEGl2M4GeiP.jpg',
    },
    'parasite': {
        'poster': f'{TMDB_BASE}/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/TU9bcK1VkmRGRm2pT6vriQa9fm.jpg',
    },
    'spider-man-spider-verse': {
        'poster': f'{TMDB_BASE}/w500/8Vt6mWEReuy4Of61Lnj5Xzh75CF.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/b3MDggIbR3JX3JKyPIzQHQpG2OL.jpg',
    },
    'joker': {
        'poster': f'{TMDB_BASE}/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/gZWl93sf8AxavYpVT1Un6EF3oCj.jpg',
    },
    'dune': {
        'poster': f'{TMDB_BASE}/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/jYEW5xZkZk2WTrdbMGAPFuBqbDc.jpg',
    },
    'grand-budapest-hotel': {
        'poster': f'{TMDB_BASE}/w500/eWDyYq6Iu2pjNiNJLF0ZNSqCiZp.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/nX5XotM9yprCKarRH4fzOq1VM1J.jpg',
    },
    'oppenheimer': {
        'poster': f'{TMDB_BASE}/w500/8Gxv8gSbU0SbOuqFqKPtS4gO.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg',
    },
}

SERIES_POSTERS = {
    'breaking-bad': {
        'poster': f'{TMDB_BASE}/w500/ztkUQFLlC19CCMYHW9o1zWhJRNq.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/tsRy63Mu5cu8etL1X7ZLyf7UP1M.jpg',
    },
    'game-of-thrones': {
        'poster': f'{TMDB_BASE}/w500/1XS1oqL89opfnbLl8WnZY1O1uJx.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/suopoADq6k8BBCSunS06sWMEHpx.jpg',
    },
    'stranger-things': {
        'poster': f'{TMDB_BASE}/w500/uOOtwVbSr4QDjAGIifLDwpb2Pdl.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/56v2KjBlYj6rfIb1k3wG3VYt2rE.jpg',
    },
    'chernobyl': {
        'poster': f'{TMDB_BASE}/w500/hlLXt2tOPT6RRnjiUmoxyG1LTFi.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/900kRVVVOYBwkQFKiLMCLdmHJPb.jpg',
    },
    'the-mandalorian': {
        'poster': f'{TMDB_BASE}/w500/sWgBv7LV2PRoQgkxwlibdGXKz1S.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/o7TGFWM4R4GEoqvjbVMXsGmBhFB.jpg',
    },
    'dark-series': {
        'poster': f'{TMDB_BASE}/w500/apbrbWs8M9lyOpJYU5WXrpFbk1Z.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/3lBDg8gj0YIOWjDFfMj0gGy2QBF.jpg',
    },
    'the-last-of-us': {
        'poster': f'{TMDB_BASE}/w500/uKvVjHNqB5VmOrdxqAt2F7J78ED.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/5Bkq0HqZ2QpjT5gSTYk5l4wPEoP.jpg',
    },
    'sherlock': {
        'poster': f'{TMDB_BASE}/w500/f9KsMEj3qmrONR7aEMEbvMrBbbT.jpg',
        'backdrop': f'{TMDB_BASE}/w1280/mFb0t4Jrvy0vHxFdSIR4bGPJEX5.jpg',
    },
}


class Command(BaseCommand):
    help = 'Assign TMDB poster and backdrop URLs to all movies and series'

    def handle(self, *args, **kwargs):
        if sys.stdout.encoding != 'utf-8':
            sys.stdout.reconfigure(encoding='utf-8')

        self.stdout.write('Adding poster URLs...')

        updated_movies = 0
        for movie in Movie.objects.all():
            urls = MOVIE_POSTERS.get(movie.slug)
            if urls:
                movie.poster_url = urls['poster']
                movie.backdrop_url = urls['backdrop']
                movie.save(update_fields=['poster_url', 'backdrop_url'])
                updated_movies += 1
                self.stdout.write(f'  Updated movie: {movie.title}')

        updated_series = 0
        for ser in Series.objects.all():
            urls = SERIES_POSTERS.get(ser.slug)
            if urls:
                ser.poster_url = urls['poster']
                ser.backdrop_url = urls['backdrop']
                ser.save(update_fields=['poster_url', 'backdrop_url'])
                updated_series += 1
                self.stdout.write(f'  Updated series: {ser.title}')

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! Updated {updated_movies} movies and {updated_series} series with poster URLs.'
        ))
