from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
async def healthcheck():
    """simple http server live check."""
    return { "status": "ok" }


@app.post("/ask")
async def ask_ai():
    """ask ai agent question, related to the app data."""
    return { "status": "WIP" }
