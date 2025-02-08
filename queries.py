import pandas as pd
from sqlalchemy import create_engine
#Render PostgreSQL connection string
db_url = 'postgresql://movies_pipeline_db_user:MeZmim8fN72BnQC80wLbeRVptwakjGAj@dpg-cujd66bv2p9s73fv9nr0-a.oregon-postgres.render.com/movies_pipeline_db'
engine = create_engine(db_url)

#SQL query and get the result as a DataFrame
#query = "SELECT * FROM movies LIMIT 10;"
query = "SELECT COUNT(*) FROM movies;"
result_df = pd.read_sql_query(query, engine)
print(result_df)
