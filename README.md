# py-video-fetcher

This project is a simple backend API built with FastAPI and yt-dlp that allows users to send a video URL and download the best quality version of the video. It's designed as a personal project to help learn Python and backend development.

## Features

- Accepts video URLs via HTTP POST.
- Uses `yt-dlp` to download videos.
- Saves downloaded videos to a local `downloads/` folder.

## Requirements

Make sure you have Python 3.11+ installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the app

Start the FastAPI server locally:

```bash
uvicorn app.main:app --reload
```

> Note: The source code is located inside the `app/` folder.

## Folder structure

```
project-root/
├── app/
│   └── main.py
├── downloads/
├── requirements.txt
└── README.md
```

## API Endpoints

### `POST /download_video/`

Downloads a video from the URL provided.

- **Request body (JSON):**

```json
{
  "url": "https://www.youtube.com/watch?v=example"
}
```

- **Response (JSON):**

```json
{
  "status": "success",
  "message": "Download completed for https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "filename": "dQw4w9WgXcQ.mp4"
}
```

- **On error:**

```json
{
  "status": "error",
  "message": "Error details here..."
}
```

### `GET /videos/{filename}`

Returns the requested video file from the downloads/ folder.

Parameters:
**`filename`** – The name of the file to download (including extension)


Example:
To download a file saved as example-video.mp4, call:

`GET http://localhost:8000/videos/dQw4w9WgXcQ.mp4`

If the file exists, it will be served as a downloadable response. If not, it returns a 404 error.

## Future Improvements

- Add download progress tracking.
- Store metadata about each download.
- Create a frontend to interact with the backend.
- Upload results to the cloud (e.g. GCP Storage or AWS S3).

## License

MIT
