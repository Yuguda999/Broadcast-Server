
# **Broadcast Server and Client**

A simple CLI-based broadcast server and client application built in Python. The server accepts connections from multiple clients, allowing clients to send messages that are broadcast to all connected clients in real-time. `https://roadmap.sh/projects/broadcast-server`

---

## **Features**
- Server listens for incoming client connections on a specified port.
- Clients can connect to the server and send messages.
- Messages from any client are broadcast to all other connected clients.
- Supports multiple simultaneous clients.
- Handles client disconnections gracefully.
- Simple command-line interface to start the server or connect as a client.

---

## **Getting Started**

### **Prerequisites**
- Python 3.7 or higher installed on your machine.
- Basic knowledge of Python and sockets.

---

### **Installation**

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd broadcast-server
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
   *(No dependencies are required for this project.)*

---

## **Usage**

### **Starting the Server**
To start the server, run:
```bash
python broadcast_server.py start
```

- The server will listen on port `12345` by default.
- You can change the port in the `start_server` function of `broadcast_server.py`.

---

### **Connecting as a Client**
To connect as a client, run:
```bash
python broadcast_client.py connect
```

- The client connects to the server at `127.0.0.1` and port `12345` by default.
- You can modify the `host` and `port` in `broadcast_client.py` as needed.

---

### **Sending and Receiving Messages**
1. After connecting, type your message and press Enter to send it.
2. All connected clients (including yourself) will see the broadcasted message.
3. To disconnect, type `exit` or press `Ctrl+C`.

---

## **Project Structure**
```
broadcast-server/
├── broadcast_server.py   # Contains the server code
├── broadcast_client.py   # Contains the client code
├── README.md             # Project documentation
```

---

## **How It Works**

### **Server**
1. The server listens for incoming client connections on a specified port.
2. When a client connects, a new thread is spawned to handle communication with that client.
3. Received messages are broadcast to all connected clients except the sender.
4. If a client disconnects or encounters an error, the server removes the client from the list of active connections.

### **Client**
1. The client connects to the server using a socket.
2. A separate thread listens for incoming messages from the server while the user can send new messages.
3. The client disconnects gracefully when `exit` is typed or when interrupted.

---
