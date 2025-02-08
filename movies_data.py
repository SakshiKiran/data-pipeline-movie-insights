import requests
import pandas as pd

def fetch_movie_data(api_key):
    """Fetching the popular movie data from - TMDb API and returning it as a Pandas DataFrame."""
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)
    response.raise_for_status()  #exception for bad responses
    data = response.json()
    
    #Converting the data to a Pandas DataFrame and select relevant columns
    movies = data['results']
    df = pd.DataFrame(movies)
    df = df[['id', 'title', 'release_date', 'vote_average', 'genre_ids']]
    return df
