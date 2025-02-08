from sqlalchemy import create_engine

def store_data_in_postgres(df, db_url):
    """Storing it as a Pandas DataFrame in a PostgreSQL database."""
    engine = create_engine(db_url)
    
    #the DataFrame is saved to PostgreSQL
    df.to_sql('movies', engine, if_exists='replace', index=False)
    print("Data successfully stored in PostgreSQL!")
