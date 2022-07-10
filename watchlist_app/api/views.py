
from watchlist_app.models import Movies
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view


@api_view()
def movie_list(request):
    movie = Movies.objects.all()
    mserializer = MovieSerializer(movie, many=True)
    return Response(mserializer.data)


@api_view()
def movie_details(request, pk):
    movie = Movies.objects.get(id=pk)
    mserializer = MovieSerializer(movie)
    return Response(mserializer.data)
