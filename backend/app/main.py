# https://www.pinecone.io/learn/fast-retrieval-augmented-generation/
from fastapi import FastAPI

app = FastAPI()


@app.get("/jesus")
async def jesus() -> dict[str, str]:
    return {"message": "Jesus is the way, the truth, and the life."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
