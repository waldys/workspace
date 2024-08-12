from fastapi import FastAPI
from redis import Redis
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

#redis_client = Redis(host='reedis', port=6379, db=0)

redis_client = Redis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    db=0
)

class Item(BaseModel):
    key: str
    value: str

@app.post("/store/")
def store_item(item: Item):
    redis_client.set(item.key, item.value)
    return {"message": "Item stored successfully!"}