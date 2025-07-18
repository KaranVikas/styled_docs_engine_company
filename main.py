from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Fast api is working"}

@app.get("/health")
async def health_check():
    return {"status":"Ok"}