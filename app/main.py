import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
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
        'outtmpl': './downloads/%(id)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_id = info.get("id")
            ext = info.get("ext")
            filename = f"{video_id}.{ext}"

        return {
            "status": "success",
            "message": f"Download completed for {video_url}",
            "filename": filename
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.get("/download/{filename}")
async def get_video(filename: str):
    file_path = f"./downloads/{filename}"

    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename, media_type="video/mp4")
    else:
        return {"status": "error", "message": "File not found"}
