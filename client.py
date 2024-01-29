import socket

def main():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))

    while True:
        
        message = input("Enter your message (type 'quit' to exit): ")
        client_socket.sendall(message.encode('utf-8'))

        if message.lower() == 'quit':
            break

        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"Server response: {response}")

    print("Connection closed.")
    client_socket.close()

if __name__ == "__main__":
    main()
