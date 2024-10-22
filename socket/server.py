import socket
ob=socket.socket()
ob.bind(('localhost',2301))#
ob.listen(4)
clientobject,add=ob.accept()

print("server is ready to  acept connection")
print('connected with this address:',add)
clientobject,add=ob.accept()
ob.close()