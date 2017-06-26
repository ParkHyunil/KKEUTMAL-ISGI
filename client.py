from socket import socket
import sys

class Finder:
    def __init__(self, filename):
        self.dic = []
        self.load(filename)

    def findWord(self, word):
        for next_word in self.dic:
            if next_word[0] == word[-1]:
                return next_word

    def load(self, filename):
        source = open(filename+".txt", 'r')
        lines = source.readlines()
        for line in lines:
            self.dic += line.split()
        source.close()

class Client(Finder):
    def __init__(self, name: str, filename: str, host="127.0.0.1", port=5005):
        super().__init__(self, filename)
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
    Client(sys.argv[1], sys.argv[2]).main()
