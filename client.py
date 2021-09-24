# Import statements
import time
from socket import *

def setBit(bitmap, num):
	"""Function to set the appropriate bits.
	   Params:
			bitmap: Bit vector to store existence of a number.
			num: Number to be marked. """
	
	num_location = num//8 # Location of element in array
	shift = num%8 # Amount to be shift 
	bitmap[num_location] = bitmap[num_location] | (1 << shift) # Setting bit
	return	

def checkBit(bitmap):
	"""Function to check the appropriate bits.
	   Params:
			bitmap: Bit vector to store existence of a number. """
	
	print("\nBits set at: ")
	count = 0
	for i in range(len(bitmap)):
		ele = bitmap[i]
		for shift in range(0, 8):
			if(ele & (1 << shift)): # Check if bit is set
				print(8*i+shift)
				count += 1
	print("Total (to check): ", count) 



if __name__ == "__main__":

	# Setting client port
	clientPort = 12000

	# Declaring the socket and setting SOCK_STREAM for TCP
	clientSocket = socket(AF_INET, SOCK_STREAM)

	# Binding IP and port
	clientSocket.bind(('localhost', clientPort))

	# Start listening on socket
	clientSocket.listen(1)

	print("The server is ready to receive")
	
	# Declaring bitmap
	bitmap = [0]*512*1024*1024
	
	# Number of requests
	i = 100
	
	# Start accepting on socket
	connectionSocket, addr = clientSocket.accept()
	
	print("The server is receiving!")

	while(i):
		# Receive 256 bytes from server
		num = connectionSocket.recv(256)

		# Stripping the padded character and decoding it
		num = int(num.decode().strip('c'))
		
		# Store in bitmap
		setBit(bitmap, num)

		# Buffer period to avoid overloading of requests
		time.sleep(0.5)
		
		# Decrementing i for limited number of requests
		i-=1

	# Closing socket
	connectionSocket.close()

	# Checking if bit is set and printing the numbers streamed
	checkBit(bitmap)
