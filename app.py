import time

import redis
import uvicorn
from fastapi import FastAPI

app = FastAPI()
cache = redis.Redis(host="redis", port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hitCount")
        except redis.exceptions.ConnectionError as e:
            if retries == 0:
                raise e
            retries -= 1
            time.sleep(0.5)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/hit_count")
async def hello():
    count = get_hit_count()
    return {"message": f"Hello Chandra! I have been seen {count} times."}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
