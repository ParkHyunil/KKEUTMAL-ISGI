from socket import socket
import sys

class Finder:
    """
    txt파일을 소스로 하여 사전을 만드는 예시임
    여러분의 상상력으로 이부분을 만들어서 1등을 해보세요
    """
    def __init__(self, filename):
        self.dic = []
        self.load(filename)

    def findWord(self, word):
        for next_word in self.dic:
            if next_word[0] == word[-1]:
                return next_word

    def load(self, filename):
        try:
            source = open(filename+".txt", 'r')
        except:
            print("파일이 존재하지 않습니다.")
        else:
            lines = source.readlines()
            for line in lines:
                self.dic += line.split()
            source.close()

class Client(Finder):
    def __init__(self, name: str, filename: str, host="127.0.0.1", port=5005):
        super().__init__(filename)
        self.host = host
        self.port = port
        self.server = socket()
        self.server.connect((host, port))
        self.server.send(name.encode())

    def main(self):
        while True:
            word = self.recv()
            if not word:
                break
            print("받은 단어 :", word)
            next_word = self.findWord(word)
            print("찾은 단어 :", next_word)
            self.send(next_word)
        self.server.close()

    def recv(self):
        return self.server.recv(1024).decode()

    def send(self, data):
        self.server.send(data.encode())

if __name__ == '__main__':
    try:
        Client(sys.argv[1], sys.argv[2]).main()
    except:
        print("사용법 : python3 client.py <username> <filename>")

