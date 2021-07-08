__author__ = "priyanka"

from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError
from genres.models import get_genre_by_id_string
from artists.models import get_artist_by_id_string

# used to return total count, next and previous records link
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CustomAPIException(ValidationError):
    """
    raises API exceptions with custom messages and custom status codes
    """
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code



def get_validate_data(validated_data):
    if 'genre_id' in validated_data:
        genre = get_genre_by_id_string(validated_data["genre_id"])
        if genre:
            validated_data["genre_id"] = genre.id
        else:
            raise CustomAPIException("Genre not found.", status_code=status.HTTP_404_NOT_FOUND)

    if 'artist_id' in validated_data:
        artist = get_artist_by_id_string(validated_data["artist_id"])
        if artist:
            validated_data["artist_id"] = artist.id
        else:
            raise CustomAPIException("Artist not found.", status_code=status.HTTP_404_NOT_FOUND)

    return validated_data
