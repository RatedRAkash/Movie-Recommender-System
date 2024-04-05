
## Movie Recommender Django App

This is a project for Machine Learning (CSE-476).
The dataset used in this project is almost about 5000 movies collected from [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
This is a content-based Movie Recommender project.


### Train Model
Initially, the model underwent preprocessing, followed by the implementation of a bag-of-words approach to extract 5000 tag words from the dataset comprising various movies. Subsequently, a Count Vectorizer Matrix was constructed using these feature words, encompassing all movies in the dataset. Finally, utilizing the cosine similarity matrix, the algorithm computed the cosine distance between each pair of movies, resulting in the identification of the top 6 movies based on their similarity scores.

##### To run Train Model Code
```
//install Python Version 3.8.3 first

cd tran_model/
virtualenv ml_env
source ./ml_env/bin/activate
pip install -r requirements.txt

// then run --> movie_recommender_system_train_model.ipynb

// save location of "movie_list.pkl" & "similarity.pkl" file
```

### Django Recommender System

This is a normal Django Web Project where people can choose a movie among those 5000 movies & based on the chosen field the system will recommend him/her Top 6 movies.

```
//install Python Version 3.8.3 first

cd movie_recommender_django_web_app/
virtualenv dj_env
source ./dj_env/bin/activate
pip install -r requirements.txt

cd movie_recommender_django_web_app/

touch .env
// inside ".env" put the following variable
MOVIE_LIST_PKL_LOCATION = "{Project_Root_Directory}/movie-recommender-system/train_model/movie_list.pkl"
SIMILARITY_PKL_LOCATION = "{Project_Root_Directory}/movie-recommender-system/train_model/similarity.pkl"

// run the django server
python manage.py runserver 0.0.0.0:8000
```
##### Demo
![image](https://github.com/RatedRAkash/Movie_Recommender_System/assets/49761339/188a4b61-6768-494d-9afa-ee66879c50c4)

![image](https://github.com/RatedRAkash/Movie_Recommender_System/assets/49761339/528009d4-6542-4d4b-8b59-c2ab19c9dea6)
