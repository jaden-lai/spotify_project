import pandas as pd
from datetime import datetime

def transform_data(tracks):
    # Convert list of tracks to a pandas DataFrame
    df = pd.DataFrame(tracks)
    
    # Convert 'played_at' to datetime format
    df['played_at'] = pd.to_datetime(df['played_at'])
    
    # Convert 'duration_ms' to seconds
    df['duration_sec'] = df['duration_ms'] / 1000
    
    # Drop unnecessary 'duration_ms' column
    df.drop(columns=['duration_ms'], inplace=True)
    
    return df
