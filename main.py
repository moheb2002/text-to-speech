from fastapi import FastAPI
from pydantic import BaseModel
import azure.cognitiveservices.speech as speechsdk
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os as OS
load_dotenv()
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



SPEECH_KEY = OS.environ.get("SPEECH_KEY")
SPEECH_REGION = OS.environ.get("SPEECH_REGION")

class SpeechRequest(BaseModel):
    text: str

@app.post("/speak")
async def speak(req: SpeechRequest):

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION
    )

    audio_config = speechsdk.audio.AudioOutputConfig(
        filename="output.wav"
    )

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    result = synthesizer.speak_text_async(
        req.text
    ).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return {
            "status": "success",
            "file": "output.wav"
        }

    return {
        "status": "error"
    }