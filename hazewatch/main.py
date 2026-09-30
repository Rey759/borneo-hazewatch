from hazewatch.fetch_hotspot import fetch_hotspot
from hazewatch.process import compute_metrics, process_hotspot

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