__author__ = "priyanka"

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from Amazatic.common_functions import StandardResultsSetPagination, CustomAPIException
from Amazatic.messages import *
from genres.models import Genres as GenresTbl, get_genre_by_id_string
from genres.genres_serializers import GenresListSerializer, GenresSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from movies.forms import GenreForm
from .models import Genres
from .genres_serializers import GenresListSerializer

def GenrePage(request):    
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('full_name')
            messages.success(request, f'Details for {username} Entered Successfully.')
            return redirect('home')
        else:
            messages.warning(request, f'Error')
    else:
        form = GenreForm()
    return render(request,'genres/genre.html', {'form': form})


class GenresList(generics.ListAPIView):
    try:
        serializer_class = GenresListSerializer
        pagination_class = StandardResultsSetPagination

        def get_queryset(self):
            queryset = GenresTbl.objects.filter(is_active=True)
            if queryset:
                return queryset
            else:
                raise CustomAPIException('GENRES_NOT_FOUND', status.HTTP_404_NOT_FOUND)
                
    except Exception as e:
    	raise e


class Genres(GenericAPIView):

    def post(self, request):
        try:
            serializer = GenresSerializer(data=request.data)
            if serializer.is_valid(raise_exception=False):
                genre_obj = serializer.create(serializer.validated_data)
                view_serializer = GenresListSerializer(instance=genre_obj, context={'request': request})
                return Response({
                    STATE: SUCCESS,
                    RESULTS: view_serializer.data,
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    STATE: ERROR,
                    RESULTS: list(serializer.errors.values())[0][0],
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                STATE: EXCEPTION,
                RESULTS: str(e),
            }, status=401)



class GenresDetail(GenericAPIView):

    def get(self, request, id_string):
        try:
            genre_obj = get_genre_by_id_string(id_string)
            if genre_obj:
                serializer = GenresListSerializer(instance=genre_obj, context={'request': request})
                return Response({
                    STATE: SUCCESS,
                    RESULTS: serializer.data,
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    STATE: ERROR,
                }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                STATE: EXCEPTION,
                RESULTS: str(e),
            }, status=404)


    def put(self, request, id_string):
        try:
            genre_obj = get_genre_by_id_string(id_string)
            if genre_obj:
                serializer = GenresSerializer(data=request.data)
                if serializer.is_valid(raise_exception=False):
                    genre_obj = serializer.update(genre_obj, serializer.validated_data)
                    view_serializer = GenresListSerializer(instance=genre_obj,
                                                            context={'request': request})
                    return Response({
                        STATE: SUCCESS,
                        RESULTS: view_serializer.data,
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        STATE: ERROR,
                        RESULTS: list(serializer.errors.values())[0][0],
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    STATE: ERROR,
                }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                STATE: EXCEPTION,
                RESULTS: str(e),
            }, status=404)

	    
