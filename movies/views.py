__author__ = "priyanka"

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from Amazatic.common_functions import StandardResultsSetPagination, CustomAPIException
from Amazatic.messages import *
from movies.models import Movies as MoviesTbl, get_movie_by_id_string
from movies.movies_serializers import MoviesListSerializer, MoviesSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets, permissions
from .forms import MovieForm
from .models import Movies
from .movies_serializers import MoviesListSerializer

class HomePage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'movies/home.html'

    def get(self, request):
        queryset = MoviesTbl.objects.all()
        return Response({'movies': queryset}) 
    

def MoviePage(request):    
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('full_name')
            messages.success(request, f'Details for {username} Entered Successfully.')
            return redirect('demo-home')
        else:
            messages.warning(request, f'Error')
    else:
        form = MovieForm()
    return render(request,'movies/movie.html', {'form': form})

    

class MoviesDetail(APIView):

    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'movies/movie.html'

    # def get(self, request, pk):
    #     profile = get_object_or_404(Profile, pk=pk)
    #     serializer = ProfileSerializer(profile)
    #     return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        movie = get_object_or_404(MoviesTbl, pk=pk)
        serializer = MoviesSerializer(movie, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': movie})
        serializer.save()
        return redirect(' ')

class MoviesList(generics.ListAPIView):
    try:
        serializer_class = MoviesListSerializer
        pagination_class = StandardResultsSetPagination

        def get_queryset(self):
            queryset = MoviesTbl.objects.filter(is_active=True)
            if queryset:
                return queryset
            else:
                raise CustomAPIException('MOVIES_NOT_FOUND', status.HTTP_404_NOT_FOUND)
                
    except Exception as e:
    	raise e


# class Movies(GenericAPIView):

#     def post(self, request):
#         try:
#             serializer = MoviesSerializer(data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 movie_obj = serializer.create(serializer.validated_data)
#                 view_serializer = MoviesListSerializer(instance=movie_obj, context={'request': request})
#                 return Response({
#                     STATE: SUCCESS,
#                     RESULTS: view_serializer.data,
#                 }, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({
#                     STATE: ERROR,
#                     RESULTS: list(serializer.errors.values())[0][0],
#                 }, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({
#                 STATE: EXCEPTION,
#                 RESULTS: str(e),
#             }, status=401)



# class MoviesDetail(GenericAPIView):

#     def get(self, request, id_string):
#         try:
#             movie_obj = get_movie_by_id_string(id_string)
#             if movie_obj:
#                 serializer = MoviesListSerializer(instance=movie_obj, context={'request': request})
#                 return Response({
#                     STATE: SUCCESS,
#                     RESULTS: serializer.data,
#                 }, status=status.HTTP_200_OK)
#             else:
#                 return Response({
#                     STATE: ERROR,
#                 }, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({
#                 STATE: EXCEPTION,
#                 RESULTS: str(e),
#             }, status=404)


#     def put(self, request, id_string):
#         try:
#             movie_obj = get_movie_by_id_string(id_string)
#             if movie_obj:
#                 serializer = MoviesSerializer(data=request.data)
#                 if serializer.is_valid(raise_exception=False):
#                     movie_obj = serializer.update(movie_obj, serializer.validated_data)
#                     view_serializer = MoviesListSerializer(instance=movie_obj,
#                                                             context={'request': request})
#                     return Response({
#                         STATE: SUCCESS,
#                         RESULTS: view_serializer.data,
#                     }, status=status.HTTP_200_OK)
#                 else:
#                     return Response({
#                         STATE: ERROR,
#                         RESULTS: list(serializer.errors.values())[0][0],
#                     }, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response({
#                     STATE: ERROR,
#                 }, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({
#                 STATE: EXCEPTION,
#                 RESULTS: str(e),
#             }, status=404)

	    


