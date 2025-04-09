# ===============================================
# TCP Server - Multithreaded Socket Server
# ===============================================
# Author: jmon360
# Date: 2025
# Purpose: Handle incoming TCP connections with threading
# Platform: Cross-platform (Windows/Linux/Mac)
# ===============================================

import socket
import threading

# Step 1: Define server's IP address and listening port
IP = '0.0.0.0'  # Listen on all interfaces
PORT = 9998     # Non-privileged port

# ===============================================
# 🧠 Pseudocode Overview:
#
# 1. CREATE a TCP socket using IPv4 and SOCK_STREAM.
# 2. BIND the socket to the defined IP and PORT.
# 3. LISTEN for incoming connections (max queue size = 5).
# 4. LOOP indefinitely to accept new connections.
#    a) ACCEPT a connection and get the client address.
#    b) SPAWN a new thread that handles the client socket.
#
# 5. DEFINE `handle_client()` to:
#    a) RECEIVE up to 1024 bytes from client.
#    b) PRINT the request in UTF-8 format.
#    c) RESPOND with a simple "ACK" message.
# ===============================================

def main():
    # Create a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to IP and port
    server.bind((IP, PORT))

    # Start listening with a queue of 5 connections
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    # Accept loop: waits for incoming client connections
    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        # Create a thread to handle this client
        client_handler = threading.Thread(
            target=handle_client,
            args=(client,)
        )
        client_handler.start()  # 🧠 FIXED: was missing () for `.start`

# ===============================================
# 🧠 Client Handler Function
# -----------------------------------------------
# 1. Use a context manager (`with`) to manage socket.
# 2. Receive 1024 bytes from client.
# 3. Decode and print received message.
# 4. Send a response back ("ACK").
# ===============================================
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

# ===============================================
# Run the server (entry point)
# ===============================================
if __name__ == '__main__':
    main()
