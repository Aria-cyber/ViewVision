from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Movie, Series, Genre, Review, WatchlistItem
from .forms import ReviewForm

ITEMS_PER_PAGE = 12


def home(request):
    trending_movies = Movie.objects.order_by('-rating')[:6]
    trending_series = Series.objects.order_by('-rating')[:6]
    recent_movies = Movie.objects.order_by('-release_date')[:6]
    recent_series = Series.objects.order_by('-release_date')[:6]
    genres = Genre.objects.all()[:10]
    total_movies = Movie.objects.count()
    total_series = Series.objects.count()
    total_genres = Genre.objects.count()
    context = {
        'trending_movies': trending_movies,
        'trending_series': trending_series,
        'recent_movies': recent_movies,
        'recent_series': recent_series,
        'genres': genres,
        'total_movies': total_movies,
        'total_series': total_series,
        'total_genres': total_genres,
    }
    return render(request, 'home.html', context)


def movie_list(request):
    movies = Movie.objects.all()
    genre_slug = request.GET.get('genre')
    sort = request.GET.get('sort', '-created_at')
    if genre_slug:
        movies = movies.filter(genres__slug=genre_slug)
    if sort in ['title', '-title', 'rating', '-rating', 'release_date', '-release_date']:
        movies = movies.order_by(sort)

    paginator = Paginator(movies, ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    genres = Genre.objects.all()
    query_params = ''
    if genre_slug:
        query_params += f'genre={genre_slug}&'
    if sort != '-created_at':
        query_params += f'sort={sort}&'
    query_params = query_params.rstrip('&')

    context = {'movies': page_obj, 'page_obj': page_obj, 'genres': genres, 'current_sort': sort, 'current_genre': genre_slug, 'query_params': query_params}
    return render(request, 'media_app/movie_list.html', context)


def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    reviews = movie.reviews.select_related('user').all()
    in_watchlist = False
    if request.user.is_authenticated:
        in_watchlist = WatchlistItem.objects.filter(user=request.user, movie=movie).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد.')
            return redirect('movies:movie_detail', slug=slug)
    else:
        form = ReviewForm()

    context = {
        'movie': movie,
        'reviews': reviews,
        'form': form,
        'in_watchlist': in_watchlist,
    }
    return render(request, 'media_app/movie_detail.html', context)


def series_list(request):
    series = Series.objects.all()
    genre_slug = request.GET.get('genre')
    sort = request.GET.get('sort', '-created_at')
    if genre_slug:
        series = series.filter(genres__slug=genre_slug)
    if sort in ['title', '-title', 'rating', '-rating', 'release_date', '-release_date']:
        series = series.order_by(sort)

    paginator = Paginator(series, ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    genres = Genre.objects.all()
    query_params = ''
    if genre_slug:
        query_params += f'genre={genre_slug}&'
    if sort != '-created_at':
        query_params += f'sort={sort}&'
    query_params = query_params.rstrip('&')

    context = {'series_list': page_obj, 'page_obj': page_obj, 'genres': genres, 'current_sort': sort, 'current_genre': genre_slug, 'query_params': query_params}
    return render(request, 'media_app/series_list.html', context)


def series_detail(request, slug):
    series = get_object_or_404(Series, slug=slug)
    reviews = series.reviews.select_related('user').all()
    in_watchlist = False
    if request.user.is_authenticated:
        in_watchlist = WatchlistItem.objects.filter(user=request.user, series=series).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.series = series
            review.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد.')
            return redirect('series:series_detail', slug=slug)
    else:
        form = ReviewForm()

    context = {
        'series': series,
        'reviews': reviews,
        'form': form,
        'in_watchlist': in_watchlist,
    }
    return render(request, 'media_app/series_detail.html', context)


def search(request):
    query = request.GET.get('q', '').strip()
    movies = Movie.objects.none()
    series = Series.objects.none()
    if query:
        movies = Movie.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(director__icontains=query)
        )
        series = Series.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(creator__icontains=query)
        )

    movies_paginator = Paginator(movies, ITEMS_PER_PAGE)
    series_paginator = Paginator(series, ITEMS_PER_PAGE)
    movies_page = movies_paginator.get_page(request.GET.get('movies_page'))
    series_page = series_paginator.get_page(request.GET.get('series_page'))

    query_params = f'q={query}' if query else ''

    context = {
        'query': query,
        'query_params': query_params,
        'movies': movies_page,
        'series': series_page,
        'movies_page_obj': movies_page,
        'series_page_obj': series_page,
        'total_movies': movies.count(),
        'total_series': series.count(),
    }
    return render(request, 'media_app/search_results.html', context)


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'media_app/genre_list.html', {'genres': genres})


def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    movies = genre.movies.all()
    series = genre.series.all()

    movies_paginator = Paginator(movies, ITEMS_PER_PAGE)
    series_paginator = Paginator(series, ITEMS_PER_PAGE)
    movies_page = movies_paginator.get_page(request.GET.get('movies_page'))
    series_page = series_paginator.get_page(request.GET.get('series_page'))

    context = {
        'genre': genre,
        'movies': movies_page,
        'series': series_page,
        'movies_page_obj': movies_page,
        'series_page_obj': series_page,
    }
    return render(request, 'media_app/genre_detail.html', context)


@login_required
def watchlist(request):
    items = WatchlistItem.objects.filter(user=request.user).select_related('movie', 'series')
    return render(request, 'media_app/watchlist.html', {'items': items})


@login_required
def toggle_watchlist(request, content_type, object_id):
    if content_type == 'movie':
        movie = get_object_or_404(Movie, pk=object_id)
        item, created = WatchlistItem.objects.get_or_create(user=request.user, movie=movie)
        if created:
            messages.success(request, f'«{movie.title}» به لیست تماشای شما اضافه شد.')
        else:
            item.delete()
            messages.info(request, f'«{movie.title}» از لیست تماشای شما حذف شد.')
        return redirect('movies:movie_detail', slug=movie.slug)
    elif content_type == 'series':
        series = get_object_or_404(Series, pk=object_id)
        item, created = WatchlistItem.objects.get_or_create(user=request.user, series=series)
        if created:
            messages.success(request, f'«{series.title}» به لیست تماشای شما اضافه شد.')
        else:
            item.delete()
            messages.info(request, f'«{series.title}» از لیست تماشای شما حذف شد.')
        return redirect('series:series_detail', slug=series.slug)
    return redirect('home')
