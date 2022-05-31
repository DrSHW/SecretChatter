import socket
import threading
import os


def send_msg(udp_socket, dest_address, dest_port):
    """
    Send message to server
    """
    while True:
        msg = input("请输入要发送的数据:(输入exit以退出) ")

        if msg == "exit":
            udp_socket.close()
            os._exit(0)
        # 这里的ip和端口号可以自己指定
        udp_address = (dest_address, dest_port)

        udp_socket.sendto(msg.encode("utf-8"), udp_address)

        print("消息已发送")




def recv_msg(udp_socket):
    """
    Receive message from server
    """
    while True:
        recv_data = udp_socket.recvfrom(1024)

        print(f"收到来自{str(recv_data[1])}的数据: {recv_data[0].decode('utf-8')}")


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # ip和端口号可以自己指定
    local_address = ('', 7788)
    udp_socket.bind(local_address)

    t1 = threading.Thread(target=send_msg, args=(udp_socket, '192.168.43.157', 7788, ))
    t2 = threading.Thread(target=recv_msg, args=(udp_socket,))

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
