import socket
from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

def start_client(host: str, port: int, message: dict) -> str:
    try:
        # Create a socket connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))

            # Send the message as a JSON-encoded string
            client_socket.sendall(json.dumps(message).encode('utf-8'))

            # Receive and decode the response
            response_data = client_socket.recv(4096).decode('utf-8')
            return response_data
    except Exception as e:
        raise Exception(f"Failed to connect to the server: {str(e)}")

@app.post("/generate_comments")
async def generate_comments(code: dict):
    code_content = code["code"]
    host = "code-parsing-microservice"  # Docker service name in Docker Compose
    port = 17000

    try:
        # Use start_client() to send the code and receive the parsed response
        response_data = start_client(host, port, {"code": code_content})
        parsed_code = json.loads(response_data)  # Assuming the response is JSON

        # Generate comments based on the parsed code
        comments = []
        lines = parsed_code.split("\n")

        for line in lines:
            if "def " in line:
                comments.append(f"# This is a function: {line.strip()}")
            elif "class " in line:
                comments.append(f"# This is a class: {line.strip()}")
            else:
                comments.append(f"# Line: {line.strip()}")

        # Combine comments with the parsed code
        commented_code = "\n".join(comments) + "\n" + parsed_code

        return {"commented_code": commented_code}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate comments: {str(e)}")
