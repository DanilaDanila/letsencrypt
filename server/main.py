import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    fortune = os.popen("fortune").read().replace("\n", "<br>")

    return f"""
    <html>
    <head>
    </head>
    <body>
        <p>{fortune}</p>
    </body>
    </html>
    """
