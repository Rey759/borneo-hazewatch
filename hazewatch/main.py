from hazewatch.fetch_hotspot import fetch_hotspot

if __name__ == "__main__":
    df = fetch_hotspot()
    print(len(df))
    print(df.head())