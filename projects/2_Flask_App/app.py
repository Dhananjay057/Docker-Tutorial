from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI App running in Docker!"}

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application running inside a Docker container."}

@app.get("/contact")
def contact():
    return {"message": "Contact us at: abc"}
