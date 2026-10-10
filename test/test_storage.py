import json
from datetime import date

from hazewatch import storage


def test_save_and_load_metrics(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    
    target_date = date(2026, 10, 9)
    metrics = {
        "total": 100,
        "high_confidence": 25,
        "total_frp": 1250.5,
        "top_area": {
            "latitude": -2.5,
            "longitude": 115.3,
            "count": 10,
        },
        "trend": 5,
    }
    
    file_path = storage.save_metrics(metrics, target_date)
    assert file_path.exists()
    
    with file_path.open("r", encoding="utf-8") as file:
        saved_data = json.load(file)
        
    assert saved_data == metrics
    assert storage.load_metrics(target_date) == metrics
    
def test_load_metrics_missing_date(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    
    result = storage.load_metrics(date(2026, 1, 1))
    
    assert result is None
