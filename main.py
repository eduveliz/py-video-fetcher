from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

@app.post("/download")
async def download_video(req: VideoRequest):
    return {"message": f"Received link: {req.url}"}
