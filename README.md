# Air Quality Data Analysis Dashboard

Dashboard untuk analisis kualitas udara pada berbagai stasiun, dengan berfokus pada PM2.5 dan PM10 sebagai matriks utamanya

## Prerequisites

Before running the dashboard, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

## Running the Dashboard

1. Navigate to the dashboard directory:

    ```sh
    cd dashboard
    ```

2. Run the Streamlit dashboard:

    ```sh
    streamlit run dashboard.py
    ```

3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Usage

The dashboard provides two main analyses:

1. **Polusi dan Cuaca**: Analyzes the weekly and monthly average PM2.5 levels and their correlation with weather conditions.
2. **Hubungan Zat-zat dengan PM2.5/PM10**: Analyzes the correlation between various pollutants and PM2.5/PM10 levels.

Use the sidebar to select the analysis you want to view.

## Data

The data used in this project should be placed in the [dataset](http://_vscodecontentref_/2) directory. Ensure the data files are named correctly as referenced in the code.