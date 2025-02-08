from movies_data import fetch_movie_data
from db_integration import store_data_in_postgres

API_KEY = '2d2767a844fd9246eb60f6f759903660'
DB_URL = 'postgresql://movies_pipeline_db_user:MeZmim8fN72BnQC80wLbeRVptwakjGAj@dpg-cujd66bv2p9s73fv9nr0-a.oregon-postgres.render.com/movies_pipeline_db'

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