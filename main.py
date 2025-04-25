from fastapi import FastAPI
from pydantic import BaseModel
import yt_dlp

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

@app.post("/download_video/")
async def download_video(video_request: VideoRequest):
    video_url = video_request.url

    ydl_opts = {
        'format': 'best',
        'outtmpl': './downloads/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return {"status": "success", "message": f"Download started for {video_url}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
