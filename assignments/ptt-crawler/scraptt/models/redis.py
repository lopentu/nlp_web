import os
import redis
from pathlib import Path
from dotenv import load_dotenv

env_path = Path("__file__").resolve().parent / ".env"
load_dotenv(env_path)

is_production = os.environ.get("PYTHON_ENV") == "production"
host = "redis" if is_production else "localhost"

pool = redis.ConnectionPool(host=host, port=6379, decode_responses=True)
redis_cli = redis.Redis(connection_pool=pool)
