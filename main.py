from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Model.inference import Inference
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")
templates = Jinja2Templates(directory="templates")
AUDIO_DIR = 'audio_files'
IMAGE_DIR = 'images'

def get_emotion(audio_file:str):
     emotion=Inference(audio_file)
     return emotion

@app.get("/", response_class=FileResponse)
async def read_root(request: Request):
    audio_files = []
    for audio in os.listdir(AUDIO_DIR):
        label = os.path.splitext(audio)[0]
        #audio_file=os.path.join("audio_files",audio)
        #label=get_emotion(audio_file)
        img_path = f"/images/{label}.jpg" if os.path.exists(os.path.join(IMAGE_DIR, f"{label}.jpg")) else None
        audio_files.append({"label": label, "filename": audio, "img_path": img_path})
    
    return templates.TemplateResponse("index.html", {"request": request, "audio_files": audio_files})

@app.get("/audio/{audio_name}")
async def get_audio(audio_name: str):
    return FileResponse(os.path.join(AUDIO_DIR, audio_name))

@app.get("/VoiceEmotion/")
async def VoiceEmotionRecognition(audio_File:str):
      emotion=await Inference(audio_File)
      return {"Voice Emotion ": emotion}