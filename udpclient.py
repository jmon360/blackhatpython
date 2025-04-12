# ===============================================
# UDP Client - Stateless Datagram Communication
# ===============================================
# Author: jmon360
# Date: 2025
# Tool Type: Lightweight Networking Script
# Platform: Cross-platform (Windows, Linux, macOS)
# ===============================================

"""
📘 Description:
This script demonstrates the use of Python's socket library to send and receive data over UDP (User Datagram Protocol). 
Unlike TCP, UDP does not require a persistent connection, making it ideal for simple, fast, and lightweight communications.

It is part of the larger Python Networking Toolkit, which includes NetCat, TCP clients/servers, and future expansions.

---

🧠 Pseudocode Overview:

1. DEFINE target host and target port
   - Example: localhost ("127.0.0.1") on port 9997
   - These represent the server IP and port that will receive the message.

2. CREATE a UDP socket
   - Use `socket.AF_INET` to specify IPv4 addressing
   - Use `socket.SOCK_DGRAM` to specify datagram-based (UDP) communication

3. SEND a raw byte message to the target server using `sendto()`
   - Format: `client.sendto(<message>, (<host>, <port>))`

4. WAIT for a response using `recvfrom()`
   - This function listens for incoming datagrams and returns:
     a) The message data
     b) The address it came from

5. DECODE the received message from bytes to UTF-8 and PRINT it

6. CLOSE the socket to release system resources
"""

# ===============================================
# 🔧 Implementation (Actual Code Below)
# ===============================================

import socket

# Step 1: Define the remote host and port
target_host = "127.0.0.1"
target_port = 9997

# Step 2: Create the UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Step 3: Send a datagram to the target address
client.sendto(b"AAABBBCCC", (target_host, target_port))

# Step 4: Receive a response from the server
data, addr = client.recvfrom(4096)

# Step 5: Decode and display the server response
print(data.decode())

# Step 6: Close the UDP socket
client.close()

