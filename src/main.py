from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_hello_world():
    return {'return': 'hello world!!!'}

# run normally:
#   - uvicorn src.main:app --port 8000 --reload
# run with docker:
#   - docker compose -f docker-compose-prod.yaml up --build
