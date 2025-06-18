from fastapi import FastAPI, Request
app = FastAPI()

@app.get("/")
async def health_check():
    return {
        "status": "healthy"
    }

