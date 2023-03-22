import socket
import threading
import argparse

def scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        print(f"{ip}")
        s.close()
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description='Port scanner')
    parser.add_argument('-s', '--subnet', type=str, required=True, help='Subnet IP address (e.g. 192.168.1)')
    args = parser.parse_args()

    for i in range(1, 255):
        ip = f"{args.subnet}.{i}"
        threading.Thread(target=scan, args=(ip, 2096)).start()

if __name__ == '__main__':
    main()
