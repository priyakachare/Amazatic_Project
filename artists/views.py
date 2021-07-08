__author__ = "priyanka"

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from Amazatic.common_functions import StandardResultsSetPagination, CustomAPIException
from Amazatic.messages import *
from artists.models import Artists as ArtistsTbl, get_artist_by_id_string
from artists.artists_serializers import ArtistsListSerializer, ArtistsSerializer


class ArtistsList(generics.ListAPIView):
    try:
        serializer_class = ArtistsListSerializer
        pagination_class = StandardResultsSetPagination

        def get_queryset(self):
            queryset = ArtistsTbl.objects.filter(is_active=True)
            if queryset:
                return queryset
            else:
                raise CustomAPIException('ARTISTS_NOT_FOUND', status.HTTP_404_NOT_FOUND)
                
    except Exception as e:
    	raise e


class Artists(GenericAPIView):

    def post(self, request):
        try:
            serializer = ArtistsSerializer(data=request.data)
            if serializer.is_valid(raise_exception=False):
                artist_obj = serializer.create(serializer.validated_data)
                view_serializer = ArtistsListSerializer(instance=artist_obj, context={'request': request})
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



class ArtistDetail(GenericAPIView):

    def get(self, request, id_string):
        try:
            artist_obj = get_artist_by_id_string(id_string)
            if artist_obj:
                serializer = ArtistsListSerializer(instance=artist_obj, context={'request': request})
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
            artist_obj = get_artist_by_id_string(id_string)
            if artist_obj:
                serializer = ArtistsSerializer(data=request.data)
                if serializer.is_valid(raise_exception=False):
                    artist_obj = serializer.update(artist_obj, serializer.validated_data)
                    view_serializer = ArtistsListSerializer(instance=artist_obj,
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

	    
