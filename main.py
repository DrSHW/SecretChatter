import socket


def send_msg(udp_socket):
    """
    Send message to server
    """
    msg = input("请输入要发送的数据: ")

    # 这里的ip和端口号可以自己指定
    udp_address = ('192.168.43.157', 7788)

    udp_socket.sendto(msg.encode("utf-8"), udp_address)

    print("消息已发送")


def recv_msg(udp_socket):
    """
    Receive message from server
    """
    recv_data = udp_socket.recvfrom(1024)

    print(f"收到来自{str(recv_data[1])}的数据: {recv_data[0].decode('utf-8')}")


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # ip和端口号可以自己指定
    local_address = ('', 7788)
    udp_socket.bind(local_address)
    while True:
        mode = input("请输入功能(send/recv)，输入exit已退出系统: ")
        if mode == "send":
            send_msg(udp_socket)
        elif mode == "recv":
            recv_msg(udp_socket)
        elif mode == "exit":
            break
        else:
            print("输入不合法")

    udp_socket.close()


if __name__ == '__main__':
    main()
