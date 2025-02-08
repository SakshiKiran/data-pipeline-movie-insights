import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
#Render PostgreSQL connection string
db_url = os.getenv('POSTGRES_URL')
engine = create_engine(db_url)

#SQL query and get the result as a DataFrame
#query = "SELECT * FROM movies LIMIT 10;"
query = "SELECT COUNT(*) FROM movies;"
result_df = pd.read_sql_query(query, engine)
print(result_df)
