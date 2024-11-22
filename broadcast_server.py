import socket
import threading

clients = []


def broadcast_message(message, sender_socket):
    """Broadcast a message to all connected clients except the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error broadcasting to client: {e}")
                client.close()
                clients.remove(client)


def handle_client(client_socket, client_address):
    """Handle communication with a single client."""
    print(f"Client connected: {client_address}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Message from {client_address}: {message.decode()}")
            broadcast_message(message, client_socket)
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            break

    print(f"Client disconnected: {client_address}")
    clients.remove(client_socket)
    client_socket.close()


def start_server(port=12345):
    """Start the broadcast server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"Server started on port {port}. Waiting for connections...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.start()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        for client in clients:
            client.close()
        server_socket.close()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "start":
        start_server()
    else:
        print("Usage: python broadcast_server.py start")
