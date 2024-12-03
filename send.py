import socket
from time import sleep


file_path = 'output.txt'


def read_data():
    try:
        with open('output.txt', 'r') as log:
            data = log.read()
        return data
    except FileNotFoundError:
        print(f"{file_path} n'existait pas et a été créé.")
        with open(file_path, 'w') as f:
            f.write('')
        return ''

    except Exception as e:
        print(f'an error as occured (reading files) : {e}')
        return None


def send_data(host, port, data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(data.encode('utf-8'))
    except socket.error as e:
        print(f"Erreur de socket: {e}")


def main():
    host = '127.0.0.1'  # Remplacez par l'adresse IP de votre serveur
    port = 5050

    while True:
        try:
            data = read_data()
            if data is not None:
                send_data(host, port, data)
            sleep(1)
        except Exception as e:
            print(f"Erreur inattendue (sending data ?): {e}")
        finally:
            sleep(10)
            print('fin d\'une boucle')