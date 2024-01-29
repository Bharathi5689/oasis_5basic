# Chat Application

This repository contains a simple client-server communication example using Python's socket module. The client and server scripts demonstrate basic message exchange over a TCP connection.

## Usage:
   
   1. Run the server script (server.py) on a machine:

            python server.py
    
       The server will start listening for incoming connections.

   2. Run the client script (client.py) on another machine or the same machine:

            python client.py
        
        The client will connect to the server.

Enter messages in the client console. The messages will be sent to the server, and the server will respond with a message.

To quit the communication, type 'quit' in the client console. The server will acknowledge, and the connection will be closed.