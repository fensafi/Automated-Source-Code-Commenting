# comment-insertion-microservice/app.py

import socket
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/insert_comments")
async def insert_comments(code: str):
    # Set up the host and port for communication with the comment generation service
    host = "comment-generation-microservice"  # Docker service name
    port = 17001  # Port used by comment generation service for socket communication
    
    try:
        # Create a socket connection to comment-generation-microservice
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(code.encode('utf-8'))  # Send the code to generate comments
            
            # Receive the generated comments from the comment-generation-microservice
            comments = client_socket.recv(4096).decode('utf-8')
        
        # Insert the comments into the code (basic placeholder logic)
        commented_code = f"{code}\n\n{comments}"
        
        return {"commented_code": commented_code}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with comment-generation service: {e}")
