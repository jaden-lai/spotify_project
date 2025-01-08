from data_pipeline.extract import extract_recent_tracks
from data_pipeline.transform import transform_data
from data_pipeline.load import load_data
from auth.spotify_oath import authenticate_spotify
from data_pipeline.config import DB_URL
import warnings
warnings.filterwarnings('ignore', category=UserWarning, message=".*only supports SQLAlchemy connectable.*")


def run_pipeline():
    try:
        print("Starting Spotify Data Pipeline...")

        print("Authenticating with Spotify...")
        sp = authenticate_spotify()
        print("Spotify authentication successful!")

        print("Extracting recent tracks...")
        tracks = extract_recent_tracks(sp)
        if not tracks:
            print("No tracks retrieved. Exiting pipeline.")
            return
        print(f"Extracted {len(tracks)} tracks.")

        print("Transforming data...")
        transformed_data = transform_data(tracks)
        if transformed_data.empty:
            print("Transformed data is empty. Exiting pipeline.")
            return
        print(f"Data transformation successful. Shape: {transformed_data.shape}")

        print("Loading data into the database...")
        load_data(transformed_data, DB_URL),
        print("Data successfully loaded into the database!")

    except Exception as e:
        print(f"An error occurred during the pipeline execution: {e}")

if __name__ == "__main__":
    run_pipeline()


