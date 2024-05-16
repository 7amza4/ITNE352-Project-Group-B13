import socket
import json
def handle_client(client_socket, client_address):

    client_name = input(f"Accepted connection from {client_address}. Enter client name: ")

    results = [{"id": 1, "name": "Youssef"}, {"id": 2, "name": "Ahmed"},{"id": 3, "name": "Ali"}]
    client_socket.send(json.dumps(results).encode())

    selected_result_id = int(client_socket.recv(1024).decode())

    print(f"New connection from {client_name}")
    print(f"Request from {client_name}: Option {selected_result_id}")

    client_socket.close()

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(3) 

    print(f"Server listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        handle_client(client_socket, client_address)

if __name__ == "__main__":
    main()
