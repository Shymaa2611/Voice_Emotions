# Voice Emotion Detection Application

## Overview

The **Voice Emotion Detection Application** is a web-based tool for analyzing and detecting emotions in audio files. Built using **FastAPI** with **Jinja2** for templating, the app provides an intuitive user interface for audio playback and emotion visualization. The application is containerized using Docker, ensuring a consistent and reproducible deployment environment.

We leverage a **fine-tuned Whisper model by OpenAI** for accurate voice-to-text transcription, which serves as the input for emotion detection.

### DEMO
[Watch ](media/project.mp4)

## Features

- **Emotion Detection**: Automated emotion detection from audio samples using a fine-tuned Whisper model.
- **Audio Playback**: Seamless audio playback with real-time emotion visualization.
- **Web Interface**: A responsive and user-friendly interface built with HTML, CSS, and JavaScript.
- **Dockerized Deployment**: Easy deployment using Docker.

## Technologies Used

- **FastAPI**: High-performance framework for building APIs and web applications.
- **Whisper by OpenAI**: Fine-tuned model for accurate transcription and emotion analysis.
- **Jinja2**: Templating engine for rendering dynamic HTML pages.
- **Docker**: Containerization for consistent deployment across environments.
- **HTML/CSS/JavaScript**: Frontend stack for creating a responsive UI.

## Project Structure
```bash
voice-emotions/
│
│── main.py           
│── Model/              
│   ├── Checkpoint      
│   ├── inference.py   
│   ├── model.py  
│── audio_files/              
│   ├── angry.wav
│   ├── disgust.wav 
│   ├── ....
│── images/              
│   ├── angry.jpg
│   ├── disgust.jpg
│   ├── ....
├── static/              
│   └── style.css         
├── templates/           
│   └── index.html       
├── requirements.txt      
├── Dockerfile           
└── README.md             
```
## Prerequisites

Before running this application, ensure that you have the following installed:

- **[Docker](https://www.docker.com/)**: To build and run the Docker container.
- **[Python 3.8+](https://www.python.org/)**: Required if running locally (without Docker).
- **[FastAPI](https://fastapi.tiangolo.com/)**: Backend framework.
- **[Jinja2](https://jinja.palletsprojects.com/)**: Templating system.
- **[Whisper](https://github.com/Shymaa2611/Voice_Emotional_Recognition.git)**: OpenAI's model for speech recognition.

## Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/Shymaa2611/Voice_Emotions.git
cd Voice-Emotions
```
### Step 2: Build the Docker Image

Build the Docker image for the application:
```bash
docker build -t emotionimage .
```
### Step 3: RUN Apllication

Once the image is built, run the Docker container:
```bash
docker run -d --name mycontainer -p 80:80 emotionimage
```
## Access the Application

- The application will run by default at http://127.0.0.1:8000.

## API Documentation

- Access the Swagger documentation for API endpoints at http://127.0.0.1:8000/docs.
