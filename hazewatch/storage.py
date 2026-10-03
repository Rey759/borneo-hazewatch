import json
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

DATA_DIR = Path("data/metrics")

def save_metrics(metrics: dict, target_date: date | None = None)-> Path:
    """ Save daily metrics to a JSON file """
    
    if target_date is None:
        target_date = datetime.now(UTC).date()
        
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    file_path = DATA_DIR / f"{target_date.isoformat()}.json"
    
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4)
        
    return file_path

def load_metrics(target_date: date)-> dict | None:
    """ Load metrics for a specific date """
    
    file_path = DATA_DIR / f"{target_date.isoformat()}.json"
    
    if not file_path.exists():
        return None
    
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)
    
def load_yesterday_metrics()-> dict | None:
    """ Load metrics from yesterday """
    
    yesterday = datetime.now(UTC).date() - timedelta(days=1)
    
    return load_metrics(yesterday)