# Spotify Data Engineering Pipeline

This project focuses on building a data engineering pipeline for streaming user data from the Spotify API, storing the data in PostgreSQL, and processing it for analysis. The pipeline facilitates easy access to users' Spotify activity, including the most recently played tracks. The project also lays the groundwork for future automation using Apache Airflow.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributors](#contributors)

## Project Overview

The **Spotify Data Engineering Pipeline** ingests user data from the Spotify API and stores it in a PostgreSQL database for later analysis. The pipeline supports the retrieval of the **top 100 most recently played tracks** of a Spotify user. The project also involves setting up the framework for task automation using Apache Airflow, although this component is partially implemented.

The core functionality includes:

1. **Data Extraction**: Fetching the user’s Spotify activity data (recently played tracks).
2. **Data Transformation**: Storing the data into a PostgreSQL database.
3. **Data Loading**: Creating tables and inserting data into the PostgreSQL database.
4. **Scheduling**: Implementing a partial Apache Airflow framework to automate data extraction tasks.

## Technologies Used

- **Python**: Main language used for building the pipeline.
- **PostgreSQL**: Relational database to store and process the data.
- **SQLAlchemy**: Python SQL toolkit and ORM for database interactions.
- **Spotify API**: Provides access to Spotify's user data.
- **Apache Airflow (Partial)**: For orchestrating and scheduling tasks (in progress).
- **GitHub**: Version control for the project.
- **Docker** (Planned): Containerizing the pipeline for reproducibility.

## Installation

### Prerequisites

Make sure you have the following tools installed:
- Python 3.7+
- PostgreSQL and pgAdmin4
- Git

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/jaden-lai/spotify_project.git
    ```

2. Navigate into the project directory:

    ```bash
    cd spotify_project
    ```

3. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up PostgreSQL:
    - Install PostgreSQL if you haven't already.
    - Create a database for storing the Spotify data.
    - Update the connection details in `config.py`.

5. Set up your Spotify API credentials:
    - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create an app to get your API credentials (client ID and client secret).
    - Set up your credentials in the `config.py` file.

## Usage

To run the pipeline, execute the `main.py` script.

```bash
python main.py
