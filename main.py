from typing import Dict, Union

from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


BACKEND_API_URL = "https://shelfi-backend-app-dhpri.ondigitalocean.app/api/confirm/getdata/"

@app.post("/forward")
def forward_data(payload: Dict):
    try:
        response = requests.post(BACKEND_API_URL, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error forwarding data: {str(e)}")