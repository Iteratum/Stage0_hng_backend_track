from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def get_info():
    info = {
        "email": "emmaogbo2002@gmail.com",
        "current_datetime": datetime.now().isoformat(),
        "github_url": "https://github.com/Iteratum/Stage0_hng_backend_track",
    }
    return info

