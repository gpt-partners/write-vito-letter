# https://www.pinecone.io/learn/fast-retrieval-augmented-generation/
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class VitoResponse(BaseModel):
    message: str


class VitoRequest(BaseModel):
    companyUrl: str
    linkedinUrl: str


@app.post("/vito-message")
async def vito_message(vitoRequest: VitoRequest) -> VitoResponse:
    return {"message": "Jesus is the way, the truth, and the life."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
