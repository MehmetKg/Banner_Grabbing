import socket

ip = 'target_ip'

for port in range(1, 100):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        s.connect((ip, port))

        try:
            response = s.recv(1024)
            print(f"Port {port} open : Banner : {response.decode()}")
        except socket.timeout:
            if port == 80:
                http_message = "GET / HTTP/1.0\r\n\r\n"
                s.send(http_message.encode())
                http_response = s.recv(1024)
                print(f"Port {port} open : HTTP Response : {http_response.decode()}")
            else:
                print(f"Port {port} : Open but different method needed")
    except Exception as e:
        print(f"Port {port} closed : Reason : {e}")
    finally:
        s.close()