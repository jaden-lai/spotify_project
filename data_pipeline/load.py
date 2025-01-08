import psycopg2
from sqlalchemy import create_engine, inspect
import pandas as pd

def load_data(df, db_url):
    """
    Load the transformed data into a PostgreSQL database.
    """
    try:
        engine = create_engine(db_url)
        # Use a connection object for to_sql
        with engine.connect() as connection:
            df.to_sql('recent_tracks', con=connection, if_exists='replace', index=False)
        print("Data successfully loaded into PostgreSQL.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")