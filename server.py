import sys
import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    server_socket.settimeout(1) # timeout for accept function

    conn = None
    
    try:
        while True:
            try:
                conn, address = server_socket.accept()  # accept new connection
                print("Connection from: " + str(address))
                with open("log.txt", "a") as fi:  # create/open and append to log.txt
                    fi.write("\nConnection from: " + str(address) + "\n")
                while True:
                    # receive data stream. it won't accept data packet greater than 1024 bytes
                    try:
                        data = conn.recv(1024).decode()
                        if not data:
                            # if data is not received break
                            break
                        with open("log.txt", "a") as fi:  # use the with statement
                            fi.write(str(data)) # write to file data receieved
                    except ConnectionResetError:
                        print("Client disconnected abruptly")
                        break
                conn.close()  # close the connection
            except socket.timeout:  # catch the timeout exception
                pass
            except KeyboardInterrupt: # catch the interupt to properly close server
                print("\nServer is shutting down")
                server_socket.close()  # close the server socket
                sys.exit(0)
    except KeyboardInterrupt: # catch the interupt to properly close server
        print("\nServer is shutting down")
        server_socket.close()  # close the server socket
        sys.exit(0)


if __name__ == '__main__':
    server_program()
