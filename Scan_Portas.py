import socket

host = input("IP ou Host: ")

for porta in [22, 80, 443, 3389]:
    sock = socket.socket()
    resultado = sock.connect_ex((host, porta))

    if resultado == 0:
        print(f"Porta {porta} ABERTA")
    else:
        print(f"Porta {porta} FECHADA")

    sock.close()