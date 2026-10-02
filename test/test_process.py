import pandas as pd

from hazewatch.process import compute_metrics


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