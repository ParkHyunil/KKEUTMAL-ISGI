from socket import socket

class Server:
    def __init__(self, host="127.0.0.1", port=5005):
        self.host = host
        self.port = port
        self.server = socket()
        self.server.bind((self.host, self.port))
        self.server.listen(1)

    def main(self):
        conn, addr = self.server.accept()
        name = conn.recv(1024).decode()
        print(name + "님이 입장하셨습니다.")
        first = input("시작단어를 입력하세요")
        conn.send(first.encode())
        print("===== 게임을 시작하지 =====")
        print(first)
        while True:
            word = conn.recv(1024).decode()
            print("-> " + word)
            word = input("-> ")
            conn.send(word.encode())
            if not word:
                break
        conn.close()

if __name__ == '__main__':
    Server().main()
