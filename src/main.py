from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_hello_world():
    return {'return': 'hello world!'}

# to run normally: 
#   - uvicorn src.main:app --port 8000 --reload
# to run using docker (first time): 
#   - docker compose up --build
# to run using docker once it is created: 
#   - docker compose up