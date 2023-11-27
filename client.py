import socket

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 8082

# Cria um socket UDP
client_socket = socket.socket(
    socket.AF_INET,  # IPv4
    socket.SOCK_DGRAM  # UDP | Socket tipo DATAGRAM
)

while True:
    # Solicita que o usuário insira uma mensagem
    message = input("Digite uma mensagem para enviar ao servidor (ou 'exit' para sair): ")

    # Envia a mensagem ao servidor
    client_socket.sendto(message.encode('utf-8'), (HOST, PORT))

    if message.lower() == 'exit':
        break

# Fecha o socket
client_socket.close()
