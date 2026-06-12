from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'slug': self.slug})


class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/movies/', blank=True, null=True)
    poster_url = models.URLField(blank=True, help_text='External poster image URL (e.g. TMDB)')
    backdrop = models.ImageField(upload_to='backdrops/movies/', blank=True, null=True)
    backdrop_url = models.URLField(blank=True, help_text='External backdrop image URL')
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    director = models.CharField(max_length=200)
    cast = models.TextField(blank=True, help_text='Comma-separated cast names')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    genres = models.ManyToManyField(Genre, related_name='movies')
    trailer_url = models.URLField(blank=True, help_text='YouTube trailer URL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('movies:movie_detail', kwargs={'slug': self.slug})

    def get_stars(self):
        """Return rating as a list for star display (out of 5)."""
        full = int(self.rating // 2)
        half = 1 if (self.rating % 2) >= 1 else 0
        empty = 5 - full - half
        return {'full': range(full), 'half': half, 'empty': range(empty)}

    def get_cast_list(self):
        return [c.strip() for c in self.cast.split(',') if c.strip()] if self.cast else []

    def get_poster_url(self):
        if self.poster:
            return self.poster.url
        if self.poster_url:
            return self.poster_url
        return None

    def get_backdrop_url(self):
        if self.backdrop:
            return self.backdrop.url
        if self.backdrop_url:
            return self.backdrop_url
        return None


class Series(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('ended', 'Ended'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/series/', blank=True, null=True)
    poster_url = models.URLField(blank=True, help_text='External poster image URL (e.g. TMDB)')
    backdrop = models.ImageField(upload_to='backdrops/series/', blank=True, null=True)
    backdrop_url = models.URLField(blank=True, help_text='External backdrop image URL')
    release_date = models.DateField()
    seasons_count = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    creator = models.CharField(max_length=200, blank=True)
    cast = models.TextField(blank=True, help_text='Comma-separated cast names')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    genres = models.ManyToManyField(Genre, related_name='series')
    trailer_url = models.URLField(blank=True, help_text='YouTube trailer URL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'series'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('series:series_detail', kwargs={'slug': self.slug})

    def get_stars(self):
        full = int(self.rating // 2)
        half = 1 if (self.rating % 2) >= 1 else 0
        empty = 5 - full - half
        return {'full': range(full), 'half': half, 'empty': range(empty)}

    def get_cast_list(self):
        return [c.strip() for c in self.cast.split(',') if c.strip()] if self.cast else []

    def get_poster_url(self):
        if self.poster:
            return self.poster.url
        if self.poster_url:
            return self.poster_url
        return None

    def get_backdrop_url(self):
        if self.backdrop:
            return self.backdrop.url
        if self.backdrop_url:
            return self.backdrop_url
        return None


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(movie__isnull=False, series__isnull=True) |
                    models.Q(movie__isnull=True, series__isnull=False)
                ),
                name='review_one_media_type',
            )
        ]

    def __str__(self):
        media = self.movie or self.series
        return f'{self.user.username} - {media.title} ({self.rating}/5)'


class WatchlistItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='watchlist_items')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True, related_name='watchlisted_by')
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True, related_name='watchlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_at']
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(movie__isnull=False, series__isnull=True) |
                    models.Q(movie__isnull=True, series__isnull=False)
                ),
                name='watchlist_one_media_type',
            )
        ]

    def __str__(self):
        media = self.movie or self.series
        return f'{self.user.username} - {media.title}'
