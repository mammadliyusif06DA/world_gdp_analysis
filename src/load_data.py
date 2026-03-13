import pandas as pd

def load_gdp_data(file_path: str) -> pd.DataFrame:
    """Load and clean world GDP data"""
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['Country', 'Year', 'GDP'])
    df['Year'] = df['Year'].astype(int)
    df['GDP'] = df['GDP'].astype(float)
    return df
