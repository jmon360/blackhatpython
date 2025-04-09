# blackhatpython
python programming for hackers and pentesters

This is repo with all the python I've followed along from the book

# 🧠 Python Networking Toolkit

A lightweight, modular toolkit for socket programming and network automation using Python.  
Created by **jmon360** (Civil Eng. Assistant • Security Student)  
Inspired by *Black Hat Python* and designed for Red/Blue Team learning.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Included Tools](#included-tools)
  - [1. NetCat Tool](#1-netcat-tool-netcat_toolpy)
  - [2. TCP Client](#2-tcp-client-tcpclientpy)
  - [3. TCP Server](#3-tcp-server-tcpserverpy)
  - [4. UDP Client](#4-udp-client-udpclientpy)
- [Educational Value](#educational-value)
- [Reference](#reference)
- [License](#license)
- [Author](#author)

---

## 📦 Overview

This suite includes four essential networking scripts, each built from scratch using Python’s standard libraries.  
Whether you're studying socket programming, building red team tools, or experimenting with automation, this toolkit offers real-world logic and clean pseudocode to help you grow.

---

## Included Tools

### 1. 🛰️ NetCat Tool (`netcat_tool.py`)
> A custom Python version of NetCat with support for reverse shells, command execution, and file uploads.

- Supports both client and server modes
- Launch a remote shell, execute commands, or upload files via TCP
- Fully class-based, with inline pseudocode and comments

### 2. 🌐 TCP Client (`tcpclient.py`)
> Demonstrates a basic TCP connection to a remote host and prints response data.

- Uses `socket.AF_INET` and `socket.SOCK_STREAM`
- Can optionally send HTTP requests
- Perfect for understanding connection-based sockets

### 3. 🧩 TCP Server (`tcpserver.py`)
> Multi-threaded TCP server that accepts incoming client connections and responds with an acknowledgment.

- Accepts multiple clients via Python's `threading.Thread`
- Logs all incoming messages to the console
- Sends back a simple "ACK" response

### 4. 📡 UDP Client (`udpclient.py`)
> Sends a single message using UDP (datagram) and waits for a stateless response.

- No formal connection or session required
- Lightweight and fast — useful for ping-style messaging
- Demonstrates the use of `SOCK_DGRAM` in contrast to TCP

---

## 🧠 Educational Value

Each script is structured with:
- Clean pseudocode above each block
- Purpose-driven comments for teaching
- Modular design, perfect for expansion

These tools can be used for:
- Penetration testing labs
- Blue team monitoring simulations
- Network protocol experiments
- Foundations for Python-based exploits

---

## 📚 Reference

This toolkit was inspired by the concepts introduced in:

**Black Hat Python: Python Programming for Hackers and Pentesters**  
Author: Justin Seitz  
Publisher: No Starch Press  
ISBN: 978-1-59327-590-7  
🔗 [Book Link](https://nostarch.com/blackhatpython)

> While the codebase takes inspiration from BHP, it has been refactored and extended to support modular learning, cleaner syntax, and new tooling logic.

---

## 📜 License

MIT License — use freely, modify respectfully, and credit the author where due.

---

## ✊ Author

**jmon360**   
📐 Civil Engineering Assistant  
💻 Red/Blue Team Security Student  
🌆 Based in NYC | Focused on Python, Networking, and Automation

---


> ⚠️ This tool is for **educational and authorized testing only.** Unauthorized use is prohibited.
