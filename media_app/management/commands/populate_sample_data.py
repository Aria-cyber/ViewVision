import sys
import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from media_app.models import Genre, Movie, Series, Review, WatchlistItem

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate the database with sample data for ViewVision'

    def handle(self, *args, **kwargs):
        # Force UTF-8 output on Windows
        if sys.stdout.encoding != 'utf-8':
            sys.stdout.reconfigure(encoding='utf-8')

        self.stdout.write('Creating sample data...')

        # --- Genres ---
        genres_data = [
            {'name': '\u0627\u06a9\u0634\u0646', 'slug': 'action', 'description': '\u0641\u06cc\u0644\u0645\u200c\u0647\u0627 \u0648 \u0633\u0631\u06cc\u0627\u0644\u200c\u0647\u0627\u06cc \u067e\u0631\u0647\u06cc\u062c\u0627\u0646 \u0628\u0627 \u0635\u062d\u0646\u0647\u200c\u0647\u0627\u06cc \u0627\u06a9\u0634\u0646 \u0648 \u0645\u0628\u0627\u0631\u0632\u0647'},
            {'name': '\u062f\u0631\u0627\u0645', 'slug': 'drama', 'description': '\u062f\u0627\u0633\u062a\u0627\u0646\u200c\u0647\u0627\u06cc \u0639\u0645\u06cc\u0642 \u0648 \u0627\u062d\u0633\u0627\u0633\u06cc \u0628\u0627 \u0634\u062e\u0635\u06cc\u062a\u200c\u067e\u0631\u062f\u0627\u0632\u06cc \u0642\u0648\u06cc'},
            {'name': '\u06a9\u0645\u062f\u06cc', 'slug': 'comedy', 'description': '\u0622\u062b\u0627\u0631 \u0637\u0646\u0632 \u0648 \u0633\u0631\u06af\u0631\u0645\u200c\u06a9\u0646\u0646\u062f\u0647 \u0628\u0631\u0627\u06cc \u0644\u062d\u0638\u0627\u062a \u0634\u0627\u062f'},
            {'name': '\u0639\u0644\u0645\u06cc-\u062a\u062e\u06cc\u0644\u06cc', 'slug': 'sci-fi', 'description': '\u0633\u0641\u0631 \u0628\u0647 \u0622\u06cc\u0646\u062f\u0647 \u0648 \u062f\u0646\u06cc\u0627\u0647\u0627\u06cc \u0646\u0627\u0634\u0646\u0627\u062e\u062a\u0647'},
            {'name': '\u062a\u0631\u0633\u0646\u0627\u06a9', 'slug': 'horror', 'description': '\u0641\u06cc\u0644\u0645\u200c\u0647\u0627 \u0648 \u0633\u0631\u06cc\u0627\u0644\u200c\u0647\u0627\u06cc \u062a\u0631\u0633\u0646\u0627\u06a9 \u0648 \u062f\u0644\u0647\u0631\u0647\u200c\u0622\u0648\u0631'},
            {'name': '\u0647\u06cc\u062c\u0627\u0646\u200c\u0627\u0646\u06af\u06cc\u0632', 'slug': 'thriller', 'description': '\u0622\u062b\u0627\u0631 \u0645\u0639\u0645\u0627\u06cc\u06cc \u0648 \u067e\u0631\u062a\u0646\u0634 \u0628\u0627 \u062f\u0627\u0633\u062a\u0627\u0646\u200c\u0647\u0627\u06cc \u067e\u06cc\u0686\u06cc\u062f\u0647'},
            {'name': '\u0645\u062c\u0627\u0648\u0631\u062c\u0648\u06cc\u06cc', 'slug': 'adventure', 'description': '\u0633\u0641\u0631\u0647\u0627\u06cc \u0647\u06cc\u062c\u0627\u0646\u200c\u0627\u0646\u06af\u06cc\u0632 \u0648 \u06a9\u0634\u0641 \u0646\u0627\u0634\u0646\u0627\u062e\u062a\u0647\u200c\u0647\u0627'},
            {'name': '\u0627\u0646\u06cc\u0645\u06cc\u0634\u0646', 'slug': 'animation', 'description': '\u0622\u062b\u0627\u0631 \u0627\u0646\u06cc\u0645\u06cc\u0634\u0646\u06cc \u0628\u0631\u0627\u06cc \u062a\u0645\u0627\u0645 \u0633\u0646\u06cc\u0646'},
            {'name': '\u0645\u0633\u062a\u0646\u062f', 'slug': 'documentary', 'description': '\u0645\u0633\u062a\u0646\u062f\u0647\u0627\u06cc \u0622\u0645\u0648\u0632\u0634\u06cc \u0648 \u062a\u0645\u0627\u0634\u0627\u06cc\u06cc'},
            {'name': '\u0631\u0645\u0627\u0646\u062a\u06cc\u06a9', 'slug': 'romance', 'description': '\u062f\u0627\u0633\u062a\u0627\u0646\u200c\u0647\u0627\u06cc \u0639\u0627\u0634\u0642\u0627\u0646\u0647 \u0648 \u0627\u062d\u0633\u0627\u0633\u06cc'},
            {'name': '\u062c\u0646\u0627\u06cc\u06cc', 'slug': 'crime', 'description': '\u067e\u0631\u0648\u0646\u062f\u0647\u200c\u0647\u0627\u06cc \u062c\u0646\u0627\u06cc\u06cc \u0648 \u062a\u0639\u0642\u06cc\u0628 \u0645\u062c\u0631\u0645\u0627\u0646'},
            {'name': '\u0641\u0627\u0646\u062a\u0632\u06cc', 'slug': 'fantasy', 'description': '\u062f\u0646\u06cc\u0627\u0647\u0627\u06cc \u062c\u0627\u062f\u0648\u06cc\u06cc \u0648 \u062e\u06cc\u0627\u0644\u200c\u067e\u0631\u062f\u0627\u0632\u0627\u0646\u0647'},
        ]

        genres = {}
        for g in genres_data:
            genre, created = Genre.objects.get_or_create(slug=g['slug'], defaults=g)
            genres[g['slug']] = genre
            if created:
                self.stdout.write(f'  Created genre: {g["slug"]}')

        # --- Users ---
        users_data = [
            {'username': 'ali', 'email': 'ali@example.com', 'bio': '\u0639\u0627\u0634\u0642 \u0633\u06cc\u0646\u0645\u0627 \u0648 \u0646\u0642\u062f \u0641\u06cc\u0644\u0645'},
            {'username': 'sara', 'email': 'sara@example.com', 'bio': '\u0645\u0646\u062a\u0642\u062f \u0641\u06cc\u0644\u0645 \u0648 \u0633\u0631\u06cc\u0627\u0644'},
            {'username': 'mohammad', 'email': 'mohammad@example.com', 'bio': '\u0637\u0631\u0641\u062f\u0627\u0631 \u0641\u06cc\u0644\u0645\u200c\u0647\u0627\u06cc \u0639\u0644\u0645\u06cc-\u062a\u062e\u06cc\u0644\u06cc'},
            {'username': 'fateme', 'email': 'fateme@example.com', 'bio': '\u0639\u0644\u0627\u0642\u0647\u200c\u0645\u0646\u062f \u0628\u0647 \u0645\u0633\u062a\u0646\u062f\u0633\u0627\u0632\u06cc'},
            {'username': 'reza', 'email': 'reza@example.com', 'bio': '\u0641\u06cc\u0644\u0645\u200c\u0628\u0627\u0632 \u062d\u0631\u0641\u0647\u200c\u0627\u06cc'},
        ]

        users = {}
        for u in users_data:
            user, created = User.objects.get_or_create(
                username=u['username'],
                defaults={'email': u['email'], 'bio': u['bio']}
            )
            if created:
                user.set_password('testpass123')
                user.save()
                self.stdout.write(f'  Created user: {u["username"]}')
            users[u['username']] = user

        # --- Movies ---
        movies_data = [
            {
                'title': 'Inception',
                'slug': 'inception',
                'description': '\u06cc\u06a9 \u062f\u0632\u062f \u062d\u0631\u0641\u0647\u200c\u0627\u06cc \u06a9\u0647 \u0627\u0633\u0631\u0627\u0631 \u0631\u0627 \u0627\u0632 \u0636\u0645\u06cc\u0631 \u0646\u0627\u062e\u0648\u062f\u0622\u06af\u0627\u0647 \u0627\u0641\u0631\u0627\u062f \u062f\u0631 \u0647\u0646\u06af\u0627\u0645 \u062e\u0648\u0627\u0628 \u0645\u06cc\u200c\u062f\u0632\u062f\u062f\u060c \u0641\u0631\u0635\u062a\u06cc \u0628\u0631\u0627\u06cc \u067e\u0627\u06a9 \u06a9\u0631\u062f\u0646 \u0633\u0627\u0628\u0642\u0647\u200c\u0627\u0634 \u067e\u06cc\u062f\u0627 \u0645\u06cc\u200c\u06a9\u0646\u062f. \u0627\u0648 \u0628\u0627\u06cc\u062f \u06cc\u06a9 \u0627\u06cc\u062f\u0647 \u0631\u0627 \u062f\u0631 \u0630\u0647\u0646 \u06cc\u06a9 \u0645\u062f\u06cc\u0631\u0639\u0627\u0645\u0644 \u0628\u06a9\u0627\u0631\u062f.',
                'release_date': datetime.date(2010, 7, 16),
                'duration': 148,
                'director': 'Christopher Nolan',
                'cast': 'Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy, Ken Watanabe',
                'rating': 9.3,
                'trailer_url': 'https://www.youtube.com/watch?v=YoHD9XEInc0',
                'genres': ['sci-fi', 'action', 'thriller'],
            },
            {
                'title': 'The Shawshank Redemption',
                'slug': 'shawshank-redemption',
                'description': '\u0627\u0646\u062f\u06cc \u062f\u0648\u0641\u0631\u06cc\u0646\u060c \u0628\u0627\u0646\u06a9\u062f\u0627\u0631\u06cc \u06a9\u0647 \u0628\u0647 \u0627\u062a\u0647\u0627\u0645 \u0642\u062a\u0644 \u0647\u0645\u0633\u0631\u0634 \u0628\u0647 \u062d\u0628\u0633 \u0627\u0628\u062f \u0645\u062d\u06a9\u0648\u0645 \u0645\u06cc\u200c\u0634\u0648\u062f\u060c \u062f\u0631 \u0632\u0646\u062f\u0627\u0646 \u0634\u0627\u0648\u0634\u0646\u06a9 \u0628\u0627 \u0631\u062f \u0645\u0627\u0646\u062f\u0631\u0644\u06cc\u0646\u06af \u062f\u0648\u0633\u062a \u0645\u06cc\u200c\u0634\u0648\u062f. \u0627\u0648 \u0628\u0627 \u0647\u0648\u0634 \u0648 \u0635\u0628\u0631 \u062e\u0648\u062f \u0632\u0646\u062f\u06af\u06cc \u062f\u0631 \u0632\u0646\u062f\u0627\u0646 \u0631\u0627 \u062a\u063a\u06cc\u06cc\u0631 \u0645\u06cc\u200c\u062f\u0647\u062f.',
                'release_date': datetime.date(1994, 9, 23),
                'duration': 142,
                'director': 'Frank Darabont',
                'cast': 'Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler',
                'rating': 9.7,
                'trailer_url': 'https://www.youtube.com/watch?v=PLl99DlL6b4',
                'genres': ['drama'],
            },
            {
                'title': 'The Dark Knight',
                'slug': 'dark-knight',
                'description': '\u0628\u062a\u0645\u0646 \u0628\u0627 \u0628\u0632\u0631\u06af\u200c\u062a\u0631\u06cc\u0646 \u0686\u0627\u0644\u0634 \u062e\u0648\u062f \u0631\u0648\u0628\u0631\u0648 \u0645\u06cc\u200c\u0634\u0648\u062f: \u062c\u0648\u06a9\u0631\u060c \u06cc\u06a9 \u062c\u0646\u0627\u06cc\u062a\u06a9\u0627\u0631 \u0646\u0627\u0628\u063a\u0647 \u06a9\u0647 \u0645\u06cc\u200c\u062e\u0648\u0627\u0647\u062f \u0634\u0647\u0631 \u06af\u0648\u0627\u062a\u0647\u0627\u0645 \u0631\u0627 \u0628\u0647 \u0622\u0634\u0648\u0628 \u0628\u06a9\u0634\u062f.',
                'release_date': datetime.date(2008, 7, 18),
                'duration': 152,
                'director': 'Christopher Nolan',
                'cast': 'Christian Bale, Heath Ledger, Aaron Eckhart, Michael Caine, Gary Oldman',
                'rating': 9.5,
                'trailer_url': 'https://www.youtube.com/watch?v=EXeTwQWrcwY',
                'genres': ['action', 'crime', 'drama'],
            },
            {
                'title': 'Pulp Fiction',
                'slug': 'pulp-fiction',
                'description': '\u0686\u0646\u062f\u06cc\u0646 \u062f\u0627\u0633\u062a\u0627\u0646 \u062c\u0646\u0627\u06cc\u06cc \u0628\u0647 \u0647\u0645 \u067e\u06cc\u0648\u0633\u062a\u0647 \u062f\u0631 \u0644\u0633\u200c\u0622\u0646\u062c\u0644\u0633. \u062f\u0648 \u0622\u062f\u0645\u06a9\u0634 \u062d\u0631\u0641\u0647\u200c\u0627\u06cc\u060c \u0647\u0645\u0633\u0631 \u0631\u0626\u06cc\u0633 \u0645\u0627\u0641\u06cc\u0627\u060c \u06cc\u06a9 \u0628\u0648\u06a9\u0633\u0648\u0631 \u0648 \u06cc\u06a9 \u0632\u0648\u062c \u0633\u0627\u0631\u0642 \u0647\u0645\u0647 \u062f\u0631 \u06cc\u06a9 \u0634\u0628 \u0633\u0631\u0646\u0648\u0634\u062a\u200c\u0633\u0627\u0632 \u0628\u0647 \u0647\u0645 \u06af\u0631\u0647 \u0645\u06cc\u200c\u062e\u0648\u0631\u0646\u062f.',
                'release_date': datetime.date(1994, 10, 14),
                'duration': 154,
                'director': 'Quentin Tarantino',
                'cast': 'John Travolta, Uma Thurman, Samuel L. Jackson, Bruce Willis, Tim Roth',
                'rating': 9.2,
                'trailer_url': 'https://www.youtube.com/watch?v=s7EdQ4FqbhY',
                'genres': ['crime', 'drama', 'thriller'],
            },
            {
                'title': 'Interstellar',
                'slug': 'interstellar',
                'description': '\u062f\u0631 \u0622\u06cc\u0646\u062f\u0647\u200c\u0627\u06cc \u06a9\u0647 \u0632\u0645\u06cc\u0646 \u0631\u0648 \u0628\u0647 \u0646\u0627\u0628\u0648\u062f\u06cc \u0627\u0633\u062a\u060c \u06af\u0631\u0648\u0647\u06cc \u0627\u0632 \u0641\u0636\u0627\u0646\u0648\u0631\u062f\u0627\u0646 \u0627\u0632 \u0637\u0631\u06cc\u0642 \u06cc\u06a9 \u06a9\u0631\u0645\u200c\u0686\u0627\u0644\u0647 \u0633\u0641\u0631 \u0645\u06cc\u200c\u06a9\u0646\u0646\u062f \u062a\u0627 \u0633\u06cc\u0627\u0631\u0647\u200c\u0627\u06cc \u0642\u0627\u0628\u0644 \u0633\u06a9\u0648\u0646\u062a \u0628\u0631\u0627\u06cc \u0628\u0634\u0631\u06cc\u062a \u067e\u06cc\u062f\u0627 \u06a9\u0646\u0646\u062f.',
                'release_date': datetime.date(2014, 11, 7),
                'duration': 169,
                'director': 'Christopher Nolan',
                'cast': 'Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine, Matt Damon',
                'rating': 9.4,
                'trailer_url': 'https://www.youtube.com/watch?v=zSWdZVtXT7E',
                'genres': ['sci-fi', 'drama', 'adventure'],
            },
            {
                'title': 'The Godfather',
                'slug': 'the-godfather',
                'description': '\u062f\u0627\u0633\u062a\u0627\u0646 \u062e\u0627\u0646\u0648\u0627\u062f\u0647 \u06a9\u0648\u0631\u0644\u0626\u0648\u0646\u0647\u060c \u06cc\u06a9\u06cc \u0627\u0632 \u0642\u062f\u0631\u062a\u0645\u0646\u062f\u062a\u0631\u06cc\u0646 \u062e\u0627\u0646\u0648\u0627\u062f\u0647\u200c\u0647\u0627\u06cc \u0645\u0627\u0641\u06cc\u0627\u06cc\u06cc \u0622\u0645\u0631\u06cc\u06a9\u0627. \u0645\u0627\u06cc\u06a9\u0644 \u06a9\u0648\u0631\u0644\u0626\u0648\u0646\u0647 \u0646\u0627\u0686\u0627\u0631 \u0645\u06cc\u200c\u0634\u0648\u062f \u062c\u0627\u06cc \u067e\u062f\u0631\u0634 \u0631\u0627 \u0628\u06af\u06cc\u0631\u062f.',
                'release_date': datetime.date(1972, 3, 24),
                'duration': 175,
                'director': 'Francis Ford Coppola',
                'cast': 'Marlon Brando, Al Pacino, James Caan, Robert Duvall, Diane Keaton',
                'rating': 9.6,
                'trailer_url': 'https://www.youtube.com/watch?v=UaVTIH8mujA',
                'genres': ['crime', 'drama'],
            },
            {
                'title': 'Parasite',
                'slug': 'parasite',
                'description': '\u062e\u0627\u0646\u0648\u0627\u062f\u0647\u200c\u0627\u06cc \u0641\u0642\u06cc\u0631 \u06a9\u0647 \u062f\u0631 \u0632\u06cc\u0631\u0632\u0645\u06cc\u0646 \u0632\u0646\u062f\u06af\u06cc \u0645\u06cc\u200c\u06a9\u0646\u0646\u062f\u060c \u0628\u0647 \u062a\u062f\u0631\u06cc\u062c \u0648\u0627\u0631\u062f \u0632\u0646\u062f\u06af\u06cc \u062e\u0627\u0646\u0648\u0627\u062f\u0647\u200c\u0627\u06cc \u062b\u0631\u0648\u062a\u0645\u0646\u062f \u0645\u06cc\u200c\u0634\u0648\u0646\u062f. \u0627\u0645\u0627 \u0631\u0627\u0632\u0647\u0627\u06cc \u067e\u0646\u0647\u0627\u0646 \u0648 \u0637\u0628\u0642\u0627\u062a \u0627\u062c\u062a\u0645\u0627\u0639\u06cc \u0628\u0647 \u0641\u0627\u062c\u0639\u0647\u200c\u0627\u06cc \u063a\u06cc\u0631\u0645\u0646\u062a\u0638\u0631\u0647 \u0645\u0646\u062c\u0631 \u0645\u06cc\u200c\u0634\u0648\u062f.',
                'release_date': datetime.date(2019, 5, 30),
                'duration': 132,
                'director': 'Bong Joon-ho',
                'cast': 'Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong, Choi Woo-shik, Park So-dam',
                'rating': 9.0,
                'trailer_url': 'https://www.youtube.com/watch?v=5xH0HfJHsaY',
                'genres': ['drama', 'thriller', 'comedy'],
            },
            {
                'title': 'Spider-Man: Across the Spider-Verse',
                'slug': 'spider-man-spider-verse',
                'description': '\u0645\u0627\u06cc\u0644\u0632 \u0645\u0648\u0631\u0627\u0644\u0632 \u0628\u0627\u0631 \u062f\u06cc\u06af\u0631 \u0628\u0647 \u0645\u0648\u0644\u062a\u06cc\u200c\u0648\u0631\u0633 \u0633\u0641\u0631 \u0645\u06cc\u200c\u06a9\u0646\u062f \u0648 \u0628\u0627 \u06af\u0648\u0626\u0646 \u0627\u0633\u062a\u06cc\u0633\u06cc \u0648 \u062a\u06cc\u0645 \u062c\u062f\u06cc\u062f\u06cc \u0627\u0632 \u0645\u0631\u062f\u0627\u0646 \u0639\u0646\u06a9\u0628\u0648\u062a\u06cc \u0645\u0644\u0627\u0642\u0627\u062a \u0645\u06cc\u200c\u06a9\u0646\u062f.',
                'release_date': datetime.date(2023, 6, 2),
                'duration': 140,
                'director': 'Joaquim Dos Santos, Kemp Powers, Justin K. Thompson',
                'cast': 'Shameik Moore, Hailee Steinfeld, Brian Tyree Henry, Oscar Isaac',
                'rating': 8.8,
                'trailer_url': 'https://www.youtube.com/watch?v=shW9i6k8cB0',
                'genres': ['animation', 'action', 'adventure'],
            },
            {
                'title': 'Joker',
                'slug': 'joker',
                'description': '\u0622\u0631\u062a\u0648\u0631 \u0641\u0644\u06a9\u060c \u06cc\u06a9 \u06a9\u0645\u062f\u06cc\u0646 \u0634\u06a9\u0633\u062a\u200c\u062e\u0648\u0631\u062f\u0647 \u062f\u0631 \u06af\u0648\u0627\u062a\u0647\u0627\u0645\u060c \u067e\u0633 \u0627\u0632 \u062a\u062c\u0631\u0628\u0647 \u0628\u06cc\u200c\u0631\u062d\u0645\u06cc\u200c\u0647\u0627\u06cc \u0627\u062c\u062a\u0645\u0627\u0639\u06cc \u0648 \u0634\u062e\u0635\u06cc\u060c \u0628\u0647 \u062a\u062f\u0631\u06cc\u062c \u0628\u0647 \u062c\u0648\u06a9\u0631 \u062a\u0628\u062f\u06cc\u0644 \u0645\u06cc\u200c\u0634\u0648\u062f.',
                'release_date': datetime.date(2019, 10, 4),
                'duration': 122,
                'director': 'Todd Phillips',
                'cast': 'Joaquin Phoenix, Robert De Niro, Zazie Beetz, Frances Conroy',
                'rating': 8.9,
                'trailer_url': 'https://www.youtube.com/watch?v=zAGVQLHvwOY',
                'genres': ['drama', 'crime', 'thriller'],
            },
            {
                'title': 'Dune',
                'slug': 'dune',
                'description': '\u067e\u0644 \u0622\u062a\u0631\u06cc\u062f\u0633\u060c \u0641\u0631\u0632\u0646\u062f \u06cc\u06a9 \u062e\u0627\u0646\u0648\u0627\u062f\u0647 \u0627\u0634\u0631\u0627\u0641\u06cc\u060c \u0628\u0627\u06cc\u062f \u0628\u0647 \u0633\u06cc\u0627\u0631\u0647 \u062e\u0637\u0631\u0646\u0627\u06a9 \u0622\u0631\u0627\u06a9\u06cc\u0633 \u0633\u0641\u0631 \u06a9\u0646\u062f \u062a\u0627 \u0622\u06cc\u0646\u062f\u0647 \u062e\u0627\u0646\u0648\u0627\u062f\u0647 \u0648 \u0628\u0634\u0631\u06cc\u062a \u0631\u0627 \u0646\u062c\u0627\u062a \u062f\u0647\u062f.',
                'release_date': datetime.date(2021, 10, 22),
                'duration': 155,
                'director': 'Denis Villeneuve',
                'cast': 'Timoth\u00e9e Chalamet, Zendaya, Oscar Isaac, Rebecca Ferguson, Josh Brolin',
                'rating': 8.7,
                'trailer_url': 'https://www.youtube.com/watch?v=8g18jFHCLXk',
                'genres': ['sci-fi', 'adventure', 'drama'],
            },
            {
                'title': 'The Grand Budapest Hotel',
                'slug': 'grand-budapest-hotel',
                'description': '\u0645\u0627\u062c\u0631\u0627\u0647\u0627\u06cc \u06af\u0648\u0633\u062a\u0627\u0648\u060c \u0633\u0631\u067e\u0631\u0633\u062a \u0627\u0641\u0633\u0627\u0646\u0647\u200c\u0627\u06cc \u0647\u062a\u0644 \u0628\u0632\u0631\u06af \u0628\u0648\u062f\u0627\u067e\u0633\u062a\u060c \u0648 \u067e\u06cc\u0634\u062e\u062f\u0645\u062a \u062c\u0648\u0627\u0646\u0634 \u0632\u06cc\u0631\u0648. \u0622\u0646\u0647\u0627 \u062f\u0631\u06af\u06cc\u0631 \u0633\u0631\u0642\u062a \u06cc\u06a9 \u0646\u0642\u0627\u0634\u06cc \u0627\u0631\u0632\u0634\u0645\u0646\u062f \u0648 \u0646\u0628\u0631\u062f \u0628\u0631\u0627\u06cc \u0627\u0631\u062b \u06cc\u06a9 \u062e\u0627\u0646\u0648\u0627\u062f\u0647 \u062b\u0631\u0648\u062a\u0645\u0646\u062f \u0645\u06cc\u200c\u0634\u0648\u0646\u062f.',
                'release_date': datetime.date(2014, 3, 28),
                'duration': 99,
                'director': 'Wes Anderson',
                'cast': 'Ralph Fiennes, Tony Revolori, F. Murray Abraham, Mathieu Amalric',
                'rating': 8.5,
                'trailer_url': 'https://www.youtube.com/watch?v=1Fg5iWmQjwk',
                'genres': ['comedy', 'adventure', 'crime'],
            },
            {
                'title': 'Oppenheimer',
                'slug': 'oppenheimer',
                'description': '\u062f\u0627\u0633\u062a\u0627\u0646 \u062c\u06cc. \u0631\u0627\u0628\u0631\u062a \u0627\u0648\u067e\u0646\u0647\u0627\u06cc\u0645\u0631\u060c \u0641\u06cc\u0632\u06cc\u06a9\u062f\u0627\u0646\u06cc \u06a9\u0647 \u0631\u0647\u0628\u0631\u06cc \u067e\u0631\u0648\u0698\u0647 \u0645\u0646\u0647\u062a\u0627\u0646 \u0631\u0627 \u0628\u0631 \u0639\u0647\u062f\u0647 \u062f\u0627\u0634\u062a \u0648 \u0628\u0645\u0628 \u0627\u062a\u0645\u06cc \u0631\u0627 \u0633\u0627\u062e\u062a. \u0641\u06cc\u0644\u0645\u06cc \u062f\u0631\u0628\u0627\u0631\u0647 \u067e\u06cc\u0627\u0645\u062f\u0647\u0627\u06cc \u0627\u062e\u0644\u0627\u0642\u06cc \u0648 \u0633\u06cc\u0627\u0633\u06cc.',
                'release_date': datetime.date(2023, 7, 21),
                'duration': 180,
                'director': 'Christopher Nolan',
                'cast': 'Cillian Murphy, Emily Blunt, Matt Damon, Robert Downey Jr., Florence Pugh',
                'rating': 9.1,
                'trailer_url': 'https://www.youtube.com/watch?v=uYPbbksJxIg',
                'genres': ['drama', 'thriller'],
            },
        ]

        movies = {}
        for m in movies_data:
            genre_slugs = m.pop('genres')
            movie, created = Movie.objects.get_or_create(slug=m['slug'], defaults=m)
            if created:
                for gs in genre_slugs:
                    movie.genres.add(genres[gs])
                self.stdout.write(f'  Created movie: {m["title"]}')
            movies[m['slug']] = movie

        # --- Series ---
        series_data = [
            {
                'title': 'Breaking Bad',
                'slug': 'breaking-bad',
                'description': '\u0648\u0627\u0644\u062a\u0631 \u0648\u0627\u06cc\u062a\u060c \u0645\u0639\u0644\u0645 \u0634\u06cc\u0645\u06cc \u0628\u0627\u0632\u0646\u062f\u0647\u200c\u0627\u06cc \u06a9\u0647 \u0628\u0647 \u0633\u0631\u0637\u0627\u0646 \u0631\u06cc\u0647 \u0645\u0628\u062a\u0644\u0627 \u0634\u062f\u0647\u060c \u0628\u0627 \u0634\u0627\u06af\u0631\u062f \u0633\u0627\u0628\u0642\u0634 \u062c\u0633\u06cc \u067e\u06cc\u0646\u06a9\u0645\u0646 \u0634\u0631\u0648\u0639 \u0628\u0647 \u062a\u0648\u0644\u06cc\u062f \u0645\u062a\u200c\u0622\u0645\u0641\u062a\u0627\u0645\u06cc\u0646 \u0645\u06cc\u200c\u06a9\u0646\u062f.',
                'release_date': datetime.date(2008, 1, 20),
                'seasons_count': 5,
                'status': 'ended',
                'creator': 'Vince Gilligan',
                'cast': 'Bryan Cranston, Aaron Paul, Anna Gunn, Dean Norris, Bob Odenkirk',
                'rating': 9.7,
                'trailer_url': 'https://www.youtube.com/watch?v=HhesaQXLuRY',
                'genres': ['drama', 'crime', 'thriller'],
            },
            {
                'title': 'Game of Thrones',
                'slug': 'game-of-thrones',
                'description': '\u0647\u0641\u062a \u062e\u0627\u0646\u0648\u0627\u062f\u0647 \u0627\u0634\u0631\u0627\u0641\u06cc \u0628\u0631\u0627\u06cc \u06a9\u0646\u062a\u0631\u0644 \u0633\u0631\u0632\u0645\u06cc\u0646 \u0648\u0633\u062a\u0631\u0648\u0633 \u0645\u06cc\u200c\u062c\u0646\u06af\u0646\u062f. \u062f\u0627\u0633\u062a\u0627\u0646\u06cc \u062d\u0645\u0627\u0633\u06cc \u0627\u0632 \u0642\u062f\u0631\u062a\u060c \u062e\u06cc\u0627\u0646\u062a \u0648 \u0627\u0698\u062f\u0647\u0627.',
                'release_date': datetime.date(2011, 4, 17),
                'seasons_count': 8,
                'status': 'ended',
                'creator': 'David Benioff, D.B. Weiss',
                'cast': 'Emilia Clarke, Kit Harington, Peter Dinklage, Lena Headey, Maisie Williams',
                'rating': 9.3,
                'trailer_url': 'https://www.youtube.com/watch?v=KPLWWIOCOOQ',
                'genres': ['fantasy', 'drama', 'adventure'],
            },
            {
                'title': 'Stranger Things',
                'slug': 'stranger-things',
                'description': '\u062f\u0631 \u062f\u0647\u0647 \u06f1\u06f9\u06f8\u06f0\u060c \u0646\u0627\u067e\u062f\u06cc\u062f \u0634\u062f\u0646 \u06cc\u06a9 \u067e\u0633\u0631 \u062c\u0648\u0627\u0646 \u062f\u0631 \u0634\u0647\u0631 \u06a9\u0648\u0686\u06a9 \u0647\u0627\u0648\u06a9\u06cc\u0646\u0632\u060c \u062f\u0648\u0633\u062a\u0627\u0646\u0634 \u0631\u0627 \u0628\u0647 \u06a9\u0634\u0641 \u0646\u06cc\u0631\u0648\u0647\u0627\u06cc \u0641\u0631\u0627\u0637\u0628\u06cc\u0639\u06cc \u0633\u0648\u0642 \u0645\u06cc\u200c\u062f\u0647\u062f.',
                'release_date': datetime.date(2016, 7, 15),
                'seasons_count': 4,
                'status': 'ongoing',
                'creator': 'The Duffer Brothers',
                'cast': 'Millie Bobby Brown, Finn Wolfhard, Winona Ryder, David Harbour, Gaten Matarazzo',
                'rating': 9.0,
                'trailer_url': 'https://www.youtube.com/watch?v=b9EkMc79ZSU',
                'genres': ['sci-fi', 'horror', 'drama'],
            },
            {
                'title': 'Chernobyl',
                'slug': 'chernobyl',
                'description': '\u062f\u0627\u0633\u062a\u0627\u0646 \u0648\u0627\u0642\u0639\u06cc \u0641\u0627\u062c\u0639\u0647 \u0647\u0633\u062a\u0647\u200c\u0627\u06cc \u0686\u0631\u0646\u0648\u0628\u06cc\u0644 \u062f\u0631 \u0633\u0627\u0644 \u06f1\u06f9\u06f8\u06f6 \u0648 \u062a\u0644\u0627\u0634\u200c\u0647\u0627\u06cc \u0642\u0647\u0631\u0645\u0627\u0646\u0627\u0646\u0647 \u0628\u0631\u0627\u06cc \u0645\u0647\u0627\u0631 \u0622\u0646.',
                'release_date': datetime.date(2019, 5, 6),
                'seasons_count': 1,
                'status': 'ended',
                'creator': 'Craig Mazin',
                'cast': 'Jared Harris, Stellan Skarsg\u00e5rd, Emily Watson, Jessie Buckley',
                'rating': 9.5,
                'trailer_url': 'https://www.youtube.com/watch?v=s9APLXM9Ei8',
                'genres': ['drama', 'thriller'],
            },
            {
                'title': 'The Mandalorian',
                'slug': 'the-mandalorian',
                'description': '\u06cc\u06a9 \u0634\u06a9\u0627\u0631\u0686\u06cc \u062c\u0627\u06cc\u0632\u0647\u200c\u0628\u06af\u06cc\u0631 \u0645\u0627\u0646\u062f\u0644\u0648\u0631\u06cc\u0646\u06cc \u062f\u0631 \u06a9\u0647\u06a9\u0634\u0627\u0646\u06cc \u062f\u0648\u0631 \u0627\u0632 \u062c\u0646\u06af\u200c\u0647\u0627\u06cc \u0633\u062a\u0627\u0631\u0647\u200c\u0627\u06cc\u060c \u0645\u0623\u0645\u0648\u0631\u06cc\u062a \u067e\u06cc\u062f\u0627 \u0645\u06cc\u200c\u06a9\u0646\u062f \u062a\u0627 \u0627\u0632 \u06af\u0631\u0648\u06af\u0648\u0645\u0631\u0648\u0632 \u0645\u062d\u0627\u0641\u0638\u062a \u06a9\u0646\u062f.',
                'release_date': datetime.date(2019, 11, 12),
                'seasons_count': 3,
                'status': 'ongoing',
                'creator': 'Jon Favreau',
                'cast': 'Pedro Pascal, Carl Weathers, Gina Carano, Giancarlo Esposito',
                'rating': 8.8,
                'trailer_url': 'https://www.youtube.com/watch?v=aOC8E8z_ifw',
                'genres': ['sci-fi', 'action', 'adventure'],
            },
            {
                'title': 'Dark',
                'slug': 'dark-series',
                'description': '\u062f\u0631 \u0634\u0647\u0631 \u06a9\u0648\u0686\u06a9 \u0622\u0644\u0645\u0627\u0646\u06cc \u0648\u06cc\u0646\u062f\u0646\u060c \u0646\u0627\u067e\u062f\u06cc\u062f \u0634\u062f\u0646 \u06a9\u0648\u062f\u06a9\u0627\u0646 \u0631\u0627\u0632\u0647\u0627\u06cc \u0686\u0647\u0627\u0631 \u062e\u0627\u0646\u0648\u0627\u062f\u0647 \u0631\u0627 \u0641\u0627\u0634 \u0645\u06cc\u200c\u06a9\u0646\u062f. \u0633\u0641\u0631 \u062f\u0631 \u0632\u0645\u0627\u0646 \u0648 \u0631\u0648\u0627\u0628\u0637 \u067e\u06cc\u0686\u06cc\u062f\u0647 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc.',
                'release_date': datetime.date(2017, 12, 1),
                'seasons_count': 3,
                'status': 'ended',
                'creator': 'Baran bo Odar, Jantje Friese',
                'cast': 'Louis Hofmann, Karoline Eichhorn, Lisa Vicari, Maja Sch\u00f6ne',
                'rating': 9.2,
                'trailer_url': 'https://www.youtube.com/watch?v=ESEUoa-mz2c',
                'genres': ['sci-fi', 'thriller', 'drama'],
            },
            {
                'title': 'The Last of Us',
                'slug': 'the-last-of-us',
                'description': '\u0628\u06cc\u0633\u062a \u0633\u0627\u0644 \u067e\u0633 \u0627\u0632 \u0646\u0627\u0628\u0648\u062f\u06cc \u062a\u0645\u062f\u0646 \u0645\u062f\u0631\u0646\u060c \u062c\u0648\u0626\u0644\u060c \u06cc\u06a9 \u0628\u0627\u0632\u0645\u0627\u0646\u062f\u0647 \u0633\u062e\u062a\u200c\u06a9\u0648\u0634\u060c \u0645\u0623\u0645\u0648\u0631 \u0645\u06cc\u200c\u0634\u0648\u062f \u0627\u0644\u06cc\u060c \u062f\u062e\u062a\u0631 \u06f1\u06f4 \u0633\u0627\u0644\u0647\u200c\u0627\u06cc \u0631\u0627 \u0627\u0632 \u06cc\u06a9 \u0645\u0646\u0637\u0642\u0647 \u0642\u0631\u0646\u0637\u06cc\u0646\u0647 \u062e\u0627\u0631\u062c \u06a9\u0646\u062f.',
                'release_date': datetime.date(2023, 1, 15),
                'seasons_count': 2,
                'status': 'ongoing',
                'creator': 'Craig Mazin, Neil Druckmann',
                'cast': 'Pedro Pascal, Bella Ramsey, Gabriel Luna, Anna Torv',
                'rating': 9.1,
                'trailer_url': 'https://www.youtube.com/watch?v=uLtkt8BonwM',
                'genres': ['drama', 'action', 'thriller'],
            },
            {
                'title': 'Sherlock',
                'slug': 'sherlock',
                'description': '\u0646\u0633\u062e\u0647 \u0645\u062f\u0631\u0646 \u0634\u0631\u0644\u0648\u06a9 \u0647\u0644\u0645\u0632 \u062f\u0631 \u0644\u0646\u062f\u0646 \u0627\u0645\u0631\u0648\u0632\u06cc. \u0634\u0631\u0644\u0648\u06a9 \u0628\u0627 \u06a9\u0645\u06a9 \u062f\u06a9\u062a\u0631 \u0648\u0627\u062a\u0633\u0648\u0646 \u067e\u0631\u0648\u0646\u062f\u0647\u200c\u0647\u0627\u06cc \u067e\u06cc\u0686\u06cc\u062f\u0647 \u062c\u0646\u0627\u06cc\u06cc \u0631\u0627 \u062d\u0644 \u0645\u06cc\u200c\u06a9\u0646\u062f.',
                'release_date': datetime.date(2010, 7, 25),
                'seasons_count': 4,
                'status': 'ended',
                'creator': 'Mark Gatiss, Steven Moffat',
                'cast': 'Benedict Cumberbatch, Martin Freeman, Andrew Scott, Una Stubbs',
                'rating': 9.2,
                'trailer_url': 'https://www.youtube.com/watch?v=IWBjH4n5xSM',
                'genres': ['crime', 'drama', 'thriller'],
            },
        ]

        series = {}
        for s in series_data:
            genre_slugs = s.pop('genres')
            ser, created = Series.objects.get_or_create(slug=s['slug'], defaults=s)
            if created:
                for gs in genre_slugs:
                    ser.genres.add(genres[gs])
                self.stdout.write(f'  Created series: {s["title"]}')
            series[s['slug']] = ser

        # --- Reviews ---
        reviews_data = [
            {'user': 'ali', 'movie': 'inception', 'rating': 5, 'comment': '\u0634\u0627\u0647\u06a9\u0627\u0631 \u0646\u0648\u0644\u0627\u0646! \u0641\u06cc\u0644\u0645\u06cc \u06a9\u0647 \u0630\u0647\u0646 \u0634\u0645\u0627 \u0631\u0627 \u0628\u0647 \u0686\u0627\u0644\u0634 \u0645\u06cc\u200c\u06a9\u0634\u062f. \u0635\u062d\u0646\u0647\u200c\u0647\u0627\u06cc \u0631\u0648\u06cc\u0627\u06cc\u06cc \u0641\u0648\u0642\u200c\u0627\u0644\u0639\u0627\u062f\u0647 \u0637\u0631\u0627\u062d\u06cc \u0634\u062f\u0647\u200c\u0627\u0646\u062f.'},
            {'user': 'sara', 'movie': 'inception', 'rating': 4, 'comment': '\u0641\u06cc\u0644\u0645 \u0628\u0633\u06cc\u0627\u0631 \u0647\u0648\u0634\u0645\u0646\u062f\u0627\u0646\u0647\u200c\u0627\u06cc \u0627\u0633\u062a \u0627\u0645\u0627 \u06af\u0627\u0647\u06cc \u067e\u06cc\u0686\u06cc\u062f\u06af\u06cc \u062f\u0627\u0633\u062a\u0627\u0646 \u0628\u0627\u0639\u062b \u0633\u0631\u062f\u0631\u06af\u0645\u06cc \u0645\u06cc\u200c\u0634\u0648\u062f.'},
            {'user': 'mohammad', 'movie': 'inception', 'rating': 5, 'comment': '\u062a\u0631\u06a9\u06cc\u0628 \u0639\u0644\u0645\u06cc-\u062a\u062e\u06cc\u0644\u06cc \u0648 \u0647\u06cc\u062c\u0627\u0646\u200c\u0627\u0646\u06af\u06cc\u0632 \u0628\u06cc\u200c\u0646\u0638\u06cc\u0631. \u0645\u0648\u0633\u06cc\u0642\u06cc \u0647\u0627\u0646\u0633 \u0632\u06cc\u0645\u0631 \u0641\u0648\u0642\u200c\u0627\u0644\u0639\u0627\u062f\u0647 \u0627\u0633\u062a.'},
            {'user': 'ali', 'movie': 'shawshank-redemption', 'rating': 5, 'comment': '\u0628\u0647\u062a\u0631\u06cc\u0646 \u0641\u06cc\u0644\u0645 \u062a\u0627\u0631\u06cc\u062e \u0633\u06cc\u0646\u0645\u0627. \u062f\u0627\u0633\u062a\u0627\u0646 \u0627\u0645\u06cc\u062f \u0648 \u062f\u0648\u0633\u062a\u06cc \u062f\u0631 \u0633\u062e\u062a\u200c\u062a\u0631\u06cc\u0646 \u0634\u0631\u0627\u06cc\u0637.'},
            {'user': 'fateme', 'movie': 'shawshank-redemption', 'rating': 5, 'comment': '\u0641\u06cc\u0644\u0645\u06cc \u06a9\u0647 \u0647\u0631 \u0628\u0627\u0631 \u062a\u0645\u0627\u0634\u0627 \u06a9\u0646\u06cc\u062f \u0686\u06cc\u0632 \u062c\u062f\u06cc\u062f\u06cc \u062f\u0631 \u0622\u0646 \u06a9\u0634\u0641 \u0645\u06cc\u200c\u06a9\u0646\u06cc\u062f.'},
            {'user': 'reza', 'movie': 'dark-knight', 'rating': 5, 'comment': '\u0647\u06cc\u062b \u0644\u062c\u0631 \u062f\u0631 \u0646\u0642\u0634 \u062c\u0648\u06a9\u0631 \u06cc\u06a9\u06cc \u0627\u0632 \u0628\u0647\u062a\u0631\u06cc\u0646 \u0628\u0627\u0632\u06cc\u200c\u0647\u0627\u06cc \u062a\u0627\u0631\u06cc\u062e \u0633\u06cc\u0646\u0645\u0627\u0633\u062a.'},
            {'user': 'sara', 'movie': 'dark-knight', 'rating': 5, 'comment': '\u0646\u0648\u0644\u0627\u0646 \u062b\u0627\u0628\u062a \u06a9\u0631\u062f \u0641\u06cc\u0644\u0645\u200c\u0647\u0627\u06cc \u0627\u0628\u0631\u0642\u0647\u0631\u0645\u0627\u0646\u06cc \u0645\u06cc\u200c\u062a\u0648\u0627\u0646\u0646\u062f \u0639\u0645\u06cc\u0642 \u0648 \u062c\u062f\u06cc \u0628\u0627\u0634\u0646\u062f.'},
            {'user': 'ali', 'movie': 'dark-knight', 'rating': 4, 'comment': '\u0635\u062d\u0646\u0647\u200c\u0647\u0627\u06cc \u0627\u06a9\u0634\u0646 \u0639\u0627\u0644\u06cc \u0648 \u062f\u0627\u0633\u062a\u0627\u0646 \u067e\u0631\u06a9\u0634\u0634. \u0641\u0642\u0637 \u06a9\u0645\u06cc \u0637\u0648\u0644\u0627\u0646\u06cc \u0627\u0633\u062a.'},
            {'user': 'mohammad', 'movie': 'interstellar', 'rating': 5, 'comment': '\u0641\u06cc\u0644\u0645\u06cc \u06a9\u0647 \u0639\u0644\u0645 \u0648 \u0627\u062d\u0633\u0627\u0633 \u0631\u0627 \u0628\u0647 \u0632\u06cc\u0628\u0627\u06cc\u06cc \u062a\u0631\u06a9\u06cc\u0628 \u0645\u06cc\u200c\u06a9\u0646\u062f.'},
            {'user': 'fateme', 'movie': 'interstellar', 'rating': 4, 'comment': '\u062f\u0627\u0633\u062a\u0627\u0646 \u0639\u0627\u0634\u0642\u0627\u0646\u0647 \u0628\u06cc\u0646 \u067e\u062f\u0631 \u0648 \u062f\u062e\u062a\u0631 \u0628\u0633\u06cc\u0627\u0631 \u062a\u0623\u062b\u06cc\u0631\u06af\u0630\u0627\u0631.'},
            {'user': 'sara', 'movie': 'parasite', 'rating': 5, 'comment': '\u0628\u0648\u0646\u06af \u062c\u0648\u0646 \u0647\u0648 \u0628\u0627 \u0627\u06cc\u0646 \u0641\u06cc\u0644\u0645 \u0645\u0631\u0632\u0647\u0627\u06cc \u0633\u06cc\u0646\u0645\u0627 \u0631\u0627 \u062c\u0627\u0628\u062c\u0627 \u06a9\u0631\u062f.'},
            {'user': 'ali', 'movie': 'parasite', 'rating': 4, 'comment': '\u0641\u06cc\u0644\u0645\u06cc \u063a\u06cc\u0631\u0645\u0646\u062a\u0638\u0631\u0647 \u0628\u0627 \u067e\u06cc\u0686\u0634\u200c\u0647\u0627\u06cc \u062f\u0627\u0633\u062a\u0627\u0646\u06cc \u0634\u06af\u0641\u062a\u200c\u0627\u0646\u06af\u06cc\u0632.'},
            {'user': 'reza', 'movie': 'joker', 'rating': 5, 'comment': '\u0648\u0627\u06a9\u06cc\u0646 \u0641\u06cc\u0646\u06cc\u06a9\u0633 \u06cc\u06a9 \u0634\u0627\u0647\u06a9\u0627\u0631 \u0628\u0627\u0632\u06cc\u06af\u0631\u06cc \u0627\u0631\u0627\u0626\u0647 \u062f\u0627\u062f\u0647.'},
            {'user': 'sara', 'movie': 'joker', 'rating': 4, 'comment': '\u0641\u06cc\u0644\u0645 \u062c\u0633\u0648\u0631\u0627\u0646\u0647\u200c\u0627\u06cc \u0627\u0633\u062a \u0627\u0645\u0627 \u0628\u0631\u062e\u06cc \u0635\u062d\u0646\u0647\u200c\u0647\u0627 \u0628\u06cc\u0634 \u0627\u0632 \u062d\u062f \u062e\u0634\u0646 \u0647\u0633\u062a\u0646\u062f.'},
            {'user': 'mohammad', 'movie': 'dune', 'rating': 5, 'comment': '\u0627\u0642\u062a\u0628\u0627\u0633\u06cc \u0628\u0627\u0634\u06a9\u0648\u0647 \u0627\u0632 \u0631\u0645\u0627\u0646 \u0641\u0631\u0627\u0646\u06a9 \u0647\u0631\u0628\u0631\u062a.'},
            {'user': 'reza', 'movie': 'dune', 'rating': 4, 'comment': '\u0641\u06cc\u0644\u0645\u200c\u0633\u0627\u0632\u06cc \u062d\u0645\u0627\u0633\u06cc \u062f\u0631 \u0628\u0647\u062a\u0631\u06cc\u0646 \u062d\u0627\u0644\u062a.'},
            {'user': 'ali', 'movie': 'oppenheimer', 'rating': 5, 'comment': '\u0646\u0648\u0644\u0627\u0646 \u0628\u0627\u0631 \u062f\u06cc\u06af\u0631 \u062b\u0627\u0628\u062a \u06a9\u0631\u062f \u0627\u0633\u062a\u0627\u062f \u0632\u0645\u0627\u0646 \u0648 \u0631\u0648\u0627\u06cc\u062a \u0627\u0633\u062a.'},
            {'user': 'fateme', 'movie': 'oppenheimer', 'rating': 5, 'comment': '\u0641\u06cc\u0644\u0645\u06cc \u062f\u0631\u0628\u0627\u0631\u0647 \u0648\u062c\u062f\u0627\u0646 \u0628\u0634\u0631\u06cc \u0648 \u067e\u06cc\u0627\u0645\u062f\u0647\u0627\u06cc \u0639\u0644\u0645.'},
            {'user': 'reza', 'movie': 'spider-man-spider-verse', 'rating': 5, 'comment': '\u0628\u0647\u062a\u0631\u06cc\u0646 \u0627\u0646\u06cc\u0645\u06cc\u0634\u0646 \u0633\u0627\u0644! \u0637\u0631\u0627\u062d\u06cc \u062e\u06cc\u0631\u0647\u200c\u06a9\u0646\u0646\u062f\u0647.'},
            {'user': 'sara', 'movie': 'spider-man-spider-verse', 'rating': 4, 'comment': '\u062e\u0644\u0627\u0642\u0627\u0646\u0647 \u0648 \u0633\u0631\u06af\u0631\u0645\u200c\u06a9\u0646\u0646\u062f\u0647.'},
            {'user': 'ali', 'series': 'breaking-bad', 'rating': 5, 'comment': '\u0628\u0647\u062a\u0631\u06cc\u0646 \u0633\u0631\u06cc\u0627\u0644 \u062a\u0627\u0631\u06cc\u062e \u062a\u0644\u0648\u06cc\u0632\u06cc\u0648\u0646. \u062a\u062d\u0648\u0644 \u0648\u0627\u0644\u062a\u0631 \u0648\u0627\u06cc\u062a \u0628\u06cc\u200c\u0646\u0638\u06cc\u0631 \u0627\u0633\u062a.'},
            {'user': 'sara', 'series': 'breaking-bad', 'rating': 5, 'comment': '\u0647\u0631 \u0641\u0635\u0644 \u0628\u0647\u062a\u0631 \u0627\u0632 \u0642\u0628\u0644\u06cc. \u0628\u0631\u0627\u06cc\u0627\u0646 \u06a9\u0631\u0627\u0646\u0633\u062a\u0648\u0646 \u0634\u0627\u0647\u06a9\u0627\u0631 \u0628\u0627\u0632\u06cc\u06af\u0631\u06cc \u0627\u0631\u0627\u0626\u0647 \u062f\u0627\u062f\u0647.'},
            {'user': 'reza', 'series': 'breaking-bad', 'rating': 5, 'comment': '\u067e\u0627\u06cc\u0627\u0646\u200c\u0628\u0646\u062f\u06cc \u0639\u0627\u0644\u06cc. \u06cc\u06a9\u06cc \u0627\u0632 \u0645\u0639\u062f\u0648\u062f \u0633\u0631\u06cc\u0627\u0644\u200c\u0647\u0627\u06cc\u06cc \u06a9\u0647 \u067e\u0627\u06cc\u0627\u0646\u0634 \u0627\u0646\u062a\u0638\u0627\u0631\u0627\u062a \u0631\u0627 \u0628\u0631\u0622\u0648\u0631\u062f\u0647.'},
            {'user': 'mohammad', 'series': 'game-of-thrones', 'rating': 5, 'comment': '\u0641\u0635\u0644\u200c\u0647\u0627\u06cc \u0627\u0648\u0644 \u062a\u0627 \u0634\u0634\u0645 \u0634\u0627\u0647\u06a9\u0627\u0631 \u0647\u0633\u062a\u0646\u062f.'},
            {'user': 'fateme', 'series': 'game-of-thrones', 'rating': 4, 'comment': '\u0634\u0631\u0648\u0639 \u0641\u0648\u0642\u200c\u0627\u0644\u0639\u0627\u062f\u0647 \u0627\u0645\u0627 \u067e\u0627\u06cc\u0627\u0646\u200c\u0628\u0646\u062f\u06cc \u0646\u0627\u0627\u0645\u06cc\u062f\u06a9\u0646\u0646\u062f\u0647.'},
            {'user': 'ali', 'series': 'game-of-thrones', 'rating': 4, 'comment': '\u062a\u0648\u0644\u06cc\u062f \u0628\u06cc\u200c\u0646\u0638\u06cc\u0631 \u0648 \u0628\u0627\u0632\u06cc\u06af\u0631\u0627\u0646 \u0639\u0627\u0644\u06cc.'},
            {'user': 'reza', 'series': 'stranger-things', 'rating': 5, 'comment': '\u0646\u0648\u0633\u062a\u0627\u0644\u0698\u06cc \u062f\u0647\u0647 \u06f8\u06f0 \u0628\u0627 \u062f\u0627\u0633\u062a\u0627\u0646\u06cc \u0647\u06cc\u062c\u0627\u0646\u200c\u0627\u0646\u06af\u06cc\u0632.'},
            {'user': 'sara', 'series': 'stranger-things', 'rating': 4, 'comment': '\u0633\u0631\u06cc\u0627\u0644 \u0633\u0631\u06af\u0631\u0645\u200c\u06a9\u0646\u0646\u062f\u0647\u200c\u0627\u06cc \u0628\u0627 \u0634\u062e\u0635\u06cc\u062a\u200c\u0647\u0627\u06cc \u062f\u0648\u0633\u062a\u200c\u062f\u0627\u0634\u062a\u0646\u06cc.'},
            {'user': 'ali', 'series': 'chernobyl', 'rating': 5, 'comment': '\u062a\u06a9\u0627\u0646\u200c\u062f\u0647\u0646\u062f\u0647 \u0648 \u0648\u0627\u0642\u0639\u06cc. \u0628\u0647\u062a\u0631\u06cc\u0646 \u0645\u06cc\u0646\u06cc\u200c\u0633\u0631\u06cc\u0627\u0644 \u062a\u0627\u0631\u06cc\u062e.'},
            {'user': 'fateme', 'series': 'chernobyl', 'rating': 5, 'comment': '\u0645\u0633\u062a\u0646\u062f-\u062f\u0631\u0627\u0645\u06cc \u06a9\u0647 \u0646\u0628\u0627\u06cc\u062f \u0627\u0632 \u062f\u0633\u062a \u062f\u0627\u062f.'},
            {'user': 'mohammad', 'series': 'dark-series', 'rating': 5, 'comment': '\u067e\u06cc\u0686\u06cc\u062f\u0647\u200c\u062a\u0631\u06cc\u0646 \u0648 \u0647\u0648\u0634\u0645\u0646\u062f\u0627\u0646\u0647\u200c\u062a\u0631\u06cc\u0646 \u0633\u0631\u06cc\u0627\u0644\u06cc \u06a9\u0647 \u062a\u0645\u0627\u0634\u0627 \u06a9\u0631\u062f\u0647\u200c\u0627\u0645.'},
            {'user': 'ali', 'series': 'dark-series', 'rating': 5, 'comment': '\u0633\u0641\u0631 \u062f\u0631 \u0632\u0645\u0627\u0646 \u0628\u0647 \u0628\u0647\u062a\u0631\u06cc\u0646 \u0634\u06a9\u0644 \u0645\u0645\u06a9\u0646. \u0622\u0644\u0645\u0627\u0646\u06cc\u200c\u0647\u0627 \u062b\u0627\u0628\u062a \u06a9\u0631\u062f\u0646\u062f \u0633\u0631\u06cc\u0627\u0644\u200c\u0633\u0627\u0632\u06cc \u0628\u0644\u062f\u0646\u062f.'},
            {'user': 'sara', 'series': 'the-last-of-us', 'rating': 5, 'comment': '\u0628\u0647\u062a\u0631\u06cc\u0646 \u0627\u0642\u062a\u0628\u0627\u0633 \u0627\u0632 \u0628\u0627\u0632\u06cc \u0648\u06cc\u062f\u06cc\u0648\u06cc\u06cc \u062a\u0627 \u0628\u0647 \u0627\u0645\u0631\u0648\u0632.'},
            {'user': 'reza', 'series': 'the-last-of-us', 'rating': 5, 'comment': '\u0641\u0648\u0642\u200c\u0627\u0644\u0639\u0627\u062f\u0647 \u0627\u062d\u0633\u0627\u0633\u06cc \u0648 \u0648\u0641\u0627\u062f\u0627\u0631 \u0628\u0647 \u0628\u0627\u0632\u06cc.'},
            {'user': 'fateme', 'series': 'sherlock', 'rating': 5, 'comment': '\u0628\u0646\u062f\u06cc\u06a9\u062a \u06a9\u0627\u0645\u0628\u0631\u0628\u062a\u0686 \u0628\u0647\u062a\u0631\u06cc\u0646 \u0634\u0631\u0644\u0648\u06a9 \u0647\u0644\u0645\u0632 \u062a\u0627\u0631\u06cc\u062e.'},
            {'user': 'mohammad', 'series': 'sherlock', 'rating': 4, 'comment': '\u0641\u0635\u0644 \u0627\u0648\u0644 \u0648 \u062f\u0648\u0645 \u0639\u0627\u0644\u06cc. \u0641\u0635\u0644\u200c\u0647\u0627\u06cc \u0628\u0639\u062f\u06cc \u06a9\u0645\u06cc \u0627\u0641\u062a \u06a9\u06cc\u0641\u06cc\u062a \u062f\u0627\u0631\u0646\u062f.'},
            {'user': 'reza', 'series': 'the-mandalorian', 'rating': 5, 'comment': '\u0628\u0627\u0632\u06af\u0634\u062a \u0628\u0627\u0634\u06a9\u0648\u0647 \u062c\u0646\u06af \u0633\u062a\u0627\u0631\u06af\u0627\u0646. \u06af\u0631\u0648\u06a9\u0648 \u0628\u0627\u0645\u0632\u0647\u200c\u062a\u0631\u06cc\u0646 \u0634\u062e\u0635\u06cc\u062a \u062a\u0627\u0631\u06cc\u062e \u062a\u0644\u0648\u06cc\u0632\u06cc\u0648\u0646!'},
            {'user': 'sara', 'series': 'the-mandalorian', 'rating': 4, 'comment': '\u0648\u0633\u062a\u0631\u0646 \u0641\u0636\u0627\u06cc\u06cc \u0639\u0627\u0644\u06cc. \u0647\u0631 \u0642\u0633\u0645\u062a \u06cc\u06a9 \u0645\u0627\u062c\u0631\u0627\u062c\u0648\u06cc\u06cc \u062c\u0630\u0627\u0628.'},
        ]

        for r in reviews_data:
            user = users[r['user']]
            movie_slug = r.get('movie')
            series_slug = r.get('series')

            if movie_slug:
                movie = movies[movie_slug]
                Review.objects.get_or_create(
                    user=user, movie=movie, defaults={'rating': r['rating'], 'comment': r['comment']}
                )
            elif series_slug:
                ser = series[series_slug]
                Review.objects.get_or_create(
                    user=user, series=ser, defaults={'rating': r['rating'], 'comment': r['comment']}
                )

        self.stdout.write(f'  Created {len(reviews_data)} reviews')

        # --- Watchlist Items ---
        watchlist_data = [
            {'user': 'ali', 'movie': 'interstellar'},
            {'user': 'ali', 'series': 'breaking-bad'},
            {'user': 'ali', 'movie': 'dune'},
            {'user': 'sara', 'movie': 'parasite'},
            {'user': 'sara', 'series': 'the-last-of-us'},
            {'user': 'sara', 'movie': 'oppenheimer'},
            {'user': 'mohammad', 'series': 'dark-series'},
            {'user': 'mohammad', 'movie': 'dune'},
            {'user': 'mohammad', 'series': 'the-mandalorian'},
            {'user': 'fateme', 'movie': 'shawshank-redemption'},
            {'user': 'fateme', 'series': 'chernobyl'},
            {'user': 'reza', 'movie': 'dark-knight'},
            {'user': 'reza', 'series': 'stranger-things'},
            {'user': 'reza', 'movie': 'spider-man-spider-verse'},
        ]

        for w in watchlist_data:
            user = users[w['user']]
            movie_slug = w.get('movie')
            series_slug = w.get('series')

            if movie_slug:
                WatchlistItem.objects.get_or_create(user=user, movie=movies[movie_slug])
            elif series_slug:
                WatchlistItem.objects.get_or_create(user=user, series=series[series_slug])

        self.stdout.write(f'  Created {len(watchlist_data)} watchlist items')

        self.stdout.write(self.style.SUCCESS('\nSample data created successfully!'))
        self.stdout.write(self.style.SUCCESS(f'  - {len(genres_data)} genres'))
        self.stdout.write(self.style.SUCCESS(f'  - {len(users_data)} users (password: testpass123)'))
        self.stdout.write(self.style.SUCCESS(f'  - {len(movies_data)} movies'))
        self.stdout.write(self.style.SUCCESS(f'  - {len(series_data)} series'))
        self.stdout.write(self.style.SUCCESS(f'  - {len(reviews_data)} reviews'))
        self.stdout.write(self.style.SUCCESS(f'  - {len(watchlist_data)} watchlist items'))
