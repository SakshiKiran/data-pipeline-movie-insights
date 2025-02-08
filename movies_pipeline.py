from movies_data import fetch_movie_data
from db_integration import store_data_in_postgres
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('MOVIE_API_KEY')
DB_URL = os.getenv('POSTGRES_URL')

def moviePipeline():
    """Main function to run the data pipeline."""
    #Fetch movie data from the TMDb API
    print("Fetching movie data...")
    df = fetch_movie_data(API_KEY)
    print(f"Fetched {len(df)} movies.")
    
    #Store data in PostgreSQL
    print("Storing data in PostgreSQL...")
    store_data_in_postgres(df, DB_URL)
    print("Pipeline execution completed!")

if __name__ == "__main__":
    moviePipeline()