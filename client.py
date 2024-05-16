import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    client_name = input("Enter your username: ")
    client_socket.send(client_name.encode())

    try:
        while True:
            print("\nMain Menu:")
            print("1. Request data")
            print("2. Go back")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                client_socket.send("get_data".encode())

                results = client_socket.recv(1024).decode()
                print("Results:")
                print(results)

                selected_item = input("Select an item (enter ID): ")

                client_socket.send(selected_item.encode())

                item_details = client_socket.recv(1024).decode()
                print("Item Details:")
                print(item_details)

            elif choice == "2":
                pass

            elif choice == "3":
                print("Quitting...")
                break

            else:
                print("Invalid choice. Please select again.")

    except KeyboardInterrupt:
        print("\nUser interrupted. Quitting...")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
