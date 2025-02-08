# **Data Pipeline for Movie Insights**

## **Overview**
This project is a simple **data pipeline** designed to fetch movie data from the **TMDb API**, store it in a **PostgreSQL** database, and visualize insights such as top-rated movies and distribution of ratings. The project aims to give hands-on experience with data collection, storage, and analysis using Python and freely available tools.

## **Features**
- Fetches movie data (popular movies) from the TMDb API.
- Stores the data in a PostgreSQL database hosted on Render.
- Analyzes and visualizes the data using **Pandas**, **Matplotlib**, and **Seaborn**.
- Provides insights like:
  - Top-rated movies.
  - Distribution of movie ratings.

## **Technologies Used**
- **Python 3**
- **Pandas** – Data manipulation and analysis.
- **SQLAlchemy** – Database connection and data storage.
- **Matplotlib** & **Seaborn** – Data visualization.
- **PostgreSQL** – Database for storing movie data.
- **Render** – Hosting PostgreSQL database.

---

## **Setup Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/data-pipeline-movie-insights.git
   cd data-pipeline-movie-insights
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your PostgreSQL database**
   - I used Render for hosting PostgreSQL.
   - Add your database connection string to the scripts where necessary.

---

## **How to Run the Project**

1. **Run the Data Pipeline**  
   This will fetch movie data and store it in your PostgreSQL database.
   ```bash
   python movies_pipeline.py
   ```

2. **Analyze and Visualize the Data**  
   Use the `data_analysis.py` script to visualize the data:
   ```bash
   python data_analysis.py
   ```

---

## **Screenshots**

### **1. Top 10 Highest-Rated Movies**
![Top 10 Movies](./Screenshot%202025-02-08%20at%2012.09.09%20AM.png)

### **2. Distribution of Movie Ratings**
![Distribution of Ratings](./Screenshot%202025-02-08%20at%2012.10.33%20AM.png)

### **3. Top 5 Highest-Rated Movies**
![Top 5 Movies](./Screenshot%202025-02-08%20at%2012.11.32%20AM.png)

---

## **Future Improvements**
- Add filters for movies by genre and release year.
- Integrate **interactive visualizations** using Plotly.
- Expand the data collection to include more details like actors and directors.

---

## **License**
This project is for personal and educational purposes only.

