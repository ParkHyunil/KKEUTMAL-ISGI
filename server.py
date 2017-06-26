from socket import socket

class Server:
    def __init__(self, host="127.0.0.1", port=5005, first="정보보안"):
        self.host = host
        self.port = port
        self.users = []
        self.first = first
        self.server = socket()
        self.server.bind((self.host, self.port))
        self.server.listen(1)

    def main(self):
        for _ in range(2):
            conn, addr = self.server.accept()
            name = conn.recv(1024).decode()
            print(name + "님이 입장하셨습니다.")
            self.users.append(User(name, conn, addr))
        self.users[0].conn.send(self.first.encode())
        print("===== 게임을 시작하지 =====")
        print(self.first)
        while True:
            for i in range(2):
                word = self.users[i].recv()
                print("-> " + word + '('+self.users[i].name+')')
                self.users[i^1].send(word)
            if not word:
                break
        for user in self.users:
            user.conn.close()


class User:
    def __init__(self, name, conn, addr):
        self.name = name
        self.conn = conn
        self.addr = addr

    def recv(self):
        return self.conn.recv(1024).decode()

    def send(self, data):
        self.conn.send(data.encode())

if __name__ == '__main__':
    Server().main()
