import socket
ob=socket.socket()
ob.connect(('localhost',2301))
msg='helo this is me '
ob.close()