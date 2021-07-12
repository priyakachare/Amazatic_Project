"""Amazatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from artists.views import ArtistsList, Artists, ArtistDetail, ArtistPage
from genres.views import GenresList, Genres, GenresDetail, GenrePage
from movies.views import MoviesList, MoviesDetail, HomePage, MoviePage, Movies
from login.views import LoginPage, LogOut

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', LoginPage, name="LoginPage"),
    path('logout', LogOut, name="LogOutPage"),
    path('movie-add',MoviePage,name="movie-add"),
    path('genre-add',GenrePage, name="genre-add"),
    path('artist-add',ArtistPage, name="artist-add"),
    path('home', HomePage, name="home"),


    # URLS for Artists
    path('artists/list',ArtistsList.as_view(), name="list_of_artists"),
    path('artists',Artists.as_view(), name="add_artists"),
    path('artist/<uuid:id_string>',ArtistDetail.as_view(), name="get_artists"),

    # URLS for Genres
    path('genres/list',GenresList.as_view(), name="list_of_genres"),
    path('genres',Genres.as_view(), name="add_genres"),
    path('genres/<uuid:id_string>',GenresDetail.as_view(), name="get_genres"),

    # URLS for Movies
    path('movies/list',MoviesList.as_view(), name="list_of_movies"),
    path('movies',Movies.as_view(), name="add_movies"),
    # path('movies/<uuid:id_string>',MoviesDetail.as_view(), name="get_movies")
]
