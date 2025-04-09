# ===============================================
# TCP Client - Socket Programming in Python
# ===============================================
# Author: jmon360
# Date: 2025
# Purpose: Demonstrate a basic TCP client that connects to a web server
# Platform: Cross-platform
# ===============================================

import socket

# ===============================================
# 🧠 Pseudocode Overview:
#
# 1. DEFINE the target host and port.
#    - Example: "www.google.com", 80 (HTTP)
#
# 2. CREATE a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM).
#
# 3. CONNECT to the remote server using the host and port.
#
# 4. SEND an HTTP GET request (optional — currently commented).
#
# 5. RECEIVE response data from the server (up to 4096 bytes).
#
# 6. PRINT the response as a decoded UTF-8 string.
#
# 7. CLOSE the socket to free up system resources.
# ===============================================

# Step 1: Define the remote host and port
target_host = "www.google.com"
target_port = 80

# Step 2: Create a socket object (AF_INET for IPv4, SOCK_STREAM for TCP)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 3: Connect to the remote server
client.connect((target_host, target_port))

# Step 4: (Optional) Send an HTTP GET request
# client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Step 5: Receive response from the server (max 4096 bytes)
response = client.recv(4096)

# Step 6: Print the decoded response
print(response.decode())

# Step 7: Close the socket connection
client.close()
