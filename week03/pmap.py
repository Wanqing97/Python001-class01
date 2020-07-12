import subprocess
import socket
from concurrent.futures import ThreadPoolExecutor

success_list = []

def ping_one(ip_address):
    # ping单个ip地址，打印出有效的ip地址
    try:
        re = subprocess.run(["ping",ip_address, "-t", "2"], capture_output=True)
        if re.returncode == 0:
            print(ip_address)
    except Exception as e:
        print(e)
        print("Something went wrong with your ping program!")

def tcp_one(ip_port_tuple):
    # 用socket连接ip地址及端口，参数 ip_port_tuple 为一个元祖
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try:
        return_code = s.connect_ex(ip_port_tuple)
    except OSError as e:
        print('OS Error:', e)
        
    if return_code == 0:
        print("Connected.")
        success_list.append(ip_port_tuple[1])
    else:
        print('Unable to connect.')

def ping_func(n, f, ip):
    # 把ip地址格式标准化，用map方式加入线程池
    if f == 'ping':
        if '-' in ip:
            start_ip, stop_ip = ip.split('-')
            start_last_num = start_ip.split('.')[-1]
            stop_last_num = stop_ip.split('.')[-1]
            start_head = start_ip.rstrip(start_last_num).rstrip('.')
            seed = [start_head + '.' + str(num) for num in range(int(start_last_num), int(stop_last_num)+1)]
            with ThreadPoolExecutor(n) as executor:
                executor.map(ping_one, seed)
        else:
            ping_one(ip)
    elif f == 'tcp':
        seed = [(ip, port) for port in range(0, 65536)]
        with ThreadPoolExecutor(n) as executor:
            executor.map(tcp_one, seed)
        print(f'IP地址{ip}的所有开放端口是：{success_list}\n')
    else:
        print("You can call 'ping' or 'tcp' function, anything else is prohibited!")

ping_func(2,'ping','192.168.0.1')