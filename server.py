import socket
import threading
import json
import requests

API_KEY = 'b8bc1265cf584b9ca9d3576dec709247'
GROUP_ID = 'my_group'  # Replace with your actual group ID

def get_api_data(endpoint, params=None):
    base_url = 'https://newsapi.org/v2/'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(f'{base_url}{endpoint}', headers=headers, params=params)
    print(f"Request URL: {response.url}")
    if response.status_code == 200:
        print(f"Response JSON: {response.json()}")
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code} {response.text}")
        return {}

def save_to_file(group_id, client_name, option, data):
    filename = f"{group_id}_{client_name}_{option}.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def handle_client(client_socket, client_address):
    try:
        client_name = client_socket.recv(1024).decode('utf-8')
        if not client_name:
            return

        print(f"Accepted new connection from {client_name} at {client_address}")

        while True:
            request_data = client_socket.recv(1024).decode('utf-8')
            if not request_data:
                break
            
            request = json.loads(request_data)
            print(f"Request from {client_name}: {request}")
            response = ""
            headlines = {}
            sources = {}

            if request['menu'] == 'headlines':
                option = request['type']
                if request['type'] == 'keywords':
                    params = {'q': request['value']}
                    headlines = get_api_data("everything", params)
                elif request['type'] == 'category':
                    params = {'category': request['value'], 'country': 'us'}
                    headlines = get_api_data("top-headlines", params)
                elif request['type'] == 'country':
                    params = {'country': request['value']}
                    headlines = get_api_data("top-headlines", params)
                elif request['type'] == 'all':
                    params = {'country': 'us'}
                    headlines = get_api_data("top-headlines", params)
                save_to_file(GROUP_ID, client_name, option, headlines)
                response = json.dumps(headlines.get('articles', [])[:15])

            elif request['menu'] == 'sources':
                option = request['type']
                if request['type'] == 'category':
                    params = {'category': request['value']}
                    sources = get_api_data("sources", params)
                elif request['type'] == 'country':
                    params = {'country': request['value']}
                    sources = get_api_data("sources", params)
                elif request['type'] == 'language':
                    params = {'language': request['value']}
                    sources = get_api_data("sources", params)
                elif request['type'] == 'all':
                    sources = get_api_data("sources")
                save_to_file(GROUP_ID, client_name, option, sources)
                response = json.dumps(sources.get('sources', [])[:15])

            client_socket.sendall(response.encode('utf-8'))

            detail_request = client_socket.recv(1024).decode('utf-8')
            if not detail_request:
                break

            if request['menu'] == 'headlines':
                detailed_info = next((item for item in headlines.get('articles', []) if item['title'] == detail_request), None)
            elif request['menu'] == 'sources':
                detailed_info = next((item for item in sources.get('sources', []) if item['id'] == detail_request), None)

            client_socket.sendall(json.dumps(detailed_info).encode('utf-8'))
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
