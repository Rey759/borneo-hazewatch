import pandas as pd


def process_hotspot(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    df = df.dropna(subset=["latitude", "longitude"])
    
    numeric_columns = [
        "latitude",
        "longitude",
        "bright_ti4",
        "bright_ti5",
        "scan",
        "track",
        "frp",
    ]
    
    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )
            
    df = df [
        df["latitude"].between(110.732674, -3.570070)
        & df["longitude"].between(115.847221, -1.964000)
    ]
    
    df = df.reset_index(drop=True)
    
    return df