import psycopg2
from sqlalchemy import create_engine, inspect, MetaData
import pandas as pd

def load_data(df, db_url):
    """
    Load the transformed data into a PostgreSQL database.
    """
    try:
        engine = create_engine(db_url)
        
        # Reflect the existing database schema to get table information
        metadata = MetaData()
        metadata.reflect(bind=engine)
        table = metadata.tables['recent_tracks']  # Assuming 'recent_tracks' is the target table
        
        # Prepare the data for insertion
        with engine.connect() as connection:
            # Insert each row from DataFrame into the table
            for index, row in df.iterrows():
                # Create a dictionary with column names as keys
                data_dict = row.to_dict()
                # Insert the row into the table
                connection.execute(table.insert().values(data_dict))

        print("Data successfully loaded into PostgreSQL.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")