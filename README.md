🎙 Azure AI Speech Assistant

A lightweight Text-to-Speech (TTS) web application built with FastAPI, Azure AI Speech Services, and a modern HTML/CSS frontend. This project enables users to convert text into natural-sounding speech using Microsoft Azure Cognitive Services and play the generated audio directly from the browser.

🚀 Features
Convert text to speech using Azure AI Speech Service
FastAPI-based REST API
Simple and responsive web interface
Audio output generation in .wav format
Environment variable support with .env
CORS enabled for frontend-backend communication
Clean Microsoft-inspired UI
🏗️ Architecture
┌─────────────────┐
│   Frontend UI   │
│  HTML/CSS/JS    │
└────────┬────────┘
         │ HTTP POST
         ▼
┌─────────────────┐
│    FastAPI      │
│   /speak API    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Azure AI Speech │
│ Text-to-Speech  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  output.wav     │
│ Generated Audio │
└─────────────────┘

📂 Project Structure
azure-ai-speech-assistant/
│
├── app.py                # FastAPI backend
├── index.html            # Frontend UI
├── output.wav            # Generated audio file
├── .env                  # Azure credentials
├── requirements.txt
└── README.md

⚙️ Prerequisites

Before running the project, ensure you have:

Python 3.9+
Azure Subscription
Azure AI Speech Service Resource
Speech Key
Speech Region
🔑 Environment Variables

Create a .env file in the project root:

SPEECH_KEY=your_azure_speech_key
SPEECH_REGION=your_azure_region


Example:

SPEECH_KEY=123456789abcdef
SPEECH_REGION=eastus

📦 Installation
1. Clone the Repository
git clone https://github.com/yourusername/azure-ai-speech-assistant.git

cd azure-ai-speech-assistant

2. Create Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux/Mac

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

📋 Required Packages
fastapi
uvicorn
python-dotenv
pydantic
azure-cognitiveservices-speech


Install manually:

pip install fastapi uvicorn python-dotenv pydantic azure-cognitiveservices-speech

▶️ Running the Application

Start the FastAPI server:

uvicorn app:app --reload


Backend will be available at:

http://localhost:8000


API Documentation:

http://localhost:8000/docs

🔌 API Endpoints
Generate Speech

POST /speak

Request
{
    "text": "Hello from Azure AI Speech Services"
}

Response
{
    "status": "success",
    "file": "output.wav"
}

Error Response
{
    "status": "error"
}

💻 Frontend Usage
Open index.html.
Enter text in the text area.
Click Generate Speech.
The frontend sends a request to the FastAPI backend.
Azure AI Speech synthesizes the text.
Audio is saved as output.wav.
The generated audio is played in the browser.
🔄 Workflow
User Input
    │
    ▼
Frontend (HTML/JS)
    │
POST /speak
    ▼
FastAPI Backend
    │
Azure Speech SDK
    ▼
Speech Synthesis
    │
output.wav
    ▼
Audio Playback

🔒 Security Considerations
Never expose your Azure Speech Key in frontend code.
Store secrets securely in environment variables.
Restrict CORS origins in production environments.
Consider generating unique filenames per request to avoid overwriting audio files.

Example:

allow_origins=[
    "https://yourdomain.com"
]

🚀 Future Enhancements
Multiple Azure neural voices
Voice selection dropdown
SSML support
MP3 audio output
Download generated audio
Azure OpenAI integration
Avatar-based speech generation
User authentication
Cloud storage for generated audio
🛠 Technologies Used
Technology	PurposeFastAPI	Backend REST API
Azure AI Speech	Text-to-Speech Engine
Azure Speech SDK	Azure Service Integration
HTML/CSS/JavaScript	Frontend Interface
Pydantic	Request Validation
Python Dotenv	Environment Management
📖 Microsoft Azure AI Services

Azure AI Speech enables developers to build natural, human-like voice experiences using neural text-to-speech technology. This project demonstrates a simple integration of Azure Speech Services with a Python FastAPI backend and a browser-based frontend.

Learn more:

Azure AI Speech Services
FastAPI Documentation
Azure Cognitive Services SDK
👨‍💻 Author

Moheb Adel
 Business Program Manager Intern | Emerging AI Consultant
 Azure AI • Generative AI • Agentic AI • Microsoft Copilot
This project is licensed under the MIT License. Feel free to use, modify, and distribute it for learning and development purposes.

⭐ If you found this project useful, consider giving it a star and sharing it with others interested in Azure AI and FastAPI development.
