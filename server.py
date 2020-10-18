from socket import *

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
# Binding a fixed port number to the socket so that client alwyas knows which application in the server to contact
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # Listening for any request
print("The server is ready to receive")
i = 0  # Keep track of the total request
while True:
    connSocket, addr = serverSocket.accept()
    connSocket.settimeout(1)
    request = connSocket.recv(1024).decode()
    # Parse the request such that just the file path is extracted
    request_file = request[5:(request.find("HTTP/1.1")-1)]
    i += 1
    try:
        f = open(request_file)  # Open the file
    except IOError:  # If file not found or some error in the filename then send a File Not Found Status to the client
        status_line = "HTTP/1.1 404 Not Found\r\n"
        response = status_line
        connSocket.send(response.encode())
        connSocket.close()
        # Just for debugging purposes
        print("Request #", i, ": Incorrect Request!")
        continue
    # If the file was found then include a status line for that
    status_line = "HTTP/1.1 200 OK\r\n\n"
    data = f.read()  # Putting the content of the file in a buffer, data
    # Concatinating the status line and the data and then send
    response = status_line + data
    connSocket.send(response.encode())
    connSocket.close()
    print("Request #", i, ": Data Sent!")  # For debugging purposes.
