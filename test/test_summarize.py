from datetime import date

from hazewatch.summarize import summarize_metrics


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

def test_summarize_metrics():
    metrics = sample_metrics()

    report = summarize_metrics(
        metrics,
        report_date=date(2026, 10, 21),
    )

    assert "21 Oktober 2026" in report
    assert "916" in report
    assert "144" in report
    assert "-3.3, 112.7" in report
    assert "Data pembanding belum tersedia" in report


def test_summarize_positive_trend():
    report = summarize_metrics(
        sample_metrics(trend=10),
        report_date=date(2026, 10, 21),
    )

    assert "meningkat sebanyak 10" in report

def test_summarize_negative_trend():
    report = summarize_metrics(
        sample_metrics(trend=-6),
        report_date=date(2026, 10, 21)
    )

    assert "menurun sebanyak 6" in report


def test_summarize_zero_trend():
    report = summarize_metrics(
        sample_metrics(trend=0),
        report_date=date(2026, 10, 21),
    )

    assert "Jumlah hotspot tidak berubah" in report


def test_summarize_without_top_area():
    metrics = sample_metrics()
    metrics["total"] = 0
    metrics["high_confidence"] = 0
    metrics["total_frp"] = 0.0
    metrics["top_area"] = None

    report = summarize_metrics(
        metrics,
        report_date=date(2026, 10, 21),
    )

    assert "Total hotspot terdeteksi: 0" in report
    assert "AREA DENGAN HOTSPOT TERBANYAK" not in report
    assert "tidak ada hotspot yang terdeteksi periode ini" in report.lower()

def test_summarize_without_top_area_still_shows_trend():
    metrics = {
        "total": 0,
        "high_confidence": 0,
        "total_frp": 0,
        "top_area": None,
        "trend": -500,
    }

    report = summarize_metrics(
        metrics,
        report_date=date(2026, 10, 27),

    )

    assert "Total hotspot terdeteksi: 0" in report
    assert "tidak ada hotspot yang terdeteksi periode ini" in report.lower()
    assert "Tren harian: " in report
    assert "500" in report
    assert "AREA DENGAN HOTSPOT TERBANYAK" not in report
