# Cliente-Servidor em Python usando UDP

Este é um simples exemplo de uma aplicação cliente-servidor em Python 
que utiliza o protocolo UDP. O programa consiste em 
um servidor que aguarda mensagens de um cliente, em loop, e ao receber uma mensagem 
de algum cliente, exibe essa mensagem. O cliente, por sua vez, envia mensagens, 
digitadas pelo usuário, ao servidor.

## Pré-requisitos

- Python 3.x instalado (pode ser baixado em [python.org](https://www.python.org/downloads/))

## Como usar

1. Clone este repositório:

   ```bash
   git clone https://github.com/Wanderson-Fer/cliente-servidor_UDP.git
   ```

   ou faça o download do código-fonte como um arquivo ZIP.

2. Abra dois terminais.

3. Navegue até o diretório do projeto:

   ```bash
   cd caminho-ate-o-repositorio/cliente-servidor_UDP
   ```

4. Em um terminal, execute o servidor:

   ```bash
   python server.py
   ```

5. No outro terminal, execute o cliente:

   ```bash
   python client.py
   ```

6. Observe as mensagens exibidas nos terminais. 
   O cliente pedirá que uma mensagem seja digitada, para enviar ao servidor,
   e o servidor exibirá essa mensagem.

7. Para encerrar os programas, digite "exit" quando solicitado a inserir 
   uma mensagem na aplicação cliente. 

## Customização

- As configurações de host e porta podem ser ajustadas no código conforme necessário.

## Notas

- Este código não lida com desconexões inesperadas ou outros cenários de erro 
  que podem ocorrer em uma aplicação do mundo real. Considere esses aspectos 
  ao adaptar para casos de uso mais complexos.
