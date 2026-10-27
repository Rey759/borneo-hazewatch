import json
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

LOCAL_TIMEZONE = ZoneInfo("Asia/Makassar")

DATA_DIR = Path("data/metrics")
REPORT_DIR = Path("data/reports")


def get_local_date() -> date:
    """ Return the current date in Central Indonesia Time (WITA)"""
    return datetime.now(LOCAL_TIMEZONE).date()


def save_metrics(
    metrics: dict,
    target_date: date | None = None,
    )-> Path:
    """ Save daily metrics to a JSON file """

    if target_date is None:
        target_date = get_local_date()

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_path = DATA_DIR / f"{target_date.isoformat()}.json"

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4, ensure_ascii=False)

    return file_path


def load_metrics(target_date: date | None = None)-> dict | None:
    """ Load metrics for a specific date """
    if target_date is None:
        target_date = get_local_date()

    file_path = DATA_DIR / f"{target_date.isoformat()}.json"

    if not file_path.exists():
        return None

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)
    

def load_yesterday_metrics(
    target_date: date | None = None,
)-> dict | None:
    """ Load metrics from the day before the specified date """
    if target_date is None:
        target_date = get_local_date()

    yesterday = target_date - timedelta(days=1)
    return load_metrics(yesterday)


def save_report(
    report: str,
    target_date: date | None = None,
)-> Path:
    """Save daily hotspot report to a JSON file """

    if target_date is None:
        target_date = get_local_date()

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    file_path = REPORT_DIR / f"{target_date.isoformat()}.txt"

    with file_path.open("w", encoding="utf-8") as file:
        file.write(report)

    return file_path