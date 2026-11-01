
from fastapi import FastAPI

app = FastAPI(
    title="ServiceOps AI",
    description="AI-powered IT service desk automation platform",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "ServiceOps AI"
    }
