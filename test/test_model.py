import pytest
from pydantic import ValidationError

from hazewatch.models import HotspotMetrics


def test_valid_hotspot_metrics():
    metrics = HotspotMetrics(
        total=100,
        high_confidence=25,
        total_frp=1250.5,
        top_area={
            "latitude": -2.5,
            "longitude": 115.3,
            "count": 10,
        },
        trend=5,
    )
    
    assert metrics.total == 100
    assert metrics.high_confidence == 25
    assert metrics.total_frp == 1250.5
    assert metrics.top_area.count == 10
    assert metrics.trend == 5
    
def test_reject_high_confidence_greater_than_total():
    with pytest.raises(ValidationError):
        HotspotMetrics(
            total=10,
            high_confidence=15,
            total_frp=100.0,
            top_area={
                "latitude": -2.5,
                "longitude": 115.3,
                "count": 5,
            },
            trend=0,
        )
        
def test_reject_negative_total():
    with pytest.raises(ValidationError):
        HotspotMetrics(
            total=-1,
            high_confidence=0,
            total_frp=100.0,
            top_area=0,
            trend=0,
        )