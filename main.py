from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware

starttime = datetime.now().microsecond
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
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Iteratum/Stage0_hng_backend_track",
    }
    endtime = datetime.now().microsecond
    print(endtime - starttime)
    return info


