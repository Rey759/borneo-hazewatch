from datetime import date

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
    df = df.dropna(subset=["latitude", "longitude"])
            
    df = df [
        df["latitude"].between(-3.570070, -1.964000)
        & df["longitude"].between(110.732674, 115.847221)
    ]
    
    if "acq_date" in df.columns:
        df["acq_date"] = pd.to_datetime(
            df["acq_date"],
            errors="coerce",
        ).dt.date
    
    df = df.reset_index(drop=True)
    
    return df


def filter_hotspot_by_date(
    df: pd.DataFrame,
    target_date,
)-> pd.DataFrame:
    """ Keep only hotspots detected on the specified date"""
    if "acq_date" not in df.columns:
        raise ValueError("Kolom 'acq_date' tidak ditemukan")
    
    target_date = pd.Timestamp(target_date).date()
    
    return df.loc[
        df["acq_date"] == target_date
    ].reset_index(drop=True)

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

def is_valid_comparison_metrics(
    metrics: dict | None,
    expected_date: date,
    source: str,
) -> bool:
    """ Check whether previous metrics are suitable for daily comparison """
    if metrics is None:
        return False
    
    return (
        metrics.get("observation_date") == expected_date.isoformat()
        and metrics.get("period_days") == 1
        and metrics.get("source") == source
        and metrics.get("total") is not None
    )