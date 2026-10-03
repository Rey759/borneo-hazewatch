from datetime import UTC, datetime

from hazewatch.fetch_hotspot import fetch_hotspot
from hazewatch.process import compute_metrics, process_hotspot
from hazewatch.storage import load_metrics, load_yesterday_metrics, save_metrics

if __name__ == "__main__":
    print("1. Mengambil data hotspot dari NASA FIRMS")
    
    df = fetch_hotspot()
    print(f"2. Data berhasil diambil: {len(df)} hotspot")
    
    df = process_hotspot(df)
    print(f"3. Data setelah diproses: {len(df)} hotspot")
    
    
    print("\nConfidence: ")
    print(df["confidence"].value_counts())
    
    metrics = compute_metrics(df)
    
    print("\nMetrics: ")
    print(metrics)
    
    file_path = save_metrics(metrics)
    
    print(f"\nMetrics berhasil disimpan ke: {file_path}")
    
    loaded_metrics = load_metrics(datetime.now(UTC).date())
    
    print("\n Metrics yang dibaca kembali: ")
    print(loaded_metrics)
    
    yesterday_metrics = load_yesterday_metrics()
    
    print("\n Metrics kemarin: ")
    print(yesterday_metrics)