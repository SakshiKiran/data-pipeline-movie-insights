import matplotlib
matplotlib.use('TkAgg')  # Switching to a reliable backend: this is optional, use if plt.show() doesn't work on default backend

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()


#Database connection and data fetching
db_url = os.getenv('POSTGRES_URL')
engine = create_engine(db_url)
df = pd.read_sql_query('SELECT * FROM movies;', engine)


#for plotting number of movies vs their rating
plt.close('all')  # Close any previous plots
plt.figure(figsize=(10, 6))
sns.histplot(df['vote_average'], bins=10, kde=True)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')


#for top 5 movies and their ratings 
top_5_movies = df.sort_values(by='vote_average', ascending=False).head(5)

plt.figure(figsize=(12, 6))
sns.barplot(x='vote_average', y='title', data=top_5_movies, palette='Blues_d')
plt.title('Top 5 Highest-Rated Movies')
plt.xlabel('Rating')
plt.ylabel('Movie Title')



# Plot Top 10 Movies with Color-Coded Bars
top_10_movies = df.sort_values(by='vote_average', ascending=False).head(10)


plt.figure(figsize=(14, 8))
colors = ['green' if rating >= 8 else 'orange' for rating in top_10_movies['vote_average']]
sns.barplot(x='vote_average', y='title', data=top_10_movies, palette=colors)
plt.title('Top 10 Highest-Rated Movies', fontsize=16)
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Movie Title', fontsize=12)

# Display the values on each bar
for index, value in enumerate(top_10_movies['vote_average']):
    plt.text(value + 0.1, index, f"{value:.1f}", va='center')

plt.show()
