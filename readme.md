
# Movie Recommender Django App

This is a project for **Machine Learning (CSE-476)**.  
The dataset used in this project consists of around 5000 movies collected from [Kaggle - TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).  
This is a **content-based Movie Recommender** system.

---

## Train Model

Initially, the model underwent preprocessing, followed by the implementation of a **Bag-of-Words** approach to extract **5000 tag words** from the dataset.  
Then, a **CountVectorizer matrix** was built using these feature words to represent all movies numerically.  
Using the resulting **cosine similarity matrix**, the algorithm calculated similarity scores between every pair of movies and identified the **top 6 most similar movies** for each entry.

### Environment Setup

Make sure Python **3.8.3** is installed.

```bash
cd train_model/
virtualenv ml_env
source ./ml_env/bin/activate
pip install -r requirements.txt
```

### Run Training Script

Open and run:

```text
movie_recommender_system_train_model.ipynb
```

After running, save the following generated files:
- `movie_list.pkl`
- `similarity.pkl`

---

## Django Recommender System

This is a Django Web App where users can select a movie from the list and receive recommendations for **Top 6 similar movies**.

### Environment Setup

Ensure Python **3.8.3** is installed.

```bash
cd movie_recommender_django_web_app/
virtualenv dj_env
source ./dj_env/bin/activate
pip install -r requirements.txt
```

### Set Up Environment Variables

Navigate to the Django app folder:

```bash
cd movie_recommender_django_web_app/
```

Create a `.env` file:

```bash
vim .env
```

Add the following configuration (adjust the path accordingly):

```env
MOVIE_LIST_PKL_LOCATION = "{Project_Root_Directory}/movie-recommender-system/train_model/movie_list.pkl"
SIMILARITY_PKL_LOCATION = "{Project_Root_Directory}/movie-recommender-system/train_model/similarity.pkl"
```

---

### Run the Django Server

Start the server:

```bash
python manage.py runserver 0.0.0.0:8000
```

Now you can access the Movie Recommender web interface in your browser at `http://localhost:8000`