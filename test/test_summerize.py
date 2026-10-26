from datetime import date

from hazewatch.summarize import summerize_metrics


def sample_metrics(trend=None):
    return {
        "total": 916,
        "high_confidence": 144,
        "total_frp": 9583.75,
        "top_area": {
            "latitude": -3.3,
            "longitude": 112.7,
            "count": 41,    
        },
        "trend": trend,
    }
    
def test_summerize_metrics():
    metrics = sample_metrics()
    
    report = summerize_metrics(
        metrics,
        report_date=date(2026, 10, 21),
    )
    
    assert "21 Oktober 2026" in report
    assert "916" in report
    assert "144" in report
    assert "-3.3, 112.7" in report
    assert "Data pembanding belum tersedia" in report
    
    
def test_summerize_positive_trend():
    report = summerize_metrics(
        sample_metrics(trend=10),
        report_date=date(2026, 10, 21),
    )
    
    assert "meningkat sebanyak 10" in report
    
def test_summerize_negative_trend():
    report = summerize_metrics(
        sample_metrics(trend=-6),
        report_date=date(2026, 10, 21)
    )
    
    assert "menurun sebanyak 6" in report
    
    
def test_summerize_zero_trend():
    report = summerize_metrics(
        sample_metrics(trend=0),
        report_date=date(2026, 10, 21), 
    )
    
    assert "Jumlah hotspot tidak berubah" in report
    

def test_summerize_without_top_area():
    metrics = sample_metrics()
    metrics["total"] = 0
    metrics["high_confidence"] = 0
    metrics["total_frp"] = 0.0
    metrics["top_area"] = None
    
    report = summerize_metrics(
        metrics,
        report_date=date(2026, 10, 21),
    )
    
    assert "Total hotspot terdeteksi: 0" in report 
    assert "AREA DENGAN HOTSPOT TERBANYAK" not in report 