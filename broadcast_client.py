import socket
import threading


def receive_messages(client_socket):
    """Receive messages from the server and print them."""
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"\n{message.decode()}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


def start_client(host="127.0.0.1", port=12345):
    """Connect to the broadcast server and send messages."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    # Start a thread to handle incoming messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.daemon = True
    thread.start()

    try:
        while True:
            message = input("You: ")
            if message.lower() == "exit":
                print("Disconnecting...")
                break
            client_socket.send(message.encode())
    except KeyboardInterrupt:
        print("\nDisconnecting...")
    finally:
        client_socket.close()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "connect":
        start_client()
    else:
        print("Usage: python broadcast_client.py connect")
