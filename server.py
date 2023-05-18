from socket  import *
from constCS import * #-
import pickle

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 

while True:                # forever
  msg = conn.recv(1024)   # receive data from client
  if not msg: break       # stop if client stopped
  data = pickle.loads(msg)
  total_value = 0
  str_back = ''
  for element in data:
    if element[0] == 'laranja':
      total_value += 3*int(element[1])
    elif element[0] == 'banana':
      total_value += 4*int(element[1])
    elif element[0] == 'abacaxi':
      total_value += 5*int(element[1])
    else:
      str_back = element[0] + 'not in stock'
  str_back = '\n soma total: ' + str(total_value)
  conn.send(pickle.dumps(str_back)) # return the total value of the buy
conn.close()               # close the connection
