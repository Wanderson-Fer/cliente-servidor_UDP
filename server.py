import socket

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 8082

# Cria um socket UDP
server_socket = socket.socket(
    socket.AF_INET,  # IPv4
    socket.SOCK_DGRAM  # UDP | Socket tipo DATAGRAM
)

# Liga o socket ao endereço e porta especificados
server_socket.bind((HOST, PORT))

print(f"Servidor UDP esperando por mensagens em {HOST}:{PORT}")

while True:
    # Recebe os dados e o endereço do remetente
    data, addr = server_socket.recvfrom(1024)

    # Exibe a mensagem recebida
    print(f"Recebido de {addr}: {data.decode('utf-8')}")

    if data.decode('utf-8').lower() == 'exit':
        break

# Fecha o socket
server_socket.close()
