from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import EmailRequest
from prompt_engine import build_prompt
from ollama_client import generate_email

app = FastAPI(title="PersonaMail AI")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "PersonaMail AI Backend Running"}


@app.post("/generate-email")
def generate_email_api(data: EmailRequest):
    try:
        prompt = build_prompt(data)

        ai_response = generate_email(prompt)

        return {
            "success": True,
            "generated_email": ai_response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))