from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def get_info():
    info = {
        "email": "emmaogbo2002@gmail.com",
        "current_datetime": datetime.now().isoformat(),
        "github_url": "",
    }
    return info

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}