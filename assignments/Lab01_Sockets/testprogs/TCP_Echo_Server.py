# TCP_Echo_Server.py
import sys, argparse
import socket 

RECV_BUFFER_SIZE = 1024
MAX_QUEUED_CONNECTIONS = 1

# Get port to listen on as command line argument
def get_args(argv):
    parser = argparse.ArgumentParser(description="TCP Echo Server")
    parser.add_argument('-p', '--port', required=False, default=12000, type=int)
    return parser.parse_args()

def main(argv):
    # Process commandline arguments
    args = get_args(argv)

    # Create a TCP socket (note use of SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Opened Server TCP socket")

    # Assign IP address and port number to socket
    server_socket.bind(('', args.port))
    print("Bound socket on port " + str(args.port))

    # Listen for incoming connections
    server_socket.listen(MAX_QUEUED_CONNECTIONS)
    print("Listening for connections...")

    while True:
        # Accept client connection and create new socket for the connection
        connection_socket, addr = server_socket.accept()

        # Receive the client message
        message = connection_socket.recv(RECV_BUFFER_SIZE)
        message = message.decode()
        print("Received msg from {}:{}\t{}".format(addr[0], addr[1], message))

        # Here we capitalize the message before returning just to show that we
        # can process / modify the message however we want
        message = message.upper()

        # Send response
        connection_socket.send(message.encode())

        # Close connection
        connection_socket.close()

if __name__ == "__main__":
    main(sys.argv[1:])
