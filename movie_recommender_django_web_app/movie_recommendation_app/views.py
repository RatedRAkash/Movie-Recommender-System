import pickle

from django.shortcuts import render
from django.views import View
from django.conf import settings

class MovieList(View):
    view_name = 'movies_list'
    def get(self, request):
        movies_dataframe = pickle.load(open(settings.MOVIE_LIST_PKL_LOCATION, 'rb'))
        similarity = pickle.load(open(settings.SIMILARITY_PKL_LOCATION, 'rb'))

        movie_list = movies_dataframe['title']
        context = {
            'movies': movie_list
        }

        return render(request, 'index.html', context=context)


class RecommendList(View):
    view_name = 'recommended_movie_list_url'

    def get(self, request):
        movie_name = request.GET.get('search')
        movies_dataframe = pickle.load(open(settings.MOVIE_LIST_PKL_LOCATION, 'rb'))
        similarity = pickle.load(open(settings.SIMILARITY_PKL_LOCATION, 'rb'))
        try:
            index = movies_dataframe[movies_dataframe['title'] == movie_name].index[0]
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x: x[1])
            recommended_movie_names = []
            recommended_movie_posters = []
            for i in distances[1:7]:
                movie_id = movies_dataframe.iloc[i[0]].movie_id
                recommended_movie_names.append(movies_dataframe.iloc[i[0]].title)

            context = {
                'recommended_movie_names': recommended_movie_names
            }

        except Exception as ex:
            print(ex)
            context = {
                'error': 'This Movie is Not in Dataset'
            }
        return render(request, 'recommend_movie.html', context=context)
