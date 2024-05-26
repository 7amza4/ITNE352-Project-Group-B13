import socket
import threading
import json
import requests

API_KEY = 'b8bc1265cf584b9ca9d3576dec709247'

# Function to retrieve data from the actual API
def get_api_data(endpoint, params=None):
    base_url = 'https://newsapi.org/v2/'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(f'{base_url}{endpoint}', headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code} {response.text}")
        return {}

def handle_client(client_socket, client_address):
    try:
        client_name = client_socket.recv(1024).decode('utf-8')
        print(f"Accepted new connection from {client_name} at {client_address}")

        while True:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break
            
            print(f"Request from {client_name}: {request}")
            response = ""

            if request == "Search headlines":
                params = {'country': 'us', 'category': 'general'}
                headlines = get_api_data("top-headlines", params)
                response = json.dumps(headlines)
            elif request == "List all sources":
                sources = get_api_data("sources")
                response = json.dumps(sources)
            
            client_socket.sendall(response.encode('utf-8'))
    except Exception as e:
        print(f"Error handling client {client_name}: {e}")
    finally:
        print(f"Client {client_name} disconnected")
        client_socket.close()

def start_server(host="127.0.0.1", port=6533):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
