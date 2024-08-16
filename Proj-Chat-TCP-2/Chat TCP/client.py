import socket
import threading

# Escolhendo um apelido
nickname = input("Escolha seu apelido: ")

# Conectando ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Função para ouvir o servidor e enviar o apelido
def receive():
    while True:
        try:
            # Receber mensagem do servidor
            # Se a mensagem for 'NICK', enviar o apelido
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Fechar conexão em caso de erro
            print("Ocorreu um erro!")
            client.close()
            break
        
# Função para enviar mensagens ao servidor
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
        
# Iniciando threads para ouvir e escrever
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
