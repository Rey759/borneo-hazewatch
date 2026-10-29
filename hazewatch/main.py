from datetime import timedelta

from hazewatch.config import FIRMS_SOURCE
from hazewatch.fetch_hotspot import fetch_hotspot
from hazewatch.models import HotspotMetrics
from hazewatch.process import (
    compute_metrics,
    filter_hotspot_by_date,
    is_valid_comparison_metrics,
    process_hotspot,
)
from hazewatch.storage import load_metrics, save_metrics, save_report
from hazewatch.summarize import summarize_metrics


def main() -> None:
    print("1. Mengambil data hotspot dari NASA FIRMS")
    
    raw_df = fetch_hotspot()
    print(f"2. Data berhasil diambil: {len(raw_df)} hotspot")
    
    if raw_df.empty:
        raise RuntimeError(
            "NASA FIRMS tidak mengembalikan data hotspot"
        )
        
    print("\n2. Membersihkan data hotspot")
    
    df = process_hotspot(raw_df)
    print(f"Data setelah diproses: {len(df)} hotspot")
    
    if df.empty:
        raise RuntimeError(
            "Tidak ada data yang valid setelah pemrosesan"
        )
        
    if "acq_date" not in df.columns:
        raise ValueError(
            "Kolom 'acq_date' tidak ditemukan pada data hotspot"
        )
        
    available_dates = df["acq_date"].dropna()
    
    if available_dates.empty:
        raise RuntimeError(
            "Tidak ditemukan tanggal observasi yang valid"
        )
        
    # Gunakan tanggal observasi terbaru dari NASA FIRMS
    observation_date = max(available_dates)
    
    print(
        "\n3. Tanggal observasi terbaru: "
        f"{observation_date}"
    )
    
    daily_df = filter_hotspot_by_date(
        df,
        target_date=observation_date,
    )
    
    print(
        f"Hotspot pada {observation_date}: "
        f"{len(daily_df)}"
    )
    
    print("\nConfidence:")
    if "confidence" in daily_df.columns:
        print(daily_df["confidence"].value_counts())
    else:
        print("Kolom confidence tidak tersedia")
        
    # Bandingkan dengan metrik dari tanggal observasi sebelumnya
    previous_date = observation_date - timedelta(days=1)
    previous_metrics = load_metrics(previous_date)
    
    if not is_valid_comparison_metrics(
        previous_metrics,
        expected_date=previous_date,
        source=FIRMS_SOURCE,
    ):
        print(
            f"Metrik pembanding untuk {previous_date} "
            "tidak tersedia atau tidak valid"
        )
        previous_metrics = None
    
    metrics = compute_metrics(
        daily_df,
        previous_metrics,
    )
    
    # Validasi metrik inti sebelum menambahkan metadata
    validate_metrics = HotspotMetrics(**metrics)
    metrics = validate_metrics.model_dump()
    
    # Metadata untuk memvalidasi pembandi di masa yang akan datang
    metrics.update({
        "observation_date": observation_date.isoformat(),
        "period_days": 1,
        "source": FIRMS_SOURCE,
    })
    
    print("\n4. Metrik harian:")
    print(metrics)
    
    metrics_path = save_metrics(
        metrics,
        target_date=observation_date,
    )
    print(f"\nMetrik disimpan: {metrics_path}")
    
    report = summarize_metrics(
        metrics,
        report_date=observation_date,
    )
    
    print("\n" + report)
    
    report_path = save_report(
        report,
        target_date=observation_date,
    )
    print(f"Laporan disimpan: {report_path}")
    
if __name__ == "__main__":
    main()