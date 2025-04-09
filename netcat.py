# ===============================================
# NetCat Tool - Python-Based Network Shell Utility
# ===============================================
# Author: jmon360
# Date: 2025
# Project Type: Python Automation / Network Tool
# Platform: Windows, Linux, macOS (cross-platform)
# ===============================================

# 📦 Import standard libraries used for networking, threading, shell interaction, and argument parsing
import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

# ===============================================
# 🧠 Execute a shell command
# -----------------------------------------------
# 1. Receive the command as input.
# 2. Strip whitespace.
# 3. If command is not empty:
#    → Use `subprocess.check_output()` to run it.
#    → Return the decoded output string.
# ===============================================
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(
        shlex.split(cmd), stderr=subprocess.STDOUT
    )
    return output.decode()

# ===============================================
# 🧠 NetCat Class - Handles client/server logic
# -----------------------------------------------
# Constructor (__init__):
# 1. Save CLI args and buffer.
# 2. Create TCP socket (IPv4).
# 3. Set socket to reuse addresses (prevents binding issues).
# ===============================================
class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # ==========================================
    # 🧠 Main runner
    # ------------------------------------------
    # If in listen mode, start server.
    # Otherwise, connect as client and send.
    # ==========================================
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    # ==========================================
    # 🧠 Send mode (Client)
    # ------------------------------------------
    # 1. Connect to target:port
    # 2. If buffer exists, send it first
    # 3. Enter loop:
    #    a) Receive response
    #    b) Display response
    #    c) Prompt for next command
    # ==========================================
    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            while True:
                response = ''
                while True:
                    data = self.socket.recv(4096)
                    if not data:
                        break
                    response += data.decode()
                    if len(data) < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('> ') + '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('\n❌ Connection closed by user.')
            self.socket.close()
            sys.exit()

    # ==========================================
    # 🧠 Listen mode (Server)
    # ------------------------------------------
    # 1. Bind to target and port.
    # 2. Accept connections.
    # 3. Spawn a thread for each client.
    # ==========================================
    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        print(f'🟢 Listening on {self.args.target}:{self.args.port}...')
        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
            )
            client_thread.start()

    # ==========================================
    # 🧠 Handle client socket
    # ------------------------------------------
    # - Execute shell command if --execute
    # - Receive + save file if --upload
    # - Enter command shell if --command
    # ==========================================
    def handle(self, client_socket):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())

        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                file_buffer += data

            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)

            message = f'✅ File saved: {self.args.upload}'
            client_socket.send(message.encode())

        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'netcat.py > ')
                    while b'\n' not in cmd_buffer:
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'❌ Server error: {e}')
                    self.socket.close()
                    sys.exit()

# ===============================================
# 🧠 Entry Point - Argument Parsing & Launcher
# -----------------------------------------------
# 1. Define CLI arguments:
#    - --listen to act as server
#    - --execute, --upload, --command for special modes
#    - --target and --port for destination
# 2. Determine if stdin should be sent (client mode)
# 3. Launch NetCat instance with parsed config
# ===============================================
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='📡 BHP Net Tool — Custom NetCat Clone',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Examples:
  Server Mode - Shell:     netcat.py -t 192.168.1.108 -p 5555 -l -c
  Server Mode - Upload:    netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt
  Server Mode - Execute:   netcat.py -t 192.168.1.108 -p 5555 -l -e="cat /etc/passwd"
  Client Mode - Send Msg:  echo "Hello" | python netcat.py -t 192.168.1.108 -p 135
  Client Mode - Interactive: netcat.py -t 192.168.1.108 -p 5555
''')
    )

    parser.add_argument('-c', '--command', action='store_true', help='Start command shell')
    parser.add_argument('-e', '--execute', help='Execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='Listen mode (server)')
    parser.add_argument('-p', '--port', type=int, default=5555, help='Target port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='Target IP')
    parser.add_argument('-u', '--upload', help='Upload file destination')

    args = parser.parse_args()

    # If client, capture buffer from stdin
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    # Launch NetCat tool with parsed configuration
    nc = NetCat(args, buffer.encode())
    nc.run()
