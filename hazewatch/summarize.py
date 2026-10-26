from datetime import date


def summerize_metrics(
    metrics: dict,
    report_date: date | None = None,
) -> str:
    if report_date is None:
        report_date = date.today()
        
    total = metrics["total"]
    high_confidence = metrics["high_confidence"]
    total_frp = metrics["total_frp"]
    top_area = metrics["top_area"]
    trend = metrics["trend"]
    
    bulan = [
        "Januari", "Februari", "Maret", "April",
        "Mei", "Juni", "Juli", "Agustus",
        "September", "Oktober", "November", "Desember",
    ]
    
    tanggal_laporan = (
        f"{report_date.day} "
        f"{bulan[report_date.month - 1]} "
        f"{report_date.year}"
    )
    
    report_lines = [
        f"LAPORAN HARIAN HOTSPOT - {tanggal_laporan}",
        "",
        f"Total hotspot terdeteksi: {total}",
        f"Hotspot dengan confidence tinggi: {high_confidence}",
        f"Total Fire Radiative Power (FRP): {total_frp:,.2f} MW",
    ]
    
    if top_area is not None:
        latitude = top_area["latitude"]
        longitude = top_area["longitude"]
        count = top_area["count"]
        
        report_lines.extend([
            "",
            "AREA DENGAN HOTSPOT TERBANYAK",
            f"Koordinat: {latitude}, {longitude}",
            f"Jumlah hotspot: {count}",
        ])
        
        report_lines.append("")
        
        if trend is None:
            report_lines.append(
                "Tren harian: Data pembanding belum tersedia."
            )
        elif trend > 0:
            report_lines.append(
                f"Tren harian: Hotspot meningkat sebanyak {trend}."
            )
        elif trend < 0:
            report_lines.append(
                f"Tren harian: Hotspot harian menurun sebanyak {abs(trend)}"
            )
        else:
            report_lines.append(
            "Tren harian: Jumlah hotspot tidak berubah."
        )
        
    return "\n".join(report_lines)