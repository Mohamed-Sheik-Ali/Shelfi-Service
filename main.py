from typing import Dict
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import requests
from dotenv import load_dotenv

load_dotenv()
import os

app = FastAPI()

BACKEND_API_URL = os.environ.get("BACKEND_URL")

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Shelfi</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }
            h1 {
                font-size: 3em;
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Shelfi</h1>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/forward")
def forward_data(payload: Dict):
    try:
        response = requests.post(BACKEND_API_URL, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error forwarding data: {str(e)}")