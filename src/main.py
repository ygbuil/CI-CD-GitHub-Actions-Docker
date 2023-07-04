from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_hello_world():
    return {'return': 'hello world!'}

# uvicorn src.main:app --port 8000 --reload