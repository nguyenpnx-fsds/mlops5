from fastapi import APIRouter
from src.services.rag import Rag
from fastapi.responses import HTMLResponse
from fastapi import WebSocket

router = APIRouter()


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Retrieval</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/v1/ws-retrieve/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

rag_service = Rag()


@router.get("/")
async def get():
    return HTMLResponse(html)


@router.websocket("/ws")
async def retrieve_restaurants(
    websocket: WebSocket,
) -> str:
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        response = await rag_service.get_rest_response(
            question=data,
        )
        await websocket.send_text(f"Answer: {response}")
