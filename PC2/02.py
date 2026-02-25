import socketserver

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        try:
            print("[{}]: open".format(self.client_address[0]))
            self.wfile.write(b"--- PKS server ---\r\n")
            while True:
                line = self.rfile.readline()
                if not line: #klient uzavrel spojeni
                    break
                sline = line.rstrip().upper()
                print("[{}]: RX: {}".format(self.client_address[0], sline))
                #zpracovani prikazu
                match sline:
                    case b'HELP' | b'?':
                        self.wfile.write(b"commands:\r\n")
                        self.wfile.write(b" HELP\r\n")
                        self.wfile.write(b" ID\r\n")
                        self.wfile.write(b" PC\r\n")
                        self.wfile.write(b" QUIT\r\n")
                    case b'ID':
                        self.wfile.write(b"id:\r\n")
                        self.wfile.write(b" 246850\r\n")
                    case b'PC':
                        self.wfile.write(b"pc:\r\n")
                        self.wfile.write(b" \r\n")
                    case b'QUIT':
                        self.wfile.write(b"Closing connection...\r\n")
                        break
                    case _:
                        self.wfile.write(sline)
                        self.wfile.write(b"\r\n")                   
        except Exception as e:
            print("[{}]: ER: {}".format(self.client_address[0], e))
        print("[{}]: disconnected".format(self.client_address[0]))
    
if __name__ == "__main__":
    HOST, PORT = "", 50000
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever() #lze prerusit pomoci Ctrl-C