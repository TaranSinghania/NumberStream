# Import statementss
import time
import random
from socket import *


if __name__ == "__main__":
    # Setting client name/ip
    clientName = 'localhost'

    # Setting client port
    clientPort = 12000

    # Declaring the socket and setting SOCK_STREAM for TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Connecting the socket to IP and Port
    serverSocket.connect((clientName, clientPort))

    # Number of elements
    i = 100

    while(i):
        # Generate unsigned id
        num = random.randint(0, 1024*1024*1024)
        print("Generating unqiue id: ", num)

        # Converting to string and padding it with 'c' to fit the buffer
        num = str(num)
        num.ljust(256,'c')

        # Send to client
        serverSocket.send(num.encode('utf-8'))

        # Buffer period to avoid overloading of requests
        time.sleep(0.5)

        # Decrementing i for limited number of requests
        i-=1

    # Closing socket connection after sending
    serverSocket.close()