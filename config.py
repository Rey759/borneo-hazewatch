import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FIRMS_MAP_KEY = os.getenv("FIRMS_MAP_KEY")

FIRMS_SOURCE = "VIIRS_SNPP_NRT"
DAYS_RANGE = 1

KALTENG_KALSEL_BBOX = (110.732674, -3.570070, 115.847221, -1.964000)

