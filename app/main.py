from fastapi import FastAPI


app = FastAPI(title="Pigia Shuru")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
