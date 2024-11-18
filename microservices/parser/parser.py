# code-parsing-microservice/app.py
import socket
from fastapi import FastAPI
from code_parser import parse_code

app = FastAPI()

@app.post("/parse")
async def parse_code_endpoint(code: str):
    host = "0.0.0.0"
    port = 17000
    start_server(Host, Port)
    # Start the TCP server inside FastAPI handler
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        with conn:
            conn.sendall(code.encode('utf-8'))
            parsed_data = conn.recv(4096).decode('utf-8')
    return {"parsed_code": parsed_data}
