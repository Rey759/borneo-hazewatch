from hazewatch.fetch_hotspot import fetch_hotspot
from hazewatch.process import process_hotspot

if __name__ == "__main__":
    print("1. Mengambil data hotspot dari NASA FIRMS")
    
    df = fetch_hotspot()
    print(f"2. Data berhasil diambil: {len(df)} hotspot")
    
    df = process_hotspot(df)
    print(f"3. Data setelah diproses: {len(df)} hotspot")
    
    print("\nPreview Data: ")
    print(df.head())