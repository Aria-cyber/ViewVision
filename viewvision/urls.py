from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from media_app import views as media_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', media_views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('movies/', include('media_app.movie_urls')),
    path('series/', include('media_app.series_urls')),
    path('search/', media_views.search, name='search'),
    path('genres/', media_views.genre_list, name='genre_list'),
    path('genre/<slug:slug>/', media_views.genre_detail, name='genre_detail'),
    path('watchlist/', media_views.watchlist, name='watchlist'),
    path('watchlist/toggle/<str:content_type>/<int:object_id>/',
         media_views.toggle_watchlist, name='toggle_watchlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
