import socket

class HTTPServer:
    def __init__(self,ip,port):
        print("Socket successfully created")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        s.bind((ip,port))        
        print ("socket binded to %s" %(port))
        s.listen(5)      
        print("socket is listening")          
        while True:
            c, addr = s.accept()
            print('Got connection from', addr).
            from_client = c.recv(1024).decode()
            print("from Client : "+from_client)
            http_response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n"
            content = "<h1>Webserver Under construction</h1>"
            http_response = http_response + "Content Length" + str(len(content)) + "\r\n\r\n"
            http_response = http_response + content
            c.sendall(http_response.encode())
            c.close()

def main():
    HTTPServer('127.0.0.1', 8888)

if __name__ == "__main__":
    main()            

