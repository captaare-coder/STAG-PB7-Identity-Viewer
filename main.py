from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="STAG PB7 Identity Viewer",
    version="1.1"
)


@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <!DOCTYPE html>
    <html>

    <head>
        <title>STAG PB7 Identity Viewer</title>

        <style>

            body {
                background: #111;
                color: white;
                font-family: Arial, sans-serif;
                padding: 40px;
            }

            h1 {
                color: #00ff88;
            }

            .card {
                background: #222;
                padding: 20px;
                margin: 15px 0;
                border-radius: 12px;
            }

            .online {
                color: #00ff88;
                font-weight: bold;
            }

        </style>

    </head>


    <body>

        <h1>🦌 STAG PB7 Ecosystem</h1>

        <div class="card">

            <h2>System Status</h2>

            <p class="online">
            🟢 ONLINE
            </p>

        </div>


        <div class="card">

            <h2>Components</h2>

            <p>
            🧠 PB7 Intelligence Studio
            <br>
            Version: v2.4
            <br>
            Status: Connected
            </p>


            <p>
            📚 PB7 Knowledge Server
            <br>
            Version: v0.2
            <br>
            Status: Connected
            </p>


            <p>
            🦌 STAG Identity
            <br>
            Version: v1.0
            <br>
            Status: Active
            </p>

        </div>


        <div class="card">

            <h2>Architecture</h2>

            <pre>

        STAG PB7
            |
     ----------------
     |              |
 Intelligence   Knowledge
   Studio        Server

            </pre>

        </div>


    </body>

    </html>
    """