import socket
import threading

def handle_client(client_socket):
    
    try:
        
        while True:
            
            data = client_socket.recv(1024)
            if not data:
                break
            
            message = data.decode('utf-8')
            print(f"Received message from {client_socket.getpeername()}: {message}")

            # Check if the client wants to quit
            if message.lower() == 'quit':
                break

            response = input(f"Enter your response for {client_socket.getpeername()}: ")
            client_socket.sendall(response.encode('utf-8'))

    except ConnectionResetError:
        
        print(f"Connection with {client_socket.getpeername()} reset by peer.")

    finally:
        
        print(f"Connection with {client_socket.getpeername()} closed.")
        client_socket.close()

def main():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target = handle_client, args = (client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
