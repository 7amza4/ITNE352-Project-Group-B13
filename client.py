import socket
import json

# Global constants
HOST = '127.0.0.1'
PORT = 6533

# Connect to the server
def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_name = input("Enter your name: ")
    client_socket.send(client_name.encode())

    while True:
        print("1. Search headlines")
        print("2. List of Sources")
        print("3. Quit")
        choice = input("Select an option: ")

        if choice == '3':
            client_socket.send(json.dumps({'type': 'QUIT'}).encode())
            break
        elif choice == '1':
            handle_headlines_menu(client_socket)
        elif choice == '2':
            handle_sources_menu(client_socket)

    client_socket.close()

def handle_headlines_menu(client_socket):
    while True:
        print("1. Search for keywords")
        print("2. Search by category")
        print("3. Search by country")
        print("4. List all new headlines")
        print("5. Back to the main menu")
        choice = input("Select an option: ")

        if choice == '5':
            break
        elif choice == '1':
            keyword = input("Enter keyword to search: ")
            request = {'menu': 'headlines', 'type': 'keywords', 'value': keyword}
        elif choice == '2':
            category = input("Enter category (business, entertainment, general, health, science, sports, technology): ")
            request = {'menu': 'headlines', 'type': 'category', 'value': category}
        elif choice == '3':
            country = input("Enter country code (au, nz, ca, ae, sa, gb, us, eg, ma): ")
            request = {'menu': 'headlines', 'type': 'country', 'value': country}
        elif choice == '4':
            request = {'menu': 'headlines', 'type': 'all'}

        client_socket.send(json.dumps(request).encode())
        display_results(client_socket, 'headlines')

def handle_sources_menu(client_socket):
    while True:
        print("1. Search by category")
        print("2. Search by country")
        print("3. Search by language")
        print("4. List all")
        print("5. Back to the main menu")
        choice = input("Select an option: ")

        if choice == '5':
            break
        elif choice == '1':
            category = input("Enter category (business, entertainment, general, health, science, sports, technology): ")
            request = {'menu': 'sources', 'type': 'category', 'value': category}
        elif choice == '2':
            country = input("Enter country code (au, nz, ca, ae, sa, gb, us, eg, ma): ")
            request = {'menu': 'sources', 'type': 'country', 'value': country}
        elif choice == '3':
            language = input("Enter language (ar, en): ")
            request = {'menu': 'sources', 'type': 'language', 'value': language}
        elif choice == '4':
            request = {'menu': 'sources', 'type': 'all'}

        client_socket.send(json.dumps(request).encode())
        display_results(client_socket, 'sources')

def display_results(client_socket, menu):
    results = json.loads(client_socket.recv(4096).decode())
    if menu == 'headlines':
        for i, article in enumerate(results):
            print(f"{i + 1}. Source: {article['source']['name']} - Title: {article['title']}")
        selected_index = int(input("Select an article number for more details: ")) - 1
        selected_title = results[selected_index]['title']
    elif menu == 'sources':
        for i, source in enumerate(results):
            print(f"{i + 1}. {source['name']}")
        selected_index = int(input("Select a source number for more details: ")) - 1
        selected_id = results[selected_index]['id']

    client_socket.send(selected_title.encode() if menu == 'headlines' else selected_id.encode())
    detailed_result = json.loads(client_socket.recv(4096).decode())
    print(json.dumps(detailed_result, indent=4))

if __name__ == "__main__":
    connect_to_server()
