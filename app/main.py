from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return{"message": "StudyVault API is running!"}
