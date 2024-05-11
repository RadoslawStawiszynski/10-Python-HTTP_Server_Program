# STAWISZYNSKI RADOSLAW , NR INDEKSU 159088, 
# ROK 2022/2023, WYDZIAL INFORMATYKA, GRUPA D1, SEM 2

import http.server
import socketserver
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
import paramiko
import socket
import threading

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            super().do_GET()
            # Dodatkowe logowanie zdarzenia dla HTTP
            print(f"Zapytanie HTTP od {self.client_address[0]}: {self.path}")
        except Exception as e:
            print(f"Błąd HTTP: {e}")

class MyFTPHandler(FTPHandler):
    def log(self, msg):
        super(MyFTPHandler, self).log(msg)
        print(f"FTP Log: {msg}")

def start_ftp_server():
    try:
        authorizer = DummyAuthorizer()
        authorizer.add_user("user", "password", "/path/to/ftp/folder", perm="elradfmw")
        authorizer.add_anonymous("/path/to/ftp/folder", perm="elradfmw")

        handler = MyFTPHandler
        handler.authorizer = authorizer

        ftp_server = socketserver.ThreadingTCPServer(("localhost", 2121), handler)
        print("FTP Server działa na porcie 2121")
        ftp_server.serve_forever()
    except Exception as e:
        print(f"Błąd FTP: {e}")

def start_ssh_server():
    try:
        host_key = paramiko.RSAKey(filename="/path/to/private/key")
        ssh_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssh_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ssh_server.bind(("localhost", 2222))

        ssh_server.listen(10)
        print("SSH Server nasłuchuje na porcie 2222")

        while True:
            client, addr = ssh_server.accept()
            transport = paramiko.Transport(client)
            transport.add_server_key(host_key)

            server = paramiko.SSHServer()
            server.set_subsystem_handler(
                "sftp", paramiko.SFTPServer, {"chroot": "/path/to/sftp/folder"}
            )
            transport.start_server(server=server)
    except Exception as e:
        print(f"Błąd SSH: {e}")

if __name__ == "__main__":
    try:
        # Uruchomienie serwera HTTP
        http_thread = threading.Thread(target=http.server.HTTPServer(("localhost", 8000), MyHTTPRequestHandler).serve_forever)
        http_thread.start()

        # Uruchomienie serwera FTP
        ftp_thread = threading.Thread(target=start_ftp_server)
        ftp_thread.start()

        # Uruchomienie serwera SSH
        ssh_thread = threading.Thread(target=start_ssh_server)
        ssh_thread.start()

        http_thread.join()
        ftp_thread.join()
        ssh_thread.join()

    except KeyboardInterrupt:
        print("\nZamykanie programu.")
