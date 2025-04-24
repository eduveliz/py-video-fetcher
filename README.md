
# py-video-fetcher

A lightweight backend built with **Python** and **FastAPI** that receives video links and manages downloads using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Purpose

This project was created to:

- Learn Python through hands-on practice.
- Explore FastAPI for building fast, modern APIs.
- Integrate `yt-dlp` to automate video downloads from various platforms.
- Lay the groundwork for a future cloud deployment.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Python 3.10+

## Installation

```bash
# Clone the repository
git clone https://github.com/eduveliz/yt-dlp-fastapi-backend.git
cd yt-dlp-fastapi-backend

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

##️ How to Use

```bash
uvicorn main:app --reload
```

Then open your browser and visit: [http://localhost:8000/docs](http://localhost:8000/docs) to see the interactive documentation provided by FastAPI.

## Project Structure

```
yt-dlp-fastapi-backend/
├── main.py             # Core backend code
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

## Notes

- This is an educational project, but it's designed to be scalable.
- yt-dlp requires `ffmpeg` installed on your system for certain formats.

## Author

Created by [Eduardo Veliz](https://github.com/eduveliz) as a personal project to learn and share.
