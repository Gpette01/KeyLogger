# KeyLogger.py

This Python script is a simple keylogger that captures and sends keystrokes to a server. It uses the `pynput` library to listen for keyboard events and the `socket` library to send the captured keystrokes to a server.

## How it works

The script first establishes a connection to a server specified by the `host` and `port` variables. The `host` is obtained using `socket.gethostname()`, which returns the host name of the current system. The `port` is set to `5000`.

The `keyPressed` function is the main function that is called whenever a key is pressed. It captures the key and sends it to the server. Special keys like Space, Enter, and Backspace are handled separately.

The script uses a `keyboard.Listener` to start listening for key press events. The listener is started in the main section of the script, and it keeps running, waiting for user input.

## Usage

To use this script, you need to have the server.py running that can accept the incoming keystrokes. The server should be running on the same host and listening on the specified port.

# server.py

This Python script is a simple server that accepts connections from clients and logs the received data. It uses the `socket` library to create a server and handle client connections.

## How it works

The script first creates a server socket and binds it to the host name of the current system and a specified port (`5000`). It then starts listening for incoming connections, with a maximum of 2 simultaneous connections.

When a new connection is accepted, the script logs the client's address to a file named `log.txt`. It then enters a loop where it receives data from the client. The data is received in chunks of `1024 bytes` and is decoded before being written to the log file.

If the client disconnects abruptly, a `ConnectionResetError` is caught and the server logs a message indicating that the client disconnected. The connection is then closed and the server goes back to listening for new connections.

The server runs indefinitely until it is manually stopped. If a keyboard interrupt is detected (`Ctrl+C`), the server logs a shutdown message, closes the server socket, and exits.

# IMPORTANT
Please note that this script is for educational purposes only. Misuse of this script may infringe on others' privacy and may be against the law.

## Dependencies

This scripts requires the following Python libraries:
- `pynput`
- `socket`

You can install these dependencies using pip:

```bash
pip install pynput socket
