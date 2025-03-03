# Simple-TCP-Servers-in-Python-and-Node.js


# Simple TCP Servers in Python and Node.js

This repository contains two implementations of a simple **TCP server**:

- **Python-based TCP server** using the `socket` library.
- **Node.js-based TCP server** using the `net` module.

Both servers:
- Listen on port `8080`.
- Send an "Open" message upon connection.
- Print received client data.
- Respond to the client with the received data (Node.js server only).

## Files
- `server.py` – Python TCP server.
- `server.js` – Node.js TCP server.

## Requirements
- **Python** (for Python server)
- **Node.js** (for Node.js server)

## Running the Servers
node tcp.py
python tcp.py

## Testing
telnet 127.0.0.1 8080