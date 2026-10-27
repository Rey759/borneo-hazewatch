
from hazewatch.fetch_hotspot import fetch_hotspot
from hazewatch.models import HotspotMetrics
from hazewatch.process import compute_metrics, process_hotspot
from hazewatch.storage import (
    get_local_date,
    load_metrics,
    load_yesterday_metrics,
    save_metrics,
    save_report,
)
from hazewatch.summarize import summarize_metrics

if __name__ == "__main__":
    report_date = get_local_date()
    
    print("1. Mengambil data hotspot dari NASA FIRMS")
    
    df = fetch_hotspot()
    print(f"2. Data berhasil diambil: {len(df)} hotspot")
    
    df = process_hotspot(df)
    print(f"3. Data setelah diproses: {len(df)} hotspot")
    
    
    print("\nConfidence: ")
    print(df["confidence"].value_counts())
    
    yesterday_metrics = load_yesterday_metrics(
        target_date=report_date,
    )
    
    metrics = compute_metrics(df, yesterday_metrics)
    
    validated_metrics = HotspotMetrics(**metrics)
    
    metrics = validated_metrics.model_dump()
    
    print("\nMetrics: ")
    print(metrics)
    
    metrics_path = save_metrics(
        metrics,
        target_date=report_date,
    )
    print(f"\nMetrics berhasil disimpan ke: {metrics_path}")
          
    report = summarize_metrics(
        metrics,
        report_date=report_date,
    )
    
    print("\n" + report)
    
    report_path = save_report(
        report,
        target_date=report_date
    )
    print(f"\nLaporan berhasil disimpan ke: {report_path}")
    
    loaded_metrics = load_metrics(report_date)
    
    print("\n Metrics yang dibaca kembali: ")
    print(loaded_metrics)