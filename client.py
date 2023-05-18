from socket  import *
from constCS import * #-
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
s.send(pickle.dumps([['banana', 3], ['abacaxi', 4]]))  # send some data
data = s.recv(1024)     # receive the response
print (pickle.loads(data))            # print the result
s.close()               # close the connection
