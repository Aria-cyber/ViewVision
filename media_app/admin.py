from django.contrib import admin
from .models import Genre, Movie, Series, Review, WatchlistItem


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'release_date', 'duration', 'rating']
    list_filter = ['genres', 'release_date']
    search_fields = ['title', 'director', 'cast']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['genres']


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'seasons_count', 'status', 'rating']
    list_filter = ['genres', 'status', 'release_date']
    search_fields = ['title', 'creator', 'cast']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['genres']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_media_title', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'comment']

    def get_media_title(self, obj):
        return (obj.movie or obj.series).title
    get_media_title.short_description = 'Media'


@admin.register(WatchlistItem)
class WatchlistItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_media_title', 'added_at']
    list_filter = ['added_at']
    search_fields = ['user__username']

    def get_media_title(self, obj):
        return (obj.movie or obj.series).title
    get_media_title.short_description = 'Media'
