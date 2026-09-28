from io import StringIO

import pandas as pd
import requests
from config import FIRMS_MAP_KEY, KALTENG_KALSEL_BBOX

FIRMS_SOURCE = "VIIRS_SNPP_NRT"
DAYS_RANGE = 1

def fetch_hotspot() -> pd.DataFrame:
    area = ",".join(map(str, KALTENG_KALSEL_BBOX))
    url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{FIRMS_MAP_KEY}/{FIRMS_SOURCE}/{area}/{DAYS_RANGE}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return pd.read_csv(StringIO(response.text))

if __name__ == "__main__":
    df = fetch_hotspot()
    print(len(df))
    print(df.head())
    
