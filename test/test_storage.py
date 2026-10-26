import json
from datetime import date

from hazewatch import storage


def test_save_and_load_metrics(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    
    target_date = date(2026, 10, 22)
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

def test_save_report(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "REPORT_DIR", tmp_path)
    
    target_date = date(2026, 10, 22)
    report = (
        "LAPORAN HARIAN HOTSPOT - 22 Oktober 2026\n"
        "Total hotspot terdeteksi: 100"
    )
    
    file_path = storage.save_report(report, target_date)
    
    assert file_path.exists()
    assert file_path.parent == tmp_path
    assert file_path.name == "2026-10-22.txt"
    assert file_path.read_text(encoding="utf-8") == report
    
def test_save_report_creates_directory(tmp_path, monkeypatch):
    report_dir = tmp_path / "reports"
    monkeypatch.setattr(storage, "REPORT_DIR", report_dir)
    
    target_date = date(2026, 10, 22)
    report = "Laporan pengujian hotspot"
    
    file_path = storage.save_report(report, target_date)
    
    assert report_dir.exists()
    assert file_path.exists()
    assert file_path.read_text(encoding="utf-8") == report