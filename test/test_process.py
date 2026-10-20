import pandas as pd

from hazewatch.process import compute_metrics, process_hotspot


def test_compute_metrics():
    df = pd.DataFrame(
        {
            "latitude": [-2.51, -2.54, -3.10, -3.12],
            "longitude": [115.31, 115.34, 114.80, 114.82],
            "confidence": ["h", "n", "h", "l"],
            "frp": [10.0, 20.0, 30.0, 40.0],
         
        }
    )
    
    result = compute_metrics(df)

    assert result["total"] == 4

    assert result["high_confidence"] == 2

    assert result["total_frp"] == 100.0

    assert result["top_area"]["latitude"] == -2.5
    assert result["top_area"]["longitude"] == 115.3
    assert result["top_area"]["count"] == 2

    assert result["trend"] is None
    
def test_compute_metrics_with_yesterday ():
    df = pd.DataFrame(
        { 
            "latitude": [-2.51, -2.54, -3.10, -3.12],
            "longitude": [115.31, 115.34, 114.80, 114.82],
            "confidence": ["h", "n", "h", "l"],
            "frp": [10.0, 20.0, 30.0, 40.0],
            
        }
    )
    
    yesterday = {"total" : 2}
    
    result = compute_metrics(df, yesterday)
    
    assert result["total"] == 4
    assert result["trend"] == 2
    
def test_process_hotspot():
    df = pd.DataFrame(
        {
            "latitude": [-2.51, -2.54, -5.0, None],
            "longitude": [115.31, 115.34, 115.0, 115.0],
            "confidence": ["h", "n", "h", "l"],
            "frp": [10.0, 20.0, 30.0, 40.0],   
        }
    )
    
    result = process_hotspot(df)
    
    assert len(result) == 2
    assert result["latitude"].between(-3.570070, -1.964000).all()
    assert result["longitude"].between(110.732674, 115.847221).all()
    
def test_process_hotspot_invalid_coordinates():
    df = pd.DataFrame(
    
        {
            "latitude": [-2.51, "invalid", -5.0, None],
            "longitude": [115.31, 115.34, 115.0, 115.0],
            "confidence": ["h", "n", "h", "l"],
            "frp": [10.0, 20.0, 30.0, 40.0],   
        }
    )
    
    result = process_hotspot(df)
    
    assert len(result) == 1
    assert result.iloc[0]["latitude"] == -2.51
    assert result.iloc[0]['longitude'] == 115.31
    
def test_compute_metrics_negative_trend():
    df = pd.DataFrame(
        {
            "latitude": [-2.51, -2.54, -3.10, -3.12],
            "longitude": [115.31, 115.4, 114.80, 114.82],
            "confidence": ["h", "n", "h", "l"],
            "frp": [10.0, 20.0, 30.0, 40.0],
        }
    )
    
    yesterday = {"total": 10}
    
    result = compute_metrics(df, yesterday)
    
    assert result["total"] == 4
    assert result["trend"] == -6


def test_compute_metrics_yesterday_without_total():
    df = pd.DataFrame(
        {
            "latitude": [-2.51, -2.54, -3.10, -3.12],
            "longitude": [115.31, 115.4, 114.80, 114.82],
            "confidence": ["h", "n", "h", "l"],
            "frp": [10.0, 20.0, 30.0, 40.0],
        }
    )
    
    yesterday = {}
    
    result = compute_metrics(df, yesterday)
    
    assert result["total"] == 4
    assert result["trend"] == -6