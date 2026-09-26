import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FIRMS_MAP_KEY = os.getenv("FIRMS_MAP_KEY")

KALTENG_KALSEL_BBOX = [110.732674, -3.570070, 115.847221, -1.964000]

print("API key detected:", os.getenv("OPENAI_API_KEY") is not None)