from socket import *

# Asking for the input from the client i.e; a URL
url = input("Type in the URL:")
url = url[7:]
serverName = url[:url.find(":")]  # Parsing the url to get just the server name
# Parsing the url to get just the port number
serverPort = int(url[url.find(":")+1:url.find("/")])
# Retrieving the path of the file, stored in thr server, from the url
request = url[url.find("/"):]
# Creating a HTTP request line by concatinating the GET function and the HTTP version at appropriate positions
request = "GET "+request+" HTTP/1.1"
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# Sending the request from the clients socket to the servers socket
clientSocket.send(request.encode())
response = clientSocket.recv(1024)  # Receiving the response from the server
print(response.decode())
clientSocket.close()
