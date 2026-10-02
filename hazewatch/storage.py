import json
from datetime import date
from pathlib import Path

DATA_DIR = Path("data/metrics")

def save_metrics(metrics: dict, target_date: date | None = None)-> Path:
    """ Save daily metrics to a JSON file """
    
    if target_date is None:
        target_date = date.today()
        
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    file_path = DATA_DIR / f"{target_date.isoformat().json}"
    
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4)
        
    return file_path