# blackhatpython
python programming for hackers and pentesters

This is repo with all the python I've followed along from the book

---

## 📚 Reference

This tool was initially inspired by the socket programming concepts introduced in:

**Black Hat Python: Python Programming for Hackers and Pentesters**  
by Justin Seitz  
[ISBN: 978-1-59327-590-7]  
Publisher: No Starch Press | [Link to Book](https://nostarch.com/blackhatpython)

While this implementation shares the same foundational ideas—such as using sockets for reverse shells, command execution, and file transfers—it has been extended and refactored to include:

- Full in-line pseudocode for educational use  
- Modular, object-oriented design (`NetCat` class)  
- Readable documentation and CLI usability enhancements  
- Future integration with TCP/UDP utilities for a full Python networking toolkit
- ---

## 🌐 TCP Client (`tcpclient.py`)

This script demonstrates a basic TCP client written in Python using the `socket` module. It connects to a remote server, optionally sends data (e.g., HTTP GET request), and receives the server’s response.

### 🧠 How It Works
- Uses `socket.AF_INET` and `socket.SOCK_STREAM` to establish a TCP connection
- Connects to a user-defined target host and port
- Receives and prints up to 4096 bytes of response
- Can be adapted for HTTP, raw sockets, or IoT devices

### 🔧 Sample Use (with HTTP GET)
Uncomment the `client.send()` line to test against real HTTP servers:

```python
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")


> ⚠️ This tool is for **educational and authorized testing only.** Unauthorized use is prohibited.
