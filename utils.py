import socket

def getConnection(option):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    match option:
        case 1:
            ip, port = input('Endereço> ').split(':')
            s.connect((ip, int(port)))
            return s

        case 2:
            s.bind(('127.0.0.1', 6781))
            s.listen(1)
            conn, _ = s.accept()
            return conn