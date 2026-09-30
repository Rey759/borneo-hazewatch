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
        df["latitude"].between(-3.570070, -1.964000)
        & df["longitude"].between(110.732674, 115.847221)
    ]
    
    df = df.reset_index(drop=True)
    
    return df

def compute_metrics(
    df: pd.DataFrame,
    yesterday: dict | None = None,
)-> dict:
    """Calculate deterministic hotspot metrics"""
    
    total = len(df)
    
    confidence_counts = df["confidence"].value_counts()
    high_confidence = int(confidence_counts.get("h", 0))
    
    total_frp = float(df["frp"].sum())
    
    area = (
        df[["latitude","longitude"]]
        .round(1)
        .value_counts()
    )
    
    if len(area) > 0:
        top_area_coords = area.index[0]
        top_area_count = int(area.iloc[0])
        
        top_area = {
            "latitude": float(top_area_coords[0]),
            "longitude": float(top_area_coords[1]),
            "count": top_area_count,
        }
    else:
        top_area = None
        
    trend = None
    
    if yesterday is not None:
        yesterday_total = yesterday.get("total")
        
        if yesterday_total is not None:
            trend = total - yesterday_total
            
    return {
        "total": total,
        "high_confidence": high_confidence,
        "total_frp": total_frp,
        "top_area": top_area,
        "trend": trend,
    }

    